import js2py

class JavaScriptExecutor:
    def __init__(self):
        # Crear un contexto de ejecución persistente (opcional)
        self.contexto = js2py.EvalJs()

    def ejecutar_codigo(self, codigo_js):
        """
        Ejecuta una cadena de código JavaScript y retorna el resultado.
        
        :param codigo_js: str - Código JavaScript a ejecutar.
        :return: Resultado de la ejecución o mensaje de error.
        """
        try:
            resultado = self.contexto.eval(codigo_js)
            return resultado
        except Exception as e:
            return f"Error al ejecutar JavaScript: {e}"

# Ejemplo de uso
if __name__ == "__main__":
    ejecutor = JavaScriptExecutor()
    
    codigo_js = """
    function saludar(nombre) {
        return "Hola, " + nombre + "!";
    }
    saludar("Mundo");
    """

    resultado = ejecutor.ejecutar_codigo(codigo_js)
    print("Resultado:", resultado)

    