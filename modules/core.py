from lark import Lark, Transformer, v_args
import re

# Definición de la gramática para nuestro lenguaje pseudocódigo
grammar = r"""
    programa: "Inicio" "(" NOMBRE ")" bloque "Fin"
    
    bloque: instruccion*
    
    instruccion: declaracion
               | mostrar
               | leer
               | asignacion
               | condicional
               | bucle_while
               | bucle_do_while
               | definicion_funcion
               | retorno
    
    declaracion: "declarar" NOMBRE "tipo:" tipo
    tipo: "entero" | "real" | "texto" | "booleano"
    
    mostrar: "mostrar" "(" expresion_mostrar ")"
    expresion_mostrar: valor (":" valor)*
    
    leer: "leer" "(" NOMBRE ")"
    
    asignacion: NOMBRE "=" expresion
    
    condicional: "si" "(" condicion ")" "ejecutar" ":" bloque_indentado ["si" "no" ":" bloque_indentado]
    
    bucle_while: "repetir" "si" "(" condicion ")" "ejecutar" ":" bloque_indentado
    
    bucle_do_while: "hacer" "hasta" "(" condicion ")" ":" bloque_indentado
    
    definicion_funcion: "definir" NOMBRE "(" parametros ")" ":" bloque_indentado
    parametros: [NOMBRE ("," NOMBRE)*]
    
    retorno: "retornar" expresion
    
    bloque_indentado: instruccion+
    
    condicion: expresion comparador expresion
    comparador: ">" | "<" | ">=" | "<=" | "==" | "!="
    
    expresion: valor
             | expresion "+" expresion -> suma
             | expresion "-" expresion -> resta
             | expresion "*" expresion -> multiplicacion
             | expresion "/" expresion -> division
    
    valor: NUMERO
         | STRING
         | NOMBRE
         | llamada_funcion
    
    llamada_funcion: NOMBRE "(" [expresion ("," expresion)*] ")"
    
    NOMBRE: /[a-zA-Z_][a-zA-Z0-9_]*/
    NUMERO: /[0-9]+(\.[0-9]+)?/
    STRING: /"[^"\\]*(\\.[^"\\]*)*"/
    
    %import common.WS
    %ignore WS
"""

class TraductorJS(Transformer):
    def __init__(self):
        super().__init__()
        self.variables = set()
        self.funciones = set()
        self.js_code = []
        self.indentacion = 0
        
    def agregar_linea(self, linea):
        """Agrega una línea de código JavaScript con la indentación correcta"""
        self.js_code.append("  " * self.indentacion + linea)
    
    def programa(self, items):
        nombre_programa = items[0]  # Nombre del algoritmo
        bloque = items[1]  # Código del bloque principal
        return "\n".join(self.js_code)
    
    def bloque(self, items):
        # Las instrucciones ya han sido procesadas y añadidas a js_code
        return None
    
    def instruccion(self, items):
        # La instrucción específica ya ha sido procesada
        return None
    
    def declaracion(self, items):
        nombre_var = items[0]
        tipo = items[1]
        self.variables.add(nombre_var)
        self.agregar_linea(f"let {nombre_var};")
    
    def tipo(self, items):
        return items[0]
    
    def mostrar(self, items):
        expr_mostrar = items[0]
        if isinstance(expr_mostrar, list):
            # Concatenación con ":"
            expresiones_js = []
            for expr in expr_mostrar:
                if isinstance(expr, str) and expr.startswith('"') and expr.endswith('"'):
                    # Es una cadena de texto
                    expr = expr.replace("\\line", "\\n")
                expresiones_js.append(str(expr))
            self.agregar_linea(f"console.log({' + '.join(expresiones_js)});")
        else:
            # Solo un valor
            if isinstance(expr_mostrar, str) and expr_mostrar.startswith('"') and expr_mostrar.endswith('"'):
                expr_mostrar = expr_mostrar.replace("\\line", "\\n")
            self.agregar_linea(f"console.log({expr_mostrar});")
    
    def expresion_mostrar(self, items):
        if len(items) == 1:
            return items[0]
        else:
            return items
    
    def leer(self, items):
        nombre_var = items[0]
        self.agregar_linea(f"{nombre_var} = prompt('Ingrese {nombre_var}');")
        # Convertir a número si es necesario (asumimos que las variables con entrada son numéricas)
        self.agregar_linea(f"{nombre_var} = Number({nombre_var});")
    
    def asignacion(self, items):
        nombre_var = items[0]
        valor = items[1]
        self.agregar_linea(f"{nombre_var} = {valor};")
    
    def condicional(self, items):
        condicion = items[0]
        bloque_si = ""  # Este ya se procesó y añadió a js_code
        
        self.agregar_linea(f"if ({condicion}) {{")
        self.indentacion += 1
        
        # El bloque "si" ya se procesó en bloque_indentado
        
        self.indentacion -= 1
        
        if len(items) > 1:  # Hay un bloque "si no"
            self.agregar_linea("} else {")
            self.indentacion += 1
            
            # El bloque "si no" ya se procesó en bloque_indentado
            
            self.indentacion -= 1
        
        self.agregar_linea("}")
    
    def bucle_while(self, items):
        condicion = items[0]
        
        self.agregar_linea(f"while ({condicion}) {{")
        self.indentacion += 1
        
        # El bloque del bucle ya se procesó en bloque_indentado
        
        self.indentacion -= 1
        self.agregar_linea("}")
    
    def bucle_do_while(self, items):
        condicion = items[0]
        
        self.agregar_linea(f"do {{")
        self.indentacion += 1
        
        # El bloque del bucle ya se procesó en bloque_indentado
        
        self.indentacion -= 1
        self.agregar_linea(f"}} while ({condicion});")
    
    def definicion_funcion(self, items):
        nombre_func = items[0]
        parametros = items[1]
        self.funciones.add(nombre_func)
        
        self.agregar_linea(f"function {nombre_func}({parametros}) {{")
        self.indentacion += 1
        
        # El bloque de la función ya se procesó en bloque_indentado
        
        self.indentacion -= 1
        self.agregar_linea("}")
    
    def parametros(self, items):
        return ", ".join(items) if items else ""
    
    def retorno(self, items):
        valor = items[0]
        self.agregar_linea(f"return {valor};")
    
    def bloque_indentado(self, items):
        # Las instrucciones ya han sido procesadas
        return None
    
    def condicion(self, items):
        expr1 = items[0]
        comparador = items[1]
        expr2 = items[2]
        return f"{expr1} {comparador} {expr2}"
    
    def comparador(self, items):
        return items[0]
    
    def expresion(self, items):
        return items[0]
    
    def suma(self, items):
        return f"{items[0]} + {items[1]}"
    
    def resta(self, items):
        return f"{items[0]} - {items[1]}"
    
    def multiplicacion(self, items):
        return f"{items[0]} * {items[1]}"
    
    def division(self, items):
        return f"{items[0]} / {items[1]}"
    
    def valor(self, items):
        return items[0]
    
    def llamada_funcion(self, items):
        nombre_func = items[0]
        argumentos = items[1:] if len(items) > 1 else []
        return f"{nombre_func}({', '.join(map(str, argumentos))})"
    
    def NOMBRE(self, token):
        return token.value
    
    def NUMERO(self, token):
        return token.value
    
    def STRING(self, token):
        return token.value


class TraductorPseudocodigoJS:
    def __init__(self):
        self.parser = Lark(grammar, start='programa', parser='lalr', transformer=TraductorJS())
    
    def traducir(self, codigo_fuente):
        # Preprocesamiento para manejar la indentación
        codigo_preprocesado = self.preprocesar_codigo(codigo_fuente)
        
        try:
            resultado = self.parser.parse(codigo_preprocesado)
            return resultado
        except Exception as e:
            return f"Error al analizar el código: {str(e)}"
    
    def preprocesar_codigo(self, codigo):
        """
        Preprocesa el código para manejar la indentación y facilitar el análisis
        """
        lineas = codigo.strip().split('\n')
        resultado = []
        
        for linea in lineas:
            linea = linea.strip()
            if not linea:
                continue
                
            resultado.append(linea)
        
        return '\n'.join(resultado)


# Función para manejar la traducción
def traducir_codigo(codigo_fuente):
    traductor = TraductorPseudocodigoJS()
    return traductor.traducir(codigo_fuente)


# Ejemplo de uso
if __name__ == "__main__":
    # Código de ejemplo
    codigo_ejemplo = """Inicio (MiAlgoritmo)
declarar edad tipo: entero
mostrar("Ingresa tu edad")
leer(edad)
mostrar("Hola")
mostrar(edad)
si (edad > 18) ejecutar:
mostrar("Eres mayor de edad")
si no:
mostrar("Eres menor de edad")
declarar numero tipo: entero
numero = 1
repetir si (numero <= 10) ejecutar:
mostrar(numero)
numero = numero + 1
hacer hasta (numero <= 20):
mostrar(numero)
numero = numero + 1
definir suma(num1,num2):
declarar resultado tipo: entero
resultado = num1 + num2
retornar resultado
declarar num1 tipo: entero
declarar num2 tipo: entero
mostrar("Ingrese el primer numero: ")
leer(num1)
mostrar("Ingrese el segundo numero: ")
leer(num2)
resultado = suma(num1,num2)
mostrar("El resultado de la suma es: ": resultado : "Gracias\\line")
Fin"""
    
    # codigo_js = traducir_codigo(codigo_ejemplo)
    # print(codigo_js)

# Versión mejorada para manejar la indentación correctamente
class TraductorSAM:
    def __init__(self):
        self.variables = set()
        self.funciones = set()
    
    def traducir(self, codigo_fuente):
        # Analizar la estructura del código
        lineas = codigo_fuente.strip().split('\n')
        js_code = []
        indentacion = 0
        
        i = 0
        
        # Verificar que el código comienza con "Inicio" y termina con "Fin"
        if not lineas[0].startswith("Inicio") or lineas[-1] != "Fin":
            return "Error: El código debe comenzar con 'Inicio' y terminar con 'Fin'"
        
        # Extraer nombre del programa y agregar comentario
        nombre_programa = lineas[0][lineas[0].find("(")+1:lineas[0].find(")")]
        js_code.append(f"// Programa: {nombre_programa}")
        js_code.append("")
        
        # Saltar la línea de Inicio
        i += 1
        
        while i < len(lineas) - 1:  # -1 para no procesar "Fin"
            linea = lineas[i].strip()
            
            if not linea:
                i += 1
                continue
            
            # Declaración de variables
            if linea.startswith("declarar "):
                partes = linea.replace("declarar ", "").split(" tipo: ")
                nombre_var = partes[0].strip()
                self.variables.add(nombre_var)
                js_code.append("  " * indentacion + f"let {nombre_var};")
            
            # Mostrar en pantalla
            elif linea.startswith("mostrar("):
                contenido = linea[linea.find("(")+1:linea.rfind(")")]
                
                if ":" in contenido:
                    # Concatenación con ":"
                    partes = contenido.split(":")
                    partes_js = []
                    for parte in partes:
                        parte = parte.strip()
                        if parte.startswith('"') and parte.endswith('"'):
                            # Es una cadena de texto
                            parte = parte.replace("\\line", "\\n")
                        partes_js.append(parte)
                    
                    js_code.append("  " * indentacion + f"console.log({' + '.join(partes_js)});")
                else:
                    # Solo un valor
                    if contenido.startswith('"') and contenido.endswith('"'):
                        contenido = contenido.replace("\\line", "\\n")
                    js_code.append("  " * indentacion + f"console.log({contenido});")
            
            # Leer entrada
            elif linea.startswith("leer("):
                var_nombre = linea[linea.find("(")+1:linea.rfind(")")]
                js_code.append("  " * indentacion + f"let {var_nombre} = prompt('Ingrese {var_nombre}');")
                js_code.append("  " * indentacion + f"{var_nombre} = Number({var_nombre});")
            
            # Asignación
            elif "=" in linea and not linea.startswith("si ") and not linea.startswith("hacer "):
                partes = linea.split("=", 1)  # Split solo la primera ocurrencia
                nombre_var = partes[0].strip()
                valor = partes[1].strip()
                js_code.append("  " * indentacion + f"{nombre_var} = {valor};")
            
            # Estructura condicional
            elif linea.startswith("si "):
                condicion = linea[linea.find("(")+1:linea.find(")")]
                js_code.append("  " * indentacion + f"if ({condicion}) {{")
                indentacion += 1
                i += 1  # Saltar la línea "ejecutar:"
                
                # Procesar bloque if
                tiene_else = False
                while i < len(lineas) - 1:
                    linea_bloque = lineas[i].strip()
                    
                    if linea_bloque.startswith("si no:"):
                        indentacion -= 1
                        js_code.append("  " * indentacion + "} else {")
                        indentacion += 1
                        tiene_else = True
                        break
                    elif (linea_bloque.startswith("si ") and not linea_bloque.startswith("si no:")) or \
                         linea_bloque.startswith("repetir ") or linea_bloque.startswith("hacer ") or \
                         linea_bloque.startswith("definir ") or \
                         linea_bloque.startswith("declarar ") or linea_bloque == "Fin":
                        indentacion -= 1
                        js_code.append("  " * indentacion + "}")
                        i -= 1  # Retroceder para procesar esta línea en la siguiente iteración
                        break
                    
                    i += 1
                
                # Cerrar el bloque if si llegamos al final y no hay un else
                if i == len(lineas) - 1 and not tiene_else:
                    indentacion -= 1
                    js_code.append("  " * indentacion + "}")
            
            # Continuar con el bloque "si no"
            elif linea.startswith("si no:"):
                # Ya procesado en el bloque "si", pero necesitamos avanzar para procesar el contenido
                i += 1
                
                # Procesar contenido del else
                while i < len(lineas) - 1:
                    linea_bloque = lineas[i].strip()
                    
                    if (linea_bloque.startswith("si ") and not linea_bloque.startswith("si no:")) or \
                       linea_bloque.startswith("repetir ") or linea_bloque.startswith("hacer ") or \
                       linea_bloque.startswith("definir ") or \
                       linea_bloque.startswith("declarar ") or linea_bloque == "Fin":
                        indentacion -= 1
                        js_code.append("  " * indentacion + "}")
                        i -= 1  # Retroceder para procesar esta línea en la siguiente iteración
                        break
                    
                    i += 1
                
                # Cerrar el bloque else si llegamos al final
                if i == len(lineas) - 1:
                    indentacion -= 1
                    js_code.append("  " * indentacion + "}")
            
            # Bucle while
            elif linea.startswith("repetir si "):
                condicion = linea[linea.find("(")+1:linea.find(")")]
                js_code.append("  " * indentacion + f"while ({condicion}) {{")
                indentacion += 1
                i += 1  # Saltar la línea "ejecutar:"
                
                # Procesar bloque while
                while i < len(lineas) - 1:
                    linea_bloque = lineas[i].strip()
                    
                    if (linea_bloque.startswith("si ") and not linea_bloque.startswith("si no:")) or \
                       linea_bloque.startswith("repetir ") or linea_bloque.startswith("hacer ") or \
                       linea_bloque.startswith("definir ") or \
                       linea_bloque.startswith("declarar ") or linea_bloque == "Fin":
                        indentacion -= 1
                        js_code.append("  " * indentacion + "}")
                        i -= 1  # Retroceder para procesar esta línea en la siguiente iteración
                        break
                    
                    i += 1
                
                # Cerrar el bloque while si llegamos al final
                if i == len(lineas) - 1:
                    indentacion -= 1
                    js_code.append("  " * indentacion + "}")
            
            # Bucle do-while
            elif linea.startswith("hacer hasta"):
                condicion = linea[linea.find("(")+1:linea.find(")")]
                js_code.append("  " * indentacion + "do {")
                indentacion += 1
                i += 1  # Saltar la línea ":"
                
                # Procesar bloque do-while
                while i < len(lineas) - 1:
                    linea_bloque = lineas[i].strip()
                    
                    if (linea_bloque.startswith("si ") and not linea_bloque.startswith("si no:")) or \
                       linea_bloque.startswith("repetir ") or linea_bloque.startswith("hacer ") or \
                       linea_bloque.startswith("definir ") or \
                       linea_bloque.startswith("declarar ") or linea_bloque == "Fin":
                        indentacion -= 1
                        js_code.append("  " * indentacion + f"}} while ({condicion});")
                        i -= 1  # Retroceder para procesar esta línea en la siguiente iteración
                        break
                    
                    i += 1
                
                # Cerrar el bloque do-while si llegamos al final
                if i == len(lineas) - 1:
                    indentacion -= 1
                    js_code.append("  " * indentacion + f"}} while ({condicion});")
            
            # Definición de función
            elif linea.startswith("definir "):
                nombre_func = linea[linea.find(" ")+1:linea.find("(")]
                params = linea[linea.find("(")+1:linea.find(")")]
                self.funciones.add(nombre_func)
                
                js_code.append("  " * indentacion + f"function {nombre_func}({params}) {{")
                indentacion += 1
                i += 1  # Saltar la línea ":"
                
                # Procesar cuerpo de la función
                while i < len(lineas) - 1:
                    linea_bloque = lineas[i].strip()
                    
                    if (linea_bloque.startswith("si ") and not linea_bloque.startswith("si no:")) or \
                       linea_bloque.startswith("repetir ") or linea_bloque.startswith("hacer ") or \
                       linea_bloque.startswith("definir ") or \
                       (linea_bloque.startswith("declarar ") and i > 0 and not lineas[i-1].strip().endswith(":")) or \
                       linea_bloque == "Fin":
                        indentacion -= 1
                        js_code.append("  " * indentacion + "}")
                        i -= 1  # Retroceder para procesar esta línea en la siguiente iteración
                        break
                    
                    i += 1
                
                # Cerrar el bloque de función si llegamos al final
                if i == len(lineas) - 1:
                    indentacion -= 1
                    js_code.append("  " * indentacion + "}")
            
            # Retorno de función
            elif linea.startswith("retornar "):
                valor_retorno = linea.replace("retornar ", "").strip()
                js_code.append("  " * indentacion + f"return {valor_retorno};")
            
            else:
                # Línea no reconocida
                js_code.append("  " * indentacion + f"// No traducido: {linea}")
            
            i += 1
        
        return "\n".join(js_code)


# Versión final mejorada
def main():
    # Código de ejemplo
    codigo_ejemplo = """Inicio (MiAlgoritmo)
declarar edad tipo: entero
mostrar("Ingresa tu edad")
leer(edad)
mostrar("Hola")
mostrar(edad)
si (edad > 18) ejecutar:
mostrar("Eres mayor de edad")
si no:
mostrar("Eres menor de edad")
declarar numero tipo: entero
numero = 1
repetir si (numero <= 10) ejecutar:
mostrar(numero)
numero = numero + 1
hacer hasta (numero <= 20):
mostrar(numero)
numero = numero + 1
definir suma(num1,num2):
declarar resultado tipo: entero
resultado = num1 + num2
retornar resultado
declarar num1 tipo: entero
declarar num2 tipo: entero
mostrar("Ingrese el primer numero: ")
leer(num1)
mostrar("Ingrese el segundo numero: ")
leer(num2)
resultado = suma(num1,num2)
mostrar("El resultado de la suma es: ": resultado : "Gracias\\line")
Fin"""
    
    traductor = TraductorSAM()
    codigo_js = traductor.traducir(codigo_ejemplo)
    print(codigo_js)

if __name__ == "__main__":
    main()