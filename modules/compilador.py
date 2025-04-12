import re
import sys

class Compilador:
    def __init__(self):
        self.variables = {}
        self.functions = {}
        self.indentacion = 0
        self.return_value = None

    def mostrar(self, *mensajes):
        """Maneja la instrucción mostrar()"""
        partes = []
        for msg in mensajes:
            if msg in self.variables:
                partes.append(str(self.variables[msg]))
            else:
                msg_str = str(msg).replace('"', '').replace("'", "").replace('\\line', '\n')
                partes.append(msg_str)
        print('  ' * self.indentacion + ' '.join(partes))

    def leer(self, variable):
        """Maneja la instrucción leer()"""
        valor = input(f'  ' * self.indentacion + f"Ingrese valor para {variable}: ")
        self.variables[variable] = self.parse_valor(valor)

    def parse_valor(self, valor):
        """Convierte el valor al tipo adecuado"""
        if valor is None:
            return None
        valor = str(valor).strip()
        if valor.isdigit():
            return int(valor)
        try:
            return float(valor)
        except ValueError:
            return valor

    def evaluar_operacion(self, operacion, op1, op2):
        """Evalúa operaciones aritméticas básicas"""
        op1_val = self.evaluar_expresion(op1)
        op2_val = self.evaluar_expresion(op2)
        
        if operacion == 'suma':
            return op1_val + op2_val
        elif operacion == 'resta':
            return op1_val - op2_val
        elif operacion == 'multiplicar':
            return op1_val * op2_val
        elif operacion == 'dividir':
            if op2_val == 0:
                raise ValueError("División por cero")
            return op1_val / op2_val
        else:
            raise ValueError(f"Operación no reconocida: {operacion}")

    def ejecutar(self, codigo):
        """Ejecuta el código de pseudocódigo"""
        if isinstance(codigo, list):
            lineas = [linea.strip() for linea in codigo if linea.strip()]
        else:
            lineas = [linea.strip() for linea in codigo.split('\n') if linea.strip()]
        
        i = 0
        while i < len(lineas):
            linea = lineas[i]
            try:
                if not linea:
                    i += 1
                    continue
                    
                if linea.startswith('Inicio'):
                    print("\n=== INICIANDO EJECUCIÓN ===")
                elif linea.startswith('Fin'):
                    print("\n=== EJECUCIÓN FINALIZADA ===")
                elif linea.startswith('mostrar('):
                    self.procesar_mostrar(linea)
                elif linea.startswith('leer('):
                    self.procesar_leer(linea)
                elif linea.startswith('declarar'):
                    self.procesar_declaracion(linea)
                elif linea.startswith('si ') and 'ejecutar:' in linea:
                    i = self.procesar_condicional(lineas, i)
                elif linea.startswith('si no:'):
                    pass
                elif linea.startswith('repetir si'):
                    i = self.procesar_repetir_si(lineas, i)
                elif linea.startswith('hacer hasta'):
                    i = self.procesar_hacer_hasta(lineas, i)
                elif linea.startswith('definir '):
                    i = self.procesar_definir_funcion(lineas, i)
                elif linea.startswith('retornar '):
                    self.procesar_retorno(linea)
                elif any(op in linea for op in ['suma(', 'resta(', 'multiplicar(', 'dividir(']):
                    self.procesar_operacion_aritmetica(linea)
                elif '=' in linea:
                    self.procesar_asignacion(linea)
                elif '(' in linea and ')' in linea:
                    if not any(linea.startswith(kw) for kw in ['mostrar', 'leer', 'si', 'repetir', 'hacer', 'definir']):
                        self.procesar_llamada_funcion(linea)
                i += 1
            except Exception as e:
                print(f"Error en línea {i+1}: {str(e)} - Línea: '{linea}'")
                break

    def procesar_operacion_aritmetica(self, linea):
        """Procesa operaciones aritméticas como suma(a,b)"""
        if '=' in linea:
            var, resto = linea.split('=', 1)
            var = var.strip()
            match = re.search(r'(\w+)\((.*?),(.*?)\)', resto.strip())
        else:
            var = None
            match = re.search(r'(\w+)\((.*?),(.*?)\)', linea)
        
        if not match:
            raise ValueError("Sintaxis incorrecta en operación aritmética")
        
        operacion = match.group(1)
        op1 = match.group(2).strip()
        op2 = match.group(3).strip()
        
        resultado = self.evaluar_operacion(operacion, op1, op2)
        
        if var is not None:
            self.variables[var] = resultado
        return resultado

    def procesar_mostrar(self, linea):
        """Procesa la instrucción mostrar()"""
        contenido = re.search(r'mostrar\((.*)\)', linea).group(1)
        partes = [p.strip() for p in re.split(r'(?<!\\),', contenido) if p.strip()]
        
        mensajes = []
        for parte in partes:
            parte = parte.replace('\,', ',')
            if parte in self.variables:
                mensajes.append(self.variables[parte])
            else:
                mensajes.append(parte.replace('"', '').replace("'", ""))
        
        self.mostrar(*mensajes)

    def procesar_leer(self, linea):
        """Procesa la instrucción leer()"""
        var = re.search(r'leer\((.*)\)', linea).group(1).strip()
        self.leer(var)

    def procesar_declaracion(self, linea):
        """Procesa declaración de variables"""
        partes = linea.split()
        nombre = partes[1]
        self.variables[nombre] = None

    def procesar_condicional(self, lineas, indice):
        """Procesa estructura si..."""
        linea = lineas[indice]
        match = re.search(r'si \((.*)\) ejecutar:', linea)
        if not match:
            raise ValueError("Sintaxis incorrecta en condicional")
        
        condicion = match.group(1).strip()
        resultado = self.evaluar_expresion(condicion)
        
        indice_else = -1
        temp_indice = indice + 1
        nivel = 1
        
        while temp_indice < len(lineas) and nivel > 0:
            current_line = lineas[temp_indice]
            if current_line.startswith('si ') and 'ejecutar:' in current_line:
                nivel += 1
            elif current_line.startswith('si no:') and nivel == 1:
                indice_else = temp_indice
            elif current_line.startswith('fin si'):
                nivel -= 1
            temp_indice += 1
        
        if resultado:
            fin_bloque = indice_else if indice_else != -1 else self.encontrar_fin(lineas, indice, 'fin si')
            return self.ejecutar_bloque(lineas, indice + 1, fin_bloque)
        elif indice_else != -1:
            fin_bloque = self.encontrar_fin(lineas, indice_else, 'fin si')
            return self.ejecutar_bloque(lineas, indice_else + 1, fin_bloque)
        else:
            return self.encontrar_fin(lineas, indice, 'fin si')

    def procesar_retorno(self, linea):
        """Procesa instrucción retornar"""
        expresion = linea.split('retornar')[1].strip()
        self.return_value = self.evaluar_expresion(expresion)

    def procesar_asignacion(self, linea):
        """Procesa asignación de variables"""
        var, expr = linea.split('=', 1)
        var = var.strip()
        self.variables[var] = self.evaluar_expresion(expr.strip())

    def evaluar_expresion(self, expresion):
        """Evalúa una expresión"""
        try:
            for var in sorted(self.variables.keys(), key=len, reverse=True):
                if var in expresion:
                    expresion = expresion.replace(var, str(self.variables[var]))
            return eval(expresion, {}, {})
        except:
            return expresion

    def procesar_definir_funcion(self, lineas, indice):
        """Procesa definición de función"""
        linea = lineas[indice]
        match = re.search(r'definir (\w+)\((.*)\):', linea)
        nombre_func = match.group(1)
        params = [p.strip() for p in match.group(2).split(',') if p.strip()]
        
        fin_definir = self.encontrar_fin(lineas, indice, 'fin definir')
        cuerpo = lineas[indice+1:fin_definir]
        
        self.functions[nombre_func] = {
            'params': params,
            'body': cuerpo
        }
        
        return fin_definir

    def procesar_llamada_funcion(self, linea):
        """Procesa llamada a función"""
        match = re.search(r'(\w+)\((.*)\)', linea)
        nombre_func = match.group(1)
        args = [arg.strip() for arg in match.group(2).split(',') if arg.strip()]
        
        if nombre_func not in self.functions:
            raise NameError(f"Función '{nombre_func}' no definida")
        
        funcion = self.functions[nombre_func]
        if len(args) != len(funcion['params']):
            raise TypeError(f"Número incorrecto de argumentos para {nombre_func}")
        
        vars_originales = self.variables.copy()
        self.variables = {}
        
        for param, arg in zip(funcion['params'], args):
            self.variables[param] = self.evaluar_expresion(arg)
        
        self.return_value = None
        self.ejecutar(funcion['body'])
        resultado = self.return_value
        
        self.variables = vars_originales
        
        if '=' in linea:
            var = linea.split('=')[0].strip()
            self.variables[var] = resultado
        
        return resultado

    def procesar_repetir_si(self, lineas, indice):
        """Procesa estructura repetir si (while)"""
        linea = lineas[indice]
        match = re.search(r'repetir si \((.*)\) ejecutar:', linea)
        if not match:
            raise ValueError("Sintaxis incorrecta en repetir si")
        
        condicion = match.group(1).strip()
        inicio_bloque = indice + 1
        fin_bloque = self.encontrar_fin(lineas, inicio_bloque, 'fin repetir')
        
        while self.evaluar_expresion(condicion):
            self.indentacion += 1
            for i in range(inicio_bloque, fin_bloque):
                self.ejecutar([lineas[i]])
            self.indentacion -= 1
        
        return fin_bloque

    def procesar_hacer_hasta(self, lineas, indice):
        """Procesa estructura hacer hasta (do-while)"""
        linea = lineas[indice]
        match = re.search(r'hacer hasta \((.*)\):', linea)
        if not match:
            raise ValueError("Sintaxis incorrecta en hacer hasta")
        
        condicion = match.group(1).strip()
        inicio_bloque = indice + 1
        fin_bloque = self.encontrar_fin(lineas, inicio_bloque, 'fin hacer')
        
        while True:
            self.indentacion += 1
            for i in range(inicio_bloque, fin_bloque):
                self.ejecutar([lineas[i]])
            self.indentacion -= 1
            
            if not self.evaluar_expresion(condicion):
                break
        
        return fin_bloque

    def ejecutar_bloque(self, lineas, inicio, fin):
        """Ejecuta un bloque de código"""
        self.indentacion += 1
        for i in range(inicio, fin):
            self.ejecutar([lineas[i]])
        self.indentacion -= 1
        return fin

    def encontrar_fin(self, lineas, inicio, marcador):
        """Encuentra el fin de un bloque"""
        for i in range(inicio, len(lineas)):
            if lineas[i].startswith(marcador):
                return i
        return len(lineas)

def main():
    codigo = """
Inicio (OperacionesAritmeticas)
    declarar a tipo: entero
    declarar b tipo: entero
    declarar resultado tipo: entero
    
    mostrar("Ingrese primer número:")
    leer(a)
    mostrar("Ingrese segundo número:")
    leer(b)
    
    resultado = suma(a, b)
    mostrar("Suma:", resultado)
    
    resultado = resta(a, b)
    mostrar("Resta:", resultado)
    
    resultado = multiplicar(a, b)
    mostrar("Multiplicación:", resultado)
    
    resultado = dividir(a, b)
    mostrar("División:", resultado)
Fin
"""
    compilador = Compilador()
    compilador.ejecutar(codigo)

if __name__ == "__main__":
    main()