import re
import sys

class Compilador:
    def __init__(self):
        self.variables = {}
        self.functions = {}
        self.indentacion = 0
        self.return_value = None
        self.operaciones_predefinidas = ['suma', 'resta', 'multiplicar', 'dividir']

    def mostrar(self, *mensajes):
        """Maneja la instrucción mostrar()"""
        partes = []
        for msg in mensajes:
            if isinstance(msg, str) and msg in self.variables:
                partes.append(str(self.variables[msg]))
            else:
                msg_str = str(msg).replace('"', '').replace("'", "").replace('\\line', '\n')
                partes.append(msg_str)
        print('  ' * self.indentacion + ' '.join(partes))

    def leer(self, variable):
        """Maneja la instrucción leer()"""
        valor = input(f'  ' * self.indentacion)
        self.variables[variable] = self.parse_valor(valor)

    def parse_valor(self, valor):
        """Convierte el valor al tipo adecuado"""
        if valor is None:
            return None
        valor = str(valor).strip()
        # Verificar si es un valor booleano
        if valor.lower() == 'verdadero':
            return True
        if valor.lower() == 'falso':
            return False
        # Verificar si es un número entero
        if valor.isdigit():
            return int(valor)
        # Verificar si es un número decimal
        try:
            return float(valor)
        except ValueError:
            # Es una cadena
            return valor

    def evaluar_operacion(self, operacion, op1, op2):
        """Evalúa operaciones aritméticas básicas"""
        op1_val = self.evaluar_expresion(op1)
        op2_val = self.evaluar_expresion(op2)
        
        # Convertir a números si es posible
        try:
            op1_val = float(op1_val) if isinstance(op1_val, str) and op1_val.replace('.', '', 1).isdigit() else op1_val
            op2_val = float(op2_val) if isinstance(op2_val, str) and op2_val.replace('.', '', 1).isdigit() else op2_val
        except:
            pass
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
                elif linea.startswith('si ('):  # Corregido para coincidir con TraductorJS
                    i = self.procesar_condicional(lineas, i)
                    continue  # No incrementamos i ya que procesar_condicional devuelve el nuevo índice
                elif linea == 'si no:': 
                    # Este caso se maneja dentro de procesar_condicional
                    pass
                elif linea.startswith('repetir si ('): 
                    i = self.procesar_repetir_si(lineas, i)
                    continue  # No incrementamos i
                elif linea.startswith('hacer hasta ('):  
                    i = self.procesar_hacer_hasta(lineas, i)
                    continue  # No incrementamos i
                elif linea.startswith('definir '):
                    i = self.procesar_definir_funcion(lineas, i)
                    continue  # No incrementamos i
                elif linea.startswith('retornar '):
                    self.procesar_retorno(linea)
                elif linea in ["fin si", "fin repetir", "fin hacer", "fin definir"]:
                    # Final de un bloque, se maneja en otras funciones
                    pass
                elif any(op in linea for op in [f'{op}(' for op in self.operaciones_predefinidas]):
                    self.procesar_operacion_aritmetica(linea)
                elif '=' in linea and not any(op in linea for op in ['==', '!=', '<=', '>=']):
                    self.procesar_asignacion(linea)
                elif '(' in linea and ')' in linea:
                    if not any(linea.startswith(kw) for kw in ['mostrar', 'leer', 'si', 'repetir', 'hacer', 'definir']):
                        self.procesar_llamada_funcion(linea)
                i += 1
            except Exception as e:
                print(f"Error en línea {i+1}: {str(e)} - Línea: '{linea}'")
                traceback = sys.exc_info()[2]
                print(f"Tipo de error: {type(e).__name__}")
                print(f"Archivo: {traceback.tb_frame.f_code.co_filename}")
                print(f"Línea: {traceback.tb_lineno}")
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
        # Manejar concatenación con :
        if ":" in contenido and not (contenido.startswith('"') and contenido.endswith('"')):
            partes = contenido.split(":")
            mensajes = []
            for parte in partes:
                parte = parte.strip()
                if parte in self.variables:
                    mensajes.append(self.variables[parte])
                else:
                    mensajes.append(parte.replace('"', '').replace("'", ""))
            self.mostrar(*mensajes)
        else:
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
        match = re.search(r'declarar\s+(\w+)\s+tipo:\s+(\w+)', linea)
        if match:
            nombre = match.group(1)
            tipo = match.group(2)
            self.variables[nombre] = None
        else:
            partes = linea.split()
            nombre = partes[1]
            self.variables[nombre] = None

    def procesar_condicional(self, lineas, indice):
        """Procesa estructura condicional if."""
        linea = lineas[indice].strip()
        
        # Extraer condición
        condicion = linea[linea.find("(")+1:linea.rfind(")")]
        # Reemplazar operadores lógicos
        condicion = condicion.replace(" y ", " and ").replace(" o ", " or ")
        resultado = self.evaluar_expresion(condicion)
        # Procesar el bloque del if
        siguiente_indice = indice + 1
        fin_si_encontrado = False
        
        while siguiente_indice < len(lineas) and not fin_si_encontrado:
            linea_actual = lineas[siguiente_indice].strip()
            
            if linea_actual == "si no:":
                if resultado:
                    fin_bloque = siguiente_indice
                    self.indentacion += 1
                    for i in range(indice + 1, fin_bloque):
                        if lineas[i].strip() not in ["", "si no:"]:
                            self.ejecutar([lineas[i]])
                    self.indentacion -= 1
                    while siguiente_indice < len(lineas) and lineas[siguiente_indice].strip() != "fin si":
                        siguiente_indice += 1
                    if siguiente_indice < len(lineas):
                        siguiente_indice += 1  # Saltar el "fin si"
                    fin_si_encontrado = True
                else:
                    siguiente_indice += 1
                    fin_bloque = siguiente_indice
                    while fin_bloque < len(lineas) and lineas[fin_bloque].strip() != "fin si":
                        fin_bloque += 1
                    
                    self.indentacion += 1
                    for i in range(siguiente_indice, fin_bloque):
                        if lineas[i].strip() not in ["", "si no:", "fin si"]:
                            self.ejecutar([lineas[i]])
                    self.indentacion -= 1
                    
                    siguiente_indice = fin_bloque
                    if siguiente_indice < len(lineas) and lineas[siguiente_indice].strip() == "fin si":
                        siguiente_indice += 1
                    fin_si_encontrado = True
            
            # Si encontramos "fin si" sin haber encontrado un "si no:" antes
            elif linea_actual == "fin si":
                if resultado:
                    # Si la condición es verdadera, ejecutamos el bloque if
                    self.indentacion += 1
                    for i in range(indice + 1, siguiente_indice):
                        if lineas[i].strip() not in ["", "fin si"]:
                            self.ejecutar([lineas[i]])
                    self.indentacion -= 1
                siguiente_indice += 1  # Saltar el "fin si"
                fin_si_encontrado = True
            else:
                siguiente_indice += 1
        
        return siguiente_indice

    def procesar_retorno(self, linea):
        """Procesa instrucción retornar"""
        expresion = linea.split('retornar')[1].strip()
        self.return_value = self.evaluar_expresion(expresion)

    def procesar_asignacion(self, linea):
        """Procesa asignación de variables"""
        var, expr = linea.split('=', 1)
        var = var.strip()
        expr = expr.strip()
        # Reemplazar operadores lógicos si existen
        expr = expr.replace(" y ", " and ").replace(" o ", " or ")
        self.variables[var] = self.evaluar_expresion(expr)

    def evaluar_expresion(self, expresion):
        """Evalúa una expresión"""
        # Reemplazar operadores de comparación
        expresion = expresion.replace("==", "==").replace("!=", "!=")
        
        # Reemplazar valores booleanos
        expresion = expresion.replace("verdadero", "True").replace("falso", "False")
        
        try:
            # Reemplazar variables por sus valores
            for var in sorted(self.variables.keys(), key=len, reverse=True):
                if var in expresion:
                    valor = self.variables[var]
                    if isinstance(valor, str):
                        expresion = re.sub(r'\b' + var + r'\b', f"'{valor}'", expresion)
                    else:
                        expresion = re.sub(r'\b' + var + r'\b', str(valor), expresion)
            # Evaluar la expresión
            return eval(expresion, {"__builtins__": {}}, {})
        except Exception as e:
            return expresion

    def procesar_definir_funcion(self, lineas, indice):
        """Procesa definición de función"""
        linea = lineas[indice]
        match = re.search(r'definir (\w+)\((.*)\):', linea)
        if not match:
            match = re.search(r'definir (\w+)\((.*)\)', linea)
            if not match:
                raise ValueError(f"Sintaxis incorrecta en definir función: {linea}")
        
        nombre_func = match.group(1)
        params = [p.strip() for p in match.group(2).split(',') if p.strip()]
        
        fin_definir = self.encontrar_fin(lineas, indice, 'fin definir')
        cuerpo = lineas[indice+1:fin_definir]
        
        self.functions[nombre_func] = {
            'params': params,
            'body': cuerpo
        }
        
        return fin_definir + 1

    def procesar_llamada_funcion(self, linea):
        """Procesa llamada a función"""
        if '=' in linea:
            var, resto = linea.split('=', 1)
            var = var.strip()
            linea_func = resto.strip()
        else:
            var = None
            linea_func = linea.strip()
            
        match = re.search(r'(\w+)\((.*)\)', linea_func)
        if not match:
            raise ValueError(f"Sintaxis incorrecta en llamada a función: {linea}")
            
        nombre_func = match.group(1)
        args_str = match.group(2)
        
        args = []
        arg_start = 0
        arg_end = 0
        parentesis_depth = 0
        comillas_activas = False
        
        for i, char in enumerate(args_str):
            if char == '"' and (i == 0 or args_str[i-1] != '\\'):
                comillas_activas = not comillas_activas
            elif char == '(' and not comillas_activas:
                parentesis_depth += 1
            elif char == ')' and not comillas_activas:
                parentesis_depth -= 1
            elif char == ',' and parentesis_depth == 0 and not comillas_activas:
                args.append(args_str[arg_start:i].strip())
                arg_start = i + 1
                
        
        if arg_start < len(args_str):
            args.append(args_str[arg_start:].strip())
        
        # Si es una operación predefinida, manejarla directamente
        if nombre_func in self.operaciones_predefinidas:
            if len(args) != 2:
                raise ValueError(f"La operación {nombre_func} requiere exactamente 2 argumentos")
            resultado = self.evaluar_operacion(nombre_func, args[0], args[1])
            if var is not None:
                self.variables[var] = resultado
            return resultado
        
        # Si no es predefinida, buscarla en las funciones definidas
        if nombre_func not in self.functions:
            raise NameError(f"Función '{nombre_func}' no definida")
        
        funcion = self.functions[nombre_func]
        if len(args) != len(funcion['params']):
            raise TypeError(f"Número incorrecto de argumentos para {nombre_func}: esperaba {len(funcion['params'])}, recibió {len(args)}")
        
        vars_originales = self.variables.copy()
        self.variables = {}
        
        # Asignar argumentos a parámetros
        for param, arg in zip(funcion['params'], args):
            arg_valor = self.evaluar_expresion(arg)
            self.variables[param] = arg_valor
        
        # Ejecutar el cuerpo de la función
        self.return_value = None
        self.ejecutar(funcion['body'])
        resultado = self.return_value
        
        # Restaurar el contexto original
        self.variables = vars_originales
    
        # Asignar el resultado si hay una variable de asignación
        if var is not None:
            self.variables[var] = resultado
        
        return resultado

    def procesar_repetir_si(self, lineas, indice):
        """Procesa estructura repetir si (while)"""
        linea = lineas[indice]
        
        condicion = linea[linea.find("(")+1:linea.rfind(")")]
        condicion = condicion.replace(" y ", " and ").replace(" o ", " or ")
        
        inicio_bloque = indice + 1
        fin_bloque = self.encontrar_fin(lineas, inicio_bloque, 'fin repetir')
        
        while self.evaluar_expresion(condicion):
            self.indentacion += 1
            for i in range(inicio_bloque, fin_bloque):
                if lineas[i].strip() and lineas[i].strip() != 'fin repetir':
                    self.ejecutar([lineas[i]])
            self.indentacion -= 1
        
        return fin_bloque + 1 

    def procesar_hacer_hasta(self, lineas, indice):
        """Procesa estructura hacer hasta (do-while)"""
        linea = lineas[indice]
        
        # Extraer condición
        condicion = linea[linea.find("(")+1:linea.rfind(")")]
        # Reemplazar operadores lógicos
        condicion = condicion.replace(" y ", " and ").replace(" o ", " or ")
        
        inicio_bloque = indice + 1
        fin_bloque = self.encontrar_fin(lineas, inicio_bloque, 'fin hacer')
        
        while True:
            self.indentacion += 1
            for i in range(inicio_bloque, fin_bloque):
                if lineas[i].strip() and lineas[i].strip() != 'fin hacer':
                    self.ejecutar([lineas[i]])
            self.indentacion -= 1
            
            if not self.evaluar_expresion(condicion):
                break
        
        return fin_bloque + 1 

    def ejecutar_bloque(self, lineas, inicio, fin):
        """Ejecuta un bloque de código"""
        self.indentacion += 1
        for i in range(inicio, fin):
            if lineas[i].strip():  # Omitir líneas vacías
                self.ejecutar([lineas[i]])
        self.indentacion -= 1
        return fin + 1  # Devolver el índice después del fin del bloque

    def encontrar_fin(self, lineas, inicio, marcador):
        """Encuentra el fin de un bloque"""
        nivel = 1  # Para manejar anidamiento
        
        for i in range(inicio, len(lineas)):
            linea = lineas[i].strip()
            
            # Detectar inicio de un nuevo bloque del mismo tipo
            if ("si (" in linea and marcador == "fin si") or \
               ("repetir si (" in linea and marcador == "fin repetir") or \
               ("hacer hasta (" in linea and marcador == "fin hacer") or \
               ("definir " in linea and marcador == "fin definir"):
                nivel += 1
            
            # Detectar fin de bloque
            elif linea == marcador:
                nivel -= 1
                if nivel == 0:
                    return i
        
        # Si no se encuentra el marcador, devolver el final del código
        return len(lineas) - 1