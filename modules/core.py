class TraductorJS:
    def __init__(self):
        self.variables = set()
        self.funciones = {}
        self.indentacion = 0
        self.resultado = []
        self.bloques_abiertos = []  # Pila para seguir los bloques abiertos
    
    def agregar_linea(self, linea):
        """Agrega una línea de código con la indentación correcta."""
        self.resultado.append("  " * self.indentacion + linea)
    
    def traducir(self, codigo_fuente):
        """Traduce el código fuente completo a JavaScript."""
        lineas = codigo_fuente.strip().split('\n')
        self.resultado = []
        # Verificar estructura básica
        if not lineas or not lineas[0].startswith("Inicio") or lineas[-1] != "Fin":
            return "Error: El código debe comenzar con 'Inicio' y terminar con 'Fin'"
        # Extraer nombre del algoritmo
        nombre_algoritmo = lineas[0][lineas[0].find("(")+1:lineas[0].find(")")]
        self.agregar_linea(f"// Programa: {nombre_algoritmo}")
        self.agregar_linea("")
        # Procesar líneas (omitiendo Inicio y Fin)
        i = 1
        while i < len(lineas) - 1:
            i = self.procesar_linea(lineas, i)
        # Cerrar bloques que quedaron abiertos
        while self.bloques_abiertos:
            tipo = self.bloques_abiertos.pop()
            self.cerrar_bloque(tipo)
        return "\n".join(self.resultado)
    
    def procesar_linea(self, lineas, indice):
        """Procesa una línea de código y actualiza el índice si es necesario."""
        linea = lineas[indice].strip()
        if not linea:
            return indice + 1
        # Declaración de variables
        if linea.startswith("declarar "):
            self.procesar_declaracion(linea)
        # Mostrar en consola
        elif linea.startswith("mostrar("):
            self.procesar_mostrar(linea)
        # Leer entrada
        elif linea.startswith("leer("):
            self.procesar_leer(linea)
        # Asignación
        elif "=" in linea and not "==" in linea and not "!=" in linea and not "<=" in linea and not ">=" in linea:
            self.procesar_asignacion(linea)
        # Condicional if
        elif linea.startswith("si ("):
            return self.procesar_condicional(lineas, indice)
        # Condicional else
        elif linea == "si no:":
            self.procesar_else()
        # Bucle while
        elif linea.startswith("repetir si ("):
            return self.procesar_while(lineas, indice)
        # Retorno de función
        elif linea.startswith("retornar "):
            self.procesar_retorno(linea)
        # Verificar si es el final de un bloque
        elif linea in ["fin si", "fin repetir", "fin hacer", "fin definir"]:
            self.cerrar_bloque(self.bloques_abiertos.pop() if self.bloques_abiertos else None)
        return indice + 1
    
    def procesar_declaracion(self, linea):
        """Procesa una declaración de variable."""
        partes = linea.replace("declarar ", "").split(" tipo: ")
        nombre_var = partes[0].strip()
        tipo = partes[1].strip()
        self.variables.add(nombre_var)
        self.agregar_linea(f"let {nombre_var};")
    
    def procesar_mostrar(self, linea):
        """Procesa una instrucción de mostrar en consola."""
        contenido = linea[linea.find("(")+1:linea.rfind(")")]
        
        # Manejar concatenación con :
        if ":" in contenido and not (contenido.startswith('"') and contenido.endswith('"')):
            partes = contenido.split(":")
            partes_js = []
            for parte in partes:
                parte = parte.strip()
                # Manejar strings y variables
                if parte.startswith('"') and parte.endswith('"'):
                    parte = parte.replace("\\line", "\\n")
                partes_js.append(parte)
            
            self.agregar_linea(f"console.log({' + '.join(partes_js)});")
        else:
            # Solo un valor
            contenido = contenido.replace("\\line", "\\n")
            self.agregar_linea(f"console.log({contenido});")
    
    def procesar_leer(self, linea):
        """Procesa una instrucción de lectura."""
        var_nombre = linea[linea.find("(")+1:linea.rfind(")")]
        # En JavaScript usamos prompt para entrada
        self.agregar_linea(f"{var_nombre} = prompt('Ingrese {var_nombre}');")
    
    def procesar_asignacion(self, linea):
        """Procesa una asignación de variable."""
        partes = linea.split("=", 1)
        nombre_var = partes[0].strip()
        valor = partes[1].strip()
        # Reemplazar operadores lógicos si existen
        valor = valor.replace(" y ", " && ").replace(" o ", " || ")
        self.agregar_linea(f"{nombre_var} = {valor};")
    
    def procesar_condicional(self, lineas, indice):
        """Procesa una estructura condicional if."""
        linea = lineas[indice].strip()
        
        # Extraer condición
        condicion = linea[linea.find("(")+1:linea.rfind(")")]
        # Reemplazar operadores lógicos
        condicion = condicion.replace(" y ", " && ").replace(" o ", " || ")
        
        self.agregar_linea(f"if ({condicion}) {{")
        self.indentacion += 1
        self.bloques_abiertos.append("if")
        
        # Procesar el bloque del if
        siguiente_indice = indice + 1
        while siguiente_indice < len(lineas) and not (lineas[siguiente_indice].strip() == "si no:" or lineas[siguiente_indice].strip() == "fin si"):
            siguiente_indice = self.procesar_linea(lineas, siguiente_indice)
            
        # Verificar si hay un else
        if siguiente_indice < len(lineas) and lineas[siguiente_indice].strip() == "si no:":
            # Cerrar bloque del if antes de else
            self.indentacion -= 1
            self.agregar_linea("} else {")
            self.indentacion += 1
            
            # Procesar el bloque del else
            siguiente_indice += 1
            while siguiente_indice < len(lineas) and lineas[siguiente_indice].strip() != "fin si":
                siguiente_indice = self.procesar_linea(lineas, siguiente_indice)
        
        # Si encontramos el fin del bloque if, cerrarlo
        if siguiente_indice < len(lineas) and lineas[siguiente_indice].strip() == "fin si":
            if "if" in self.bloques_abiertos:
                self.bloques_abiertos.remove("if")
            self.indentacion -= 1
            self.agregar_linea("}")
            return siguiente_indice + 1
            
        return siguiente_indice
    
    def procesar_else(self):
        """Procesa una estructura condicional else."""
        self.indentacion -= 1
        self.agregar_linea("} else {")
        self.indentacion += 1
    
    def procesar_while(self, lineas, indice):
        """Procesa un bucle while."""
        linea = lineas[indice].strip()
        
        # Extraer condición
        condicion = linea[linea.find("(")+1:linea.rfind(")")]
        # Reemplazar operadores lógicos
        condicion = condicion.replace(" y ", " && ").replace(" o ", " || ")
        
        self.agregar_linea(f"while ({condicion}) {{")
        self.indentacion += 1
        self.bloques_abiertos.append("while")
        
        # Procesar el bloque del while
        siguiente_indice = indice + 1
        while siguiente_indice < len(lineas) and lineas[siguiente_indice].strip() != "fin repetir":
            siguiente_indice = self.procesar_linea(lineas, siguiente_indice)
        
        # Cerrar el bloque si corresponde
        if siguiente_indice < len(lineas) and lineas[siguiente_indice].strip() == "fin repetir":
            if "while" in self.bloques_abiertos:
                self.bloques_abiertos.remove("while")
            self.indentacion -= 1
            self.agregar_linea("}")
            return siguiente_indice + 1
        
        # Si no se encontró 'fin repetir', solo cerrar el bloque
        self.indentacion -= 1
        self.agregar_linea("}")
        return siguiente_indice
    
    def procesar_retorno(self, linea):
        """Procesa una instrucción de retorno."""
        valor = linea.replace("retornar ", "").strip()
        self.agregar_linea(f"return {valor};")
        
        if "function" in self.bloques_abiertos:
            self.bloques_abiertos.remove("function")
            self.indentacion -= 1
            self.agregar_linea("}")
    
    def cerrar_bloque(self, tipo=None):
        """Cierra un bloque de código."""
        self.indentacion -= 1
        if tipo == "do_while":
            # Para do-while, la condición debe estar en la misma línea que la llave de cierre
            # Nota: la condición real se maneja en procesar_do_while
            self.agregar_linea("} while (condicion);")
        else:
            # Para otros bloques, simplemente cierra con una llave
            self.agregar_linea("}")