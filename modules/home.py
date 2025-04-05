# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'homeQAeLeJ.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QScrollBar, QSizePolicy,
    QStatusBar, QTextEdit, QWidget,QFileDialog, QInputDialog)
from iconos_rc import *
from code import Ui_Form as codeui
from exec import Ui_Ejecucion as execui
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(871, 663)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 871, 91))
        self.frame.setStyleSheet(u"background-color: rgb(201, 233, 210)")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 61, 61))
        self.label.setStyleSheet(u"border-radius: 5px;")
        self.label.setPixmap(QPixmap(u":/icons/icons/logo-logicflow.png"))
        self.label.setScaledContents(True)
        self.horizontalLayoutWidget = QWidget(self.frame)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(90, 10, 781, 90))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btnImportar = QPushButton(self.horizontalLayoutWidget)
        self.btnImportar.setObjectName(u"btnImportar")
        self.btnImportar.setCursor(QCursor(Qt.OpenHandCursor))
        self.btnImportar.setStyleSheet(u"background-color: rgba(0,0,0,0);")
        icon = QIcon()
        icon.addFile(u":/icons/icons/carpeta-abierta.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnImportar.setIcon(icon)
        self.btnImportar.setIconSize(QSize(50, 50))

        self.horizontalLayout.addWidget(self.btnImportar)

        self.btnExportar = QPushButton(self.horizontalLayoutWidget)
        self.btnExportar.setObjectName(u"btnExportar")
        self.btnExportar.setCursor(QCursor(Qt.OpenHandCursor))
        self.btnExportar.setStyleSheet(u"background-color: rgba(0,0,0,0);")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/documento.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnExportar.setIcon(icon1)
        self.btnExportar.setIconSize(QSize(80, 80))

        self.horizontalLayout.addWidget(self.btnExportar)

        self.btnCorrer = QPushButton(self.horizontalLayoutWidget)
        self.btnCorrer.setObjectName(u"btnCorrer")
        self.btnCorrer.setCursor(QCursor(Qt.OpenHandCursor))
        self.btnCorrer.setStyleSheet(u"background-color: rgba(0,0,0,0);")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/boton-de-play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnCorrer.setIcon(icon2)
        self.btnCorrer.setIconSize(QSize(50, 50))

        self.horizontalLayout.addWidget(self.btnCorrer)

        self.verCodigoJS = QPushButton(self.horizontalLayoutWidget)
        self.verCodigoJS.setObjectName(u"verCodigoJS")
        self.verCodigoJS.setCursor(QCursor(Qt.OpenHandCursor))
        self.verCodigoJS.setStyleSheet(u"background-color: rgba(0,0,0,0);")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/js.png", QSize(), QIcon.Normal, QIcon.Off)
        self.verCodigoJS.setIcon(icon3)
        self.verCodigoJS.setIconSize(QSize(50, 50))

        self.horizontalLayout.addWidget(self.verCodigoJS)

        self.btnAyuda = QPushButton(self.horizontalLayoutWidget)
        self.btnAyuda.setObjectName(u"btnAyuda")
        self.btnAyuda.setCursor(QCursor(Qt.OpenHandCursor))
        self.btnAyuda.setStyleSheet(u"background-color: rgba(0,0,0,0);")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/ayuda.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnAyuda.setIcon(icon4)
        self.btnAyuda.setIconSize(QSize(50, 50))

        self.horizontalLayout.addWidget(self.btnAyuda)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 90, 871, 561))
        self.frame_2.setStyleSheet(u"background-color: rgb(254, 249, 242)")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalScrollBar = QScrollBar(self.frame_2)
        self.horizontalScrollBar.setObjectName(u"horizontalScrollBar")
        self.horizontalScrollBar.setGeometry(QRect(10, 545, 991, 21))
        self.horizontalScrollBar.setOrientation(Qt.Horizontal)
        self.textEdit = QTextEdit(self.frame_2)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(0, 0, 661, 561))
        self.textEdit.setStyleSheet(u"font: 15pt \"Fira Code\";")
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(660, 0, 211, 551))
        self.frame_3.setStyleSheet(u"background-color: rgb(201, 233, 210);\n"
"border-color: rgb(0, 0, 0);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.btnDeclarar = QPushButton(self.frame_3)
        self.btnDeclarar.setObjectName(u"btnDeclarar")
        self.btnDeclarar.setGeometry(QRect(10, 110, 191, 41))
        self.btnDeclarar.setCursor(QCursor(Qt.OpenHandCursor))
        self.btnDeclarar.setStyleSheet(u"background-color: rgb(251, 216, 124);\n"
"font: 600 12pt \"Cascadia Code SemiBold\";\n"
"border-radius: 10px;")
        self.btnMostrar = QPushButton(self.frame_3)
        self.btnMostrar.setObjectName(u"btnMostrar")
        self.btnMostrar.setGeometry(QRect(10, 10, 191, 41))
        self.btnMostrar.setCursor(QCursor(Qt.OpenHandCursor))
        self.btnMostrar.setStyleSheet(u"background-color: rgb(251, 216, 124);\n"
"font: 600 12pt \"Cascadia Code SemiBold\";\n"
"border-radius: 10px;")
        self.btnLeer = QPushButton(self.frame_3)
        self.btnLeer.setObjectName(u"btnLeer")
        self.btnLeer.setGeometry(QRect(10, 60, 191, 41))
        self.btnLeer.setCursor(QCursor(Qt.OpenHandCursor))
        self.btnLeer.setStyleSheet(u"background-color: rgb(251, 216, 124);\n"
"font: 600 12pt \"Cascadia Code SemiBold\";\n"
"border-radius: 10px;")
        self.btnAsignar = QPushButton(self.frame_3)
        self.btnAsignar.setObjectName(u"btnAsignar")
        self.btnAsignar.setGeometry(QRect(10, 160, 191, 41))
        self.btnAsignar.setCursor(QCursor(Qt.OpenHandCursor))
        self.btnAsignar.setStyleSheet(u"background-color: rgb(251, 216, 124);\n"
"font: 600 12pt \"Cascadia Code SemiBold\";\n"
"border-radius: 10px;")
        self.btnCondicion = QPushButton(self.frame_3)
        self.btnCondicion.setObjectName(u"btnCondicion")
        self.btnCondicion.setGeometry(QRect(10, 210, 191, 41))
        self.btnCondicion.setCursor(QCursor(Qt.OpenHandCursor))
        self.btnCondicion.setStyleSheet(u"background-color: rgb(251, 216, 124);\n"
"font: 600 12pt \"Cascadia Code SemiBold\";\n"
"border-radius: 10px;")
        self.btnRepetirSi = QPushButton(self.frame_3)
        self.btnRepetirSi.setObjectName(u"btnRepetirSi")
        self.btnRepetirSi.setGeometry(QRect(10, 260, 191, 41))
        self.btnRepetirSi.setCursor(QCursor(Qt.OpenHandCursor))
        self.btnRepetirSi.setStyleSheet(u"background-color: rgb(251, 216, 124);\n"
"font: 600 12pt \"Cascadia Code SemiBold\";\n"
"border-radius: 10px;")
        self.btnHacerHasta = QPushButton(self.frame_3)
        self.btnHacerHasta.setObjectName(u"btnHacerHasta")
        self.btnHacerHasta.setGeometry(QRect(10, 310, 191, 41))
        self.btnHacerHasta.setCursor(QCursor(Qt.OpenHandCursor))
        self.btnHacerHasta.setStyleSheet(u"background-color: rgb(251, 216, 124);\n"
"font: 600 12pt \"Cascadia Code SemiBold\";\n"
"border-radius: 10px;")
        self.btnDefinirFuncion = QPushButton(self.frame_3)
        self.btnDefinirFuncion.setObjectName(u"btnDefinirFuncion")
        self.btnDefinirFuncion.setGeometry(QRect(10, 360, 191, 41))
        self.btnDefinirFuncion.setCursor(QCursor(Qt.OpenHandCursor))
        self.btnDefinirFuncion.setStyleSheet(u"background-color: rgb(251, 216, 124);\n"
"font: 600 12pt \"Cascadia Code SemiBold\";\n"
"border-radius: 10px;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)
        self.inicializar_codigo()
        self.btnMostrar.clicked.connect(self.mostrar)
        self.btnLeer.clicked.connect(self.leer)
        self.btnDeclarar.clicked.connect(self.declarar)
        self.btnAsignar.clicked.connect(self.asignar)
        self.btnCondicion.clicked.connect(self.establecer_condicion)
        self.btnRepetirSi.clicked.connect(self.repetir_si)
        self.btnHacerHasta.clicked.connect(self.hacer_hasta)
        self.btnDefinirFuncion.clicked.connect(self.definir_funcion)
        self.btnImportar.clicked.connect(self.importar_archivo)
        self.btnExportar.clicked.connect(self.exportar_archivo)
        self.verCodigoJS.clicked.connect(self.abrir_codigo)
        self.btnCorrer.clicked.connect(self.abrir_exec)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.btnImportar.setText("")
        self.btnExportar.setText("")
        self.btnCorrer.setText("")
        self.verCodigoJS.setText("")
        self.btnAyuda.setText("")
        self.btnDeclarar.setText(QCoreApplication.translate("MainWindow", u"Declarar Variable", None))
        self.btnMostrar.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.btnLeer.setText(QCoreApplication.translate("MainWindow", u"Leer", None))
        self.btnAsignar.setText(QCoreApplication.translate("MainWindow", u"Asignar Valor", None))
        self.btnCondicion.setText(QCoreApplication.translate("MainWindow", u"Establecer Condici\u00f3n", None))
        self.btnRepetirSi.setText(QCoreApplication.translate("MainWindow", u"Repetir Si", None))
        self.btnHacerHasta.setText(QCoreApplication.translate("MainWindow", u"Hacer Hasta", None))
        self.btnDefinirFuncion.setText(QCoreApplication.translate("MainWindow", u"Definir Funci\u00f3n", None))
    # retranslateUi
    def inicializar_codigo(self):
        self.textEdit.setText("Inicio (NombreAlgoritmo)\n\nFin")
        self.textEdit.setTextColor(QColor(0, 255, 0))
    
    def importar_archivo(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        fileName, _ = QFileDialog.getOpenFileName(None, "Importar Archivo", "", "Archivos LogicFlow (*.sam)", options=options)
        if fileName:
            print(f"Archivo seleccionado: {fileName}")
            with open(fileName, "r") as file:
                codigo = file.read()
                self.textEdit.setText(codigo)
    
    def exportar_archivo(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        fileName, _ = QFileDialog.getSaveFileName(None, "Exportar Archivo", "", "Archivos LogicFlow (*.sam)", options=options)
        if fileName:
            print(f"Archivo seleccionado: {fileName}")
            codigo = self.exportar_codigo()
            with open(fileName, "w") as file:
                file.write(codigo)
    
    def abrir_codigo(self):
        self.code = QMainWindow()
        self.ui = codeui()
        self.ui.setupUi(self.code)
        self.code.show()

    def exportar_codigo(self):
        codigo = self.textEdit.toPlainText()
        return codigo

    def mostrar(self):
        self.textEdit.insertPlainText('\t   mostrar("Texto" o Variable)\n')
    
    def leer(self):
        self.textEdit.insertPlainText('\t   leer(Variable)\n')
    
    def declarar(self):
        self.textEdit.insertPlainText('\t   declarar nombre_variable tipo: \n')
    
    def asignar(self):
        self.textEdit.insertPlainText('\t   nombre_variable = valor\n')
    
    def establecer_condicion(self):
        self.textEdit.insertPlainText('\t   si (condicion) ejecutar: \n \t\t ... \n')
    
    def repetir_si(self):
        self.textEdit.insertPlainText('\t   repetir si (condicion) ejecutar: \n \t\t ... \n')

    def hacer_hasta(self):
        self.textEdit.insertPlainText('\t   hacer hasta (condicion): \n \t\t ... \n')
    
    def definir_funcion(self):
        self.textEdit.insertPlainText('\t   definir nombre_funcion(parametros): \n \t\t ... \n')

    def mostrar(self):
        opciones = ["Texto", "Variable"]
        tipo, ok1 = QInputDialog.getItem(None, "Tipo de Salida", "Seleccione el tipo:", opciones, 0, False)
        if ok1 and tipo:
            if tipo == "Texto":
                texto, ok2 = QInputDialog.getText(None, "Mostrar", "Ingrese el texto a mostrar:")
                if ok2 and texto:
                    self.textEdit.insertPlainText(f'\t   mostrar("{texto}")\n')
            elif tipo == "Variable":
                variable, ok2 = QInputDialog.getText(None, "Mostrar", "Ingrese el nombre de la variable a mostrar:")
                if ok2 and variable:
                    self.textEdit.insertPlainText(f'\t   mostrar({variable})\n')
   
    def leer(self):
        variable, ok = QInputDialog.getText(None, "Leer", "Ingrese el nombre de la variable:")
        if ok and variable:
            self.textEdit.insertPlainText(f'\t   leer({variable})\n')
   
    def declarar(self):
        nombre, ok1 = QInputDialog.getText(None, "Declarar Variable", "Nombre de la variable:")
        if ok1 and nombre:
            tipos = ["entero", "decimal", "cadena", "booleano"]
            tipo, ok2 = QInputDialog.getItem(None, "Tipo de Variable", "Seleccione el tipo:", tipos, 0, False)
            if ok2 and tipo:
                self.textEdit.insertPlainText(f'\t   declarar {nombre} tipo: {tipo}\n')
   
    def asignar(self):
        variable, ok1 = QInputDialog.getText(None, "Asignar Valor", "Nombre de la variable:")
        if ok1 and variable:
            valor, ok2 = QInputDialog.getText(None, "Asignar Valor", f"Valor para {variable}:")
            if ok2 and valor:
                self.textEdit.insertPlainText(f'\t   {variable} = {valor}\n')
   
    def establecer_condicion(self):
        condicion, ok = QInputDialog.getText(None, "Condición", "Ingrese la condición (ej: x > 5):")
        if ok and condicion:
            self.textEdit.insertPlainText(f'\t   si ({condicion}) ejecutar: \n\t\t...\n')
   
    def repetir_si(self):
        condicion, ok = QInputDialog.getText(None, "Repetir Si", "Ingrese la condición (ej: x < 10):")
        if ok and condicion:
            self.textEdit.insertPlainText(f'\t   repetir si ({condicion}) ejecutar: \n\t\t...\n')
   
    def hacer_hasta(self):
        condicion, ok = QInputDialog.getText(None, "Hacer Hasta", "Ingrese la condición (ej: x == 0):")
        if ok and condicion:
            self.textEdit.insertPlainText(f'\t   hacer hasta ({condicion}): \n\t\t...\n')
   
    def definir_funcion(self):
        nombre, ok1 = QInputDialog.getText(None, "Definir Función", "Nombre de la función:")
        if ok1 and nombre:
            parametros, ok2 = QInputDialog.getText(None, "Parámetros", "Ingrese los parámetros (separados por comas):")
            if ok2:
                params = parametros if parametros else ""
                self.textEdit.insertPlainText(f'\t   definir {nombre}({params}): \n\t\t...\n')
        
    def abrir_exec(self):
        self.exec = QMainWindow()
        self.ui = execui()
        self.ui.setupUi(self.exec)
        self.exec.show()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())