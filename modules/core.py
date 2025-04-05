class Interprete:
    def __init__(self):
        self.variables = {}
        self.tipos = {}
        self.funciones = {}
        self.llamadas = []
        self.salida = []  # Lista para almacenar las salidas
        self.entrada = []  # Lista para almacenar las entradas del usuario

    def ejecutar(self, codigo):
        self.salida = []  # Reiniciar las salidas en cada ejecución
        lineas = codigo.strip().split('\n')
        self._ejecutar_bloque(lineas)
        return self.salida  # Devolver las salidas generadas

    def _ejecutar_bloque(self, lineas, i=0):
        while i < len(lineas):
            linea = lineas[i].strip()
            if not linea:
                i += 1
                continue
            if linea.startswith("mostrar("):
                self._mostrar(linea)
            elif linea.startswith("leer("):
                self._leer(linea)
            elif linea.startswith("declarar "):
                self._declarar(linea)
            elif "=" in linea and not linea.startswith("si") and not linea.startswith("hacer"):
                self._asignar(linea)
            elif linea.startswith("si ("):
                i = self._si(lineas, i)
            elif linea.startswith("repetir si ("):
                i = self._repetir_si(lineas, i)
            elif linea.startswith("hacer hasta ("):
                i = self._hacer_hasta(lineas, i)
            elif linea.startswith("definir "):
                i = self._definir_funcion(lineas, i)
            elif linea.startswith("llamar "):
                self._llamar_funcion(linea)
            else:
                self.salida.append(f"Instrucción no reconocida: {linea}")
            i += 1

    def _mostrar(self, linea):
        contenido = linea[len("mostrar("):-1].strip()
        if contenido.startswith('"') and contenido.endswith('"'):
            self.salida.append(contenido[1:-1])  # Agregar texto a la salida
        elif contenido in self.variables:
            self.salida.append(str(self.variables[contenido]))  # Agregar valor de la variable a la salida
        else:
            self.salida.append("Error: variable no encontrada")

    def _leer(self, linea):
        nombre_var = linea[len("leer("):-1].strip()
        if self.entrada:
            valor = self.entrada.pop(0)  # Obtener el valor de la lista de entradas
            self.variables[nombre_var] = valor
        else:
            self.salida.append(f"Error: no hay entrada para la variable {nombre_var}")

    def _declarar(self, linea):
        partes = linea[len("declarar "):].split()
        if len(partes) >= 2:
            nombre, tipo = partes[0], partes[1]
            self.variables[nombre] = None
            self.tipos[nombre] = tipo
        else:
            self.salida.append("Error en declaración.")

    def _asignar(self, linea):
        nombre, valor = [x.strip() for x in linea.split("=", 1)]
        if valor.startswith('"') and valor.endswith('"'):
            valor = valor[1:-1]
        elif valor.isdigit():
            valor = int(valor)
        elif valor in self.variables:
            valor = self.variables[valor]
        self.variables[nombre] = valor

    def _si(self, lineas, i):
        condicion = lineas[i][lineas[i].find('(')+1 : lineas[i].find(')')]
        if self._evaluar_condicion(condicion):
            bloque, salto = self._leer_bloque(lineas, i + 1)
            self._ejecutar_bloque(bloque)
        else:
            _, salto = self._leer_bloque(lineas, i + 1)
        return salto

    def _repetir_si(self, lineas, i):
        condicion = lineas[i][lineas[i].find('(')+1 : lineas[i].find(')')]
        bloque, salto = self._leer_bloque(lineas, i + 1)
        while self._evaluar_condicion(condicion):
            self._ejecutar_bloque(bloque)
        return salto

    def _hacer_hasta(self, lineas, i):
        condicion = lineas[i][lineas[i].find('(')+1 : lineas[i].find(')')]
        bloque, salto = self._leer_bloque(lineas, i + 1)
        while not self._evaluar_condicion(condicion):
            self._ejecutar_bloque(bloque)
        return salto
    
    def _definir_funcion(self, lineas, i):
        cabecera = lineas[i]
        nombre = cabecera[cabecera.find("definir") + 8: cabecera.find("(")].strip()
        params = cabecera[cabecera.find("(")+1 : cabecera.find(")")].strip().split(",")
        cuerpo, salto = self._leer_bloque(lineas, i + 1)
        self.funciones[nombre] = {"params": [p.strip() for p in params if p], "cuerpo": cuerpo}
        return salto

    def _llamar_funcion(self, linea):
        nombre = linea[len("llamar "):].strip()
        if nombre in self.funciones:
            self._ejecutar_bloque(self.funciones[nombre]["cuerpo"])
        else:
            self.salida.append(f"Función '{nombre}' no definida.")

    def _evaluar_condicion(self, cond):
        for op in ["==", "!=", ">", "<", ">=", "<="]:
            if op in cond:
                izquierda, derecha = cond.split(op)
                izquierda = izquierda.strip()
                derecha = derecha.strip()
                if izquierda in self.variables:
                    izquierda = self.variables[izquierda]
                if derecha in self.variables:
                    derecha = self.variables[derecha]
                try:
                    return eval(f"{repr(izquierda)} {op} {repr(derecha)}")
                except:
                    return False
        return False
    
    def _leer_bloque(self, lineas, i):
        bloque = []
        while i < len(lineas):
            linea = lineas[i]
            if linea.startswith("    ") or linea.startswith("\t"):
                bloque.append(linea.strip())
                i += 1
            else:
                break
        return bloque, i - 1