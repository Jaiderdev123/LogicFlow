# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ejecucionvGemiQ.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLineEdit, QMainWindow,
    QPushButton, QScrollBar, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget, QTextEdit)
import sys
import iconos_rc
from compilador import Compilador
import threading
from io import StringIO

# Clase para redirigir la salida estándar
class OutputRedirector(StringIO):
    def __init__(self, text_widget):
        super().__init__()
        self.text_widget = text_widget
        self.old_stdout = sys.stdout
        
    def write(self, text):
        if text.strip():
            self.text_widget.append(f'<span style="color: blue;">{text}</span>')
        return self.old_stdout.write(text)
        
    def flush(self):
        self.old_stdout.flush()

# Compilador extendido para usar la interfaz de chat
class CompiladorChat(Compilador):
    def __init__(self, ui):
        super().__init__()
        self.ui = ui
        self.esperando_entrada = False
        self.variable_esperando = None
        
    def leer(self, variable):
        """Sobrecarga el método leer para usar la interfaz gráfica"""
        self.variable_esperando = variable
        self.esperando_entrada = True
        self.ui.mostrar_prompt(f"")
        
        # Esperar hasta que la entrada sea procesada
        while self.esperando_entrada:
            QApplication.processEvents()
            threading.Event().wait(0.1)
                
    def procesar_entrada(self, texto):
        """Procesa la entrada desde la interfaz"""
        if self.esperando_entrada and self.variable_esperando:
            self.ui.mostrar_entrada(f"> {texto}")
            valor = self.parse_valor(texto)
            self.variables[self.variable_esperando] = valor
            self.esperando_entrada = False
            self.variable_esperando = None
            return True
        return False
        
    def mostrar(self, *mensajes):
        """Sobrecarga mostrar para usar la interfaz gráfica"""
        mensaje = ' '.join(str(m) for m in mensajes)
        self.ui.mostrar_salida(mensaje)

class Ui_Ejecucion(object):
    def setupUi(self, Ejecucion):
        Ui_Ejecucion.codigo = ""
        self.ejecucion_activa = False
        self.compilador = None
        
        if not Ejecucion.objectName():
            Ejecucion.setObjectName(u"Ejecucion")
        Ejecucion.resize(657, 519)
        self.centralwidget = QWidget(Ejecucion)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 701, 601))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.entrada = QLineEdit(self.frame)
        self.entrada.setObjectName(u"entrada")
        self.entrada.setGeometry(QRect(90, 450, 471, 51))
        self.entrada.setStyleSheet(u"font: 15pt \"Fira Code\";\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(570, 460, 81, 41))
        icon = QIcon()
        icon.addFile(u":/icons/icons/subir.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(30, 30))
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(90, 0, 581, 461))
        self.frame_2.setStyleSheet(u"background-color: rgb(254, 249, 242);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        
        # Reemplazamos el fondo de imagen con un QTextEdit para mostrar el chat
        self.chat_output = QTextEdit(self.frame_2)
        self.chat_output.setObjectName(u"chat_output")
        self.chat_output.setGeometry(QRect(10, 10, 560, 440))
        self.chat_output.setReadOnly(True)
        self.chat_output.setStyleSheet(u"background-color: rgb(255, 255, 255); font: 12pt \"Consolas\";")
        
        self.verticalScrollBar = QScrollBar(self.frame_2)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setGeometry(QRect(550, 0, 16, 451))
        self.verticalScrollBar.setOrientation(Qt.Vertical)
        # Conectar el scroll bar con el chat_output
        self.chat_output.setVerticalScrollBar(self.verticalScrollBar)
        
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(0, 0, 91, 501))
        self.frame_3.setStyleSheet(u"background-color: rgb(201, 233, 210);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayoutWidget = QWidget(self.frame_3)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 91, 501))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.btnCorrer = QPushButton(self.verticalLayoutWidget)
        self.btnCorrer.setObjectName(u"btnCorrer")
        self.btnCorrer.setCursor(QCursor(Qt.OpenHandCursor))
        self.btnCorrer.setStyleSheet(u"background-color: rgba(0,0,0,0);")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/boton-de-play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnCorrer.setIcon(icon1)
        self.btnCorrer.setIconSize(QSize(50, 50))

        self.verticalLayout.addWidget(self.btnCorrer)

        self.btnParar = QPushButton(self.verticalLayoutWidget)
        self.btnParar.setObjectName(u"btnParar")
        self.btnParar.setCursor(QCursor(Qt.OpenHandCursor))
        self.btnParar.setStyleSheet(u"background-color: rgba(0,0,0,0);")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/detener.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnParar.setIcon(icon2)
        self.btnParar.setIconSize(QSize(50, 50))

        self.verticalLayout.addWidget(self.btnParar)

        # self.verCodigoJS = QPushButton(self.verticalLayoutWidget)
        # self.verCodigoJS.setObjectName(u"verCodigoJS")
        # self.verCodigoJS.setCursor(QCursor(Qt.OpenHandCursor))
        # self.verCodigoJS.setStyleSheet(u"background-color: rgba(0,0,0,0);")
        # icon5 = QIcon()
        # icon5.addFile(u":/icons/icons/js.png", QSize(), QIcon.Normal, QIcon.Off)
        # self.verCodigoJS.setIcon(icon5)
        # self.verCodigoJS.setIconSize(QSize(50, 50))
        # self.verticalLayout.addWidget(self.verCodigoJS)
        Ejecucion.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Ejecucion)
        self.statusbar.setObjectName(u"statusbar")
        Ejecucion.setStatusBar(self.statusbar)
        self.retranslateUi(Ejecucion)
        QMetaObject.connectSlotsByName(Ejecucion)
        
        # Conectar señales a slots
        self.btnCorrer.clicked.connect(self.ejecutar_codigo)
        self.pushButton.clicked.connect(self.enviar_entrada)
        self.entrada.returnPressed.connect(self.enviar_entrada)
        self.btnParar.clicked.connect(self.detener_ejecucion)

    def retranslateUi(self, Ejecucion):
        Ejecucion.setWindowTitle(QCoreApplication.translate("Ejecucion", u"Ejecución", None))
        self.pushButton.setText("")
        self.btnCorrer.setText("")
        self.btnParar.setText("")
        # self.verCodigoJS.setText("")
        self.entrada.setPlaceholderText(QCoreApplication.translate("Ejecucion", u"Ingrese datos aquí...", None))

    def setCodigo(self, codigo):
        """Establece el código a ejecutar"""
        Ui_Ejecucion.codigo = codigo
        self.chat_output.clear()
        self.mostrar_sistema("Código cargado. Presione el botón Play para ejecutar.")

    def mostrar_sistema(self, mensaje):
        """Muestra un mensaje del sistema en el chat"""
        self.chat_output.append(f'<span style="color: gray;"># {mensaje}</span>')
        self.auto_scroll()
        
    def mostrar_salida(self, mensaje):
        """Muestra una salida del programa en el chat"""
        self.chat_output.append(f'<span style="color: blue;">{mensaje}</span>')
        self.auto_scroll()
        
    def mostrar_prompt(self, mensaje):
        """Muestra un mensaje de solicitud de entrada en el chat"""
        self.chat_output.append(f'<span style="color: green;">{mensaje}</span>')
        self.auto_scroll()
        
    def mostrar_entrada(self, mensaje):
        """Muestra la entrada del usuario en el chat"""
        self.chat_output.append(f'<span style="color: purple;">{mensaje}</span>')
        self.auto_scroll()
    
    def auto_scroll(self):
        """Desplaza automáticamente al final del chat"""
        self.chat_output.verticalScrollBar().setValue(
            self.chat_output.verticalScrollBar().maximum()
        )

    def ejecutar_codigo(self):
        """Inicia la ejecución del código"""
        if not self.ejecucion_activa and Ui_Ejecucion.codigo:
            self.ejecucion_activa = True
            self.chat_output.clear()
            self.mostrar_sistema("Iniciando ejecución...")
            
            # Crear el compilador para chat
            self.compilador = CompiladorChat(self)
            
            # Redirigir stdout a nuestro widget
            self.stdout_redirector = OutputRedirector(self.chat_output)
            sys.stdout = self.stdout_redirector
            
            # Crear un hilo para ejecutar el código sin bloquear la interfaz
            self.thread = threading.Thread(target=self.ejecutar_en_hilo)
            self.thread.daemon = True
            self.thread.start()
            
    def ejecutar_en_hilo(self):
        """Ejecuta el código en un hilo separado"""
        try:
            self.compilador.ejecutar(Ui_Ejecucion.codigo)
            # Si no está esperando entrada, finalizar
            if not self.compilador.esperando_entrada:
                self.finalizar_ejecucion()
        except Exception as e:
            self.mostrar_sistema(f"Error: {str(e)}")
            self.finalizar_ejecucion()
            
    def enviar_entrada(self):
        """Procesa la entrada del usuario"""
        texto = self.entrada.text()
        if not texto:
            return
            
        self.entrada.clear()
        
        if self.compilador and self.compilador.esperando_entrada:
            self.compilador.procesar_entrada(texto)
        else:
            self.mostrar_sistema("No hay una solicitud de entrada activa.")
            
    def detener_ejecucion(self):
        """Detiene la ejecución del código"""
        if self.ejecucion_activa:
            self.mostrar_sistema("Ejecución detenida por el usuario.")
            self.finalizar_ejecucion()
            
    def finalizar_ejecucion(self):
        """Finaliza la ejecución y restaura el estado"""
        self.ejecucion_activa = False
        # Restaurar stdout
        if hasattr(self, 'stdout_redirector'):
            sys.stdout = self.stdout_redirector.old_stdout
        self.mostrar_sistema("Ejecución finalizada.")

def main():
    import sys
    app = QApplication(sys.argv)
    Ejecucion = QMainWindow()
    ui = Ui_Ejecucion()
    ui.setupUi(Ejecucion)
    Ejecucion.show()
    sys.exit(app.exec())
if __name__ == "__main__":
    main()