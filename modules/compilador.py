import re
import sys
import traceback

class CompiladorError(Exception):
    """Clase personalizada para errores del compilador"""
    def __init__(self, mensaje, linea=None):
        self.mensaje = mensaje
        self.linea = linea
        super().__init__(self.mensaje)

class Compilador:
    def __init__(self):
        self.variables = {}
        self.variables_tipo = {}  
        self.functions = {}
        self.indentacion = 0
        self.return_value = None
        self.operaciones_predefinidas = ['suma', 'resta', 'multiplicar', 'dividir']
        self.tipo_esperado = {
            'entero': int,
            'decimal': float,
            'cadena': str,
            'booleano': bool
        }

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
        tipo_esperado = self.variables_tipo.get(variable)
        valor = input(f'  ' * self.indentacion)
        try:
            valor_parseado = self.parse_valor(valor)
            if tipo_esperado and not self.validar_tipo(valor_parseado, tipo_esperado):
                tipo_actual = type(valor_parseado).__name__
                raise CompiladorError(f"Error de tipo: Se esperaba {tipo_esperado} pero se ingresó {tipo_actual} ({valor})")
                
            self.variables[variable] = valor_parseado
        except Exception as e:
            raise CompiladorError(f"Error al leer variable '{variable}': {str(e)}")

    def validar_tipo(self, valor, tipo_esperado):
        """Valida que un valor coincida con el tipo esperado"""
        if tipo_esperado == 'entero':
            return isinstance(valor, int)
        elif tipo_esperado == 'decimal':
            return isinstance(valor, (int, float))
        elif tipo_esperado == 'cadena':
            return isinstance(valor, str)
        elif tipo_esperado == 'booleano':
            return isinstance(valor, bool)
        return True 

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

    def evaluar_operacion(self, operacion, op1, op2, linea_num=None):
        """Evalúa operaciones aritméticas básicas"""
        try:
            # Evaluar los operandos
            op1_val = self.evaluar_expresion(op1)
            op2_val = self.evaluar_expresion(op2)
            
            # Convertir a números si es posible
            try:
                op1_val = float(op1_val) if isinstance(op1_val, str) and op1_val.replace('.', '', 1).isdigit() else op1_val
                op2_val = float(op2_val) if isinstance(op2_val, str) and op2_val.replace('.', '', 1).isdigit() else op2_val
            except:
                pass
            
            # Validar que ambos operandos sean valores numéricos
            if operacion in ['suma', 'resta', 'multiplicar', 'dividir']:
                if not isinstance(op1_val, (int, float)):
                    raise CompiladorError(f"El primer operando debe ser numérico para la operación {operacion}, pero es {type(op1_val).__name__}", linea_num)
                if not isinstance(op2_val, (int, float)):
                    raise CompiladorError(f"El segundo operando debe ser numérico para la operación {operacion}, pero es {type(op2_val).__name__}", linea_num)
            
            # Realizar la operación
            if operacion == 'suma':
                return op1_val + op2_val
            elif operacion == 'resta':
                return op1_val - op2_val
            elif operacion == 'multiplicar':
                return op1_val * op2_val
            elif operacion == 'dividir':
                if op2_val == 0:
                    raise CompiladorError("División por cero no permitida", linea_num)
                return op1_val / op2_val
            else:
                raise CompiladorError(f"Operación no reconocida: {operacion}", linea_num)
        except CompiladorError as e:
            raise e
        except Exception as e:
            raise CompiladorError(f"Error en la operación {operacion}: {str(e)}", linea_num)

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
                    self.procesar_mostrar(linea, i+1)
                elif linea.startswith('leer('):
                    self.procesar_leer(linea, i+1)
                elif linea.startswith('declarar'):
                    self.procesar_declaracion(linea, i+1)
                elif linea.startswith('si ('):
                    i = self.procesar_condicional(lineas, i)
                    continue
                elif linea == 'si no:':
                    # Este caso se maneja dentro de procesar_condicional
                    pass
                elif linea.startswith('repetir si ('): 
                    i = self.procesar_repetir_si(lineas, i)
                    continue
                elif linea.startswith('definir '):
                    i = self.procesar_definir_funcion(lineas, i)
                    continue
                elif linea.startswith('retornar '):
                    self.procesar_retorno(linea, i+1)
                elif linea in ["fin si", "fin repetir", "fin hacer", "fin definir"]:
                    # Final de un bloque, se maneja en otras funciones
                    pass
                elif any(op in linea for op in [f'{op}(' for op in self.operaciones_predefinidas]):
                    self.procesar_operacion_aritmetica(linea, i+1)
                elif '=' in linea and not any(op in linea for op in ['==', '!=', '<=', '>=']):
                    self.procesar_asignacion(linea, i+1)
                elif '(' in linea and ')' in linea:
                    if not any(linea.startswith(kw) for kw in ['mostrar', 'leer', 'si', 'repetir', 'hacer', 'definir']):
                        self.procesar_llamada_funcion(linea, i+1)
                else:
                    raise CompiladorError(f"Sintaxis no reconocida: '{linea}'", i+1)
                i += 1
            except CompiladorError as e:
                if e.linea:
                    print(f"\n❌ Error en línea {e.linea}: {e.mensaje}")
                else:
                    print(f"\n❌ Error en línea {i+1}: {e.mensaje}")
                print(f"   Código: '{linea}'")
                return False
            except Exception as e:
                print(f"\n❌ Error inesperado en línea {i+1}: {str(e)}")
                print(f"   Código: '{linea}'")
                print(f"   Tipo de error: {type(e).__name__}")
                tb = traceback.extract_tb(sys.exc_info()[2])
                print(f"   En el archivo: {tb[-1].filename}, línea {tb[-1].lineno}")
                return False
        return True

    def procesar_operacion_aritmetica(self, linea, linea_num):
        """Procesa operaciones aritméticas como suma(a,b)"""
        try:
            if '=' in linea:
                var, resto = linea.split('=', 1)
                var = var.strip()
                match = re.search(r'(\w+)\((.*?),(.*?)\)', resto.strip())
            else:
                var = None
                match = re.search(r'(\w+)\((.*?),(.*?)\)', linea)
            
            if not match:
                raise CompiladorError("Sintaxis incorrecta en operación aritmética", linea_num)
            
            operacion = match.group(1)
            op1 = match.group(2).strip()
            op2 = match.group(3).strip()
            
            # Evaluar la operación
            resultado = self.evaluar_operacion(operacion, op1, op2, linea_num)
            
            if var is not None:
                # Verificar el tipo si la variable ya tiene un tipo declarado
                if var in self.variables_tipo:
                    tipo_esperado = self.variables_tipo[var]
                    if not self.validar_tipo(resultado, tipo_esperado):
                        tipo_actual = type(resultado).__name__
                        raise CompiladorError(f"Error de tipo: La variable '{var}' es de tipo {tipo_esperado}, pero el resultado es {tipo_actual}", linea_num)
                self.variables[var] = resultado
            return resultado
        except CompiladorError as e:
            raise e
        except Exception as e:
            raise CompiladorError(f"Error al procesar operación aritmética: {str(e)}", linea_num)

    def procesar_mostrar(self, linea, linea_num):
        """Procesa la instrucción mostrar()"""
        try:
            match = re.search(r'mostrar\((.*)\)', linea)
            if not match:
                raise CompiladorError("Sintaxis incorrecta en mostrar()", linea_num)
            contenido = match.group(1)
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
                        if parte not in self.variables:
                            raise CompiladorError(f"Variable '{parte}' no declarada", linea_num)
                        mensajes.append(self.variables[parte])
                    else:
                        mensajes.append(parte.replace('"', '').replace("'", ""))
                self.mostrar(*mensajes)
        except CompiladorError as e:
            raise e
        except Exception as e:
            raise CompiladorError(f"Error al procesar mostrar(): {str(e)}", linea_num)

    def procesar_leer(self, linea, linea_num):
        """Procesa la instrucción leer()"""
        try:
            match = re.search(r'leer\((.*)\)', linea)
            if not match:
                raise CompiladorError("Sintaxis incorrecta en leer()", linea_num)
            var = match.group(1).strip()
            if var not in self.variables:
                raise CompiladorError(f"Variable '{var}' no declarada", linea_num)
            self.leer(var)
        except CompiladorError as e:
            raise e
        except Exception as e:
            raise CompiladorError(f"Error al procesar leer(): {str(e)}", linea_num)

    def procesar_declaracion(self, linea, linea_num):
        """Procesa declaración de variables"""
        try:
            match = re.search(r'declarar\s+(\w+)\s+tipo:\s+(\w+)', linea)
            if match:
                nombre = match.group(1)
                tipo = match.group(2)
                
                if tipo not in self.tipo_esperado:
                    tipos_validos = ", ".join(self.tipo_esperado.keys())
                    raise CompiladorError(f"Tipo de dato '{tipo}' no válido. Tipos válidos: {tipos_validos}", linea_num)
                    
                self.variables[nombre] = None
                self.variables_tipo[nombre] = tipo
            else:
                partes = linea.split()
                if len(partes) < 2:
                    raise CompiladorError("Declaración de variable incorrecta", linea_num)
                    
                nombre = partes[1]
                self.variables[nombre] = None
        except CompiladorError as e:
            raise e
        except Exception as e:
            raise CompiladorError(f"Error al declarar variable: {str(e)}", linea_num)

    def procesar_condicional(self, lineas, indice):
        """Procesa estructura condicional if."""
        linea_num = indice + 1
        try:
            linea = lineas[indice].strip()
            
            # Verificar sintaxis
            match = re.search(r'si\s*\((.*)\)\s*ejecutar\s*:', linea)
            if not match:
                raise CompiladorError("Sintaxis incorrecta en condicional si", linea_num)
                
            # Extraer condición
            condicion = linea[linea.find("(")+1:linea.rfind(")")]
            # Reemplazar operadores lógicos
            condicion = condicion.replace(" y ", " and ").replace(" o ", " or ")
            
            try:
                resultado = self.evaluar_expresion(condicion)
            except Exception as e:
                raise CompiladorError(f"Error al evaluar condición: {str(e)}", linea_num)
                
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
            
            if not fin_si_encontrado:
                raise CompiladorError("Bloque 'si' sin 'fin si' correspondiente", linea_num)
                
            return siguiente_indice
        except CompiladorError as e:
            raise e
        except Exception as e:
            raise CompiladorError(f"Error en estructura condicional: {str(e)}", linea_num)

    def procesar_asignacion(self, linea, linea_num):
        """Procesa asignación de variables"""
        try:
            var, expr = linea.split('=', 1)
            var = var.strip()
            expr = expr.strip()
            
            if var not in self.variables:
                raise CompiladorError(f"Variable '{var}' no declarada", linea_num)
                
            # Reemplazar operadores lógicos si existen
            expr = expr.replace(" y ", " and ").replace(" o ", " or ")
            
            try:
                valor = self.evaluar_expresion(expr)
            except Exception as e:
                raise CompiladorError(f"Error al evaluar expresión: {str(e)}", linea_num)
                
            # Verificar tipo si la variable ya tiene un tipo declarado
            if var in self.variables_tipo:
                tipo_esperado = self.variables_tipo[var]
                if not self.validar_tipo(valor, tipo_esperado):
                    tipo_actual = type(valor).__name__
                    raise CompiladorError(f"Error de tipo: La variable '{var}' es de tipo {tipo_esperado}, pero se asignó {tipo_actual}", linea_num)
                    
            self.variables[var] = valor
        except CompiladorError as e:
            raise e
        except Exception as e:
            raise CompiladorError(f"Error en asignación: {str(e)}", linea_num)

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

    def procesar_llamada_funcion(self, linea, linea_num):
        """Procesa llamada a función"""
        try:
            if '=' in linea:
                var, resto = linea.split('=', 1)
                var = var.strip()
                linea_func = resto.strip()
                
                if var not in self.variables:
                    raise CompiladorError(f"Variable '{var}' no declarada", linea_num)
            else:
                var = None
                linea_func = linea.strip()
                
            match = re.search(r'(\w+)\((.*)\)', linea_func)
            if not match:
                raise CompiladorError(f"Sintaxis incorrecta en llamada a función: {linea}", linea_num)
                
            nombre_func = match.group(1)
            args_str = match.group(2)
            
            args = []
            arg_start = 0
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
                    raise CompiladorError(f"La operación {nombre_func} requiere exactamente 2 argumentos", linea_num)
                resultado = self.evaluar_operacion(nombre_func, args[0], args[1], linea_num)
                if var is not None:
                    # Verificar tipo si la variable ya tiene un tipo declarado
                    if var in self.variables_tipo:
                        tipo_esperado = self.variables_tipo[var]
                        if not self.validar_tipo(resultado, tipo_esperado):
                            tipo_actual = type(resultado).__name__
                            raise CompiladorError(f"Error de tipo: La variable '{var}' es de tipo {tipo_esperado}, pero el resultado es {tipo_actual}", linea_num)
                    self.variables[var] = resultado
                return resultado
            
            # Si no es predefinida, buscarla en las funciones definidas
            if nombre_func not in self.functions:
                raise CompiladorError(f"Función '{nombre_func}' no definida", linea_num)
            
            funcion = self.functions[nombre_func]
            if len(args) != len(funcion['params']):
                raise CompiladorError(f"Número incorrecto de argumentos para {nombre_func}: esperaba {len(funcion['params'])}, recibió {len(args)}", linea_num)
            
            vars_originales = self.variables.copy()
            tipos_originales = self.variables_tipo.copy()
            self.variables = {}
            self.variables_tipo = {}
            
            # Asignar argumentos a parámetros
            for param, arg in zip(funcion['params'], args):
                try:
                    arg_valor = self.evaluar_expresion(arg)
                except Exception as e:
                    raise CompiladorError(f"Error al evaluar argumento '{arg}': {str(e)}", linea_num)
                self.variables[param] = arg_valor
            
            # Ejecutar el cuerpo de la función
            self.return_value = None
            self.ejecutar(funcion['body'])
            resultado = self.return_value
            
            # Restaurar el contexto original
            self.variables = vars_originales
            self.variables_tipo = tipos_originales
        
            # Asignar el resultado si hay una variable de asignación
            if var is not None:
                # Verificar tipo si la variable ya tiene un tipo declarado
                if var in self.variables_tipo:
                    tipo_esperado = self.variables_tipo[var]
                    if not self.validar_tipo(resultado, tipo_esperado):
                        tipo_actual = type(resultado).__name__
                        raise CompiladorError(f"Error de tipo: La variable '{var}' es de tipo {tipo_esperado}, pero el resultado es {tipo_actual}", linea_num)
                self.variables[var] = resultado
            
            return resultado
        except CompiladorError as e:
            raise e
        except Exception as e:
            raise CompiladorError(f"Error en llamada a función: {str(e)}", linea_num)

    def procesar_repetir_si(self, lineas, indice):
        """Procesa estructura repetir si (while)"""
        linea_num = indice + 1
        try:
            linea = lineas[indice]
            
            # Verificar sintaxis
            match = re.search(r'repetir\s+si\s*\((.*)\)\s*ejecutar\s*:', linea)
            if not match:
                raise CompiladorError("Sintaxis incorrecta en bucle repetir si", linea_num)
                
            condicion = linea[linea.find("(")+1:linea.rfind(")")]
            condicion = condicion.replace(" y ", " and ").replace(" o ", " or ")
            
            inicio_bloque = indice + 1
            try:
                fin_bloque = self.encontrar_fin(lineas, inicio_bloque, 'fin repetir')
            except Exception as e:
                raise CompiladorError(f"Bloque 'repetir si' sin 'fin repetir' correspondiente", linea_num)
            
            iteraciones = 0
            max_iteraciones = 10000  # Limitar número de iteraciones para evitar bucles infinitos
            
            while True:
                try:
                    resultado_condicion = self.evaluar_expresion(condicion)
                except Exception as e:
                    raise CompiladorError(f"Error al evaluar condición del bucle: {str(e)}", linea_num)
                    
                if not resultado_condicion:
                    break
                    
                iteraciones += 1
                if iteraciones > max_iteraciones:
                    raise CompiladorError(f"Posible bucle infinito detectado (más de {max_iteraciones} iteraciones)", linea_num)
                    
                self.indentacion += 1
                for i in range(inicio_bloque, fin_bloque):
                    if lineas[i].strip() and lineas[i].strip() != 'fin repetir':
                        self.ejecutar([lineas[i]])
                self.indentacion -= 1
            
            return fin_bloque + 1
        except CompiladorError as e:
            raise e
        except Exception as e:
            raise CompiladorError(f"Error en bucle repetir si: {str(e)}", linea_num)

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
        
        # Si no se encuentra el marcador, lanzar error
        raise CompiladorError(f"No se encontró el marcador '{marcador}' para cerrar el bloque")