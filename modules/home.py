from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QFrame,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QScrollBar,
    QSizePolicy,
    QStatusBar,
    QTextEdit,
    QWidget,
    QFileDialog,
    QInputDialog,
)
from iconos_rc import *
from code import Ui_Form as codeui
from exec import Ui_Ejecucion as execui
from core import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(871, 663)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName("frame")
        self.frame.setGeometry(QRect(0, 0, 871, 91))
        self.frame.setStyleSheet("background-color: rgb(201, 233, 210)")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(20, 10, 61, 61))
        self.label.setStyleSheet("border-radius: 5px;")
        self.label.setPixmap(QPixmap(":/icons/icons/logo-logicflow.png"))
        self.label.setScaledContents(True)
        self.horizontalLayoutWidget = QWidget(self.frame)
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(90, 10, 781, 90))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btnImportar = QPushButton(self.horizontalLayoutWidget)
        self.btnImportar.setObjectName("btnImportar")
        self.btnImportar.setCursor(QCursor(Qt.OpenHandCursor))
        self.btnImportar.setStyleSheet("background-color: rgba(0,0,0,0);")
        icon = QIcon()
        icon.addFile(
            ":/icons/icons/carpeta-abierta.png", QSize(), QIcon.Normal, QIcon.Off
        )
        self.btnImportar.setIcon(icon)
        self.btnImportar.setIconSize(QSize(50, 50))
        self.horizontalLayout.addWidget(self.btnImportar)
        self.btnExportar = QPushButton(self.horizontalLayoutWidget)
        self.btnExportar.setObjectName("btnExportar")
        self.btnExportar.setCursor(QCursor(Qt.OpenHandCursor))
        self.btnExportar.setStyleSheet("background-color: rgba(0,0,0,0);")
        icon1 = QIcon()
        icon1.addFile(":/icons/icons/documento.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnExportar.setIcon(icon1)
        self.btnExportar.setIconSize(QSize(80, 80))
        self.horizontalLayout.addWidget(self.btnExportar)
        self.btnCorrer = QPushButton(self.horizontalLayoutWidget)
        self.btnCorrer.setObjectName("btnCorrer")
        self.btnCorrer.setCursor(QCursor(Qt.OpenHandCursor))
        self.btnCorrer.setStyleSheet("background-color: rgba(0,0,0,0);")
        icon2 = QIcon()
        icon2.addFile(
            ":/icons/icons/boton-de-play.png", QSize(), QIcon.Normal, QIcon.Off
        )
        self.btnCorrer.setIcon(icon2)
        self.btnCorrer.setIconSize(QSize(50, 50))
        self.horizontalLayout.addWidget(self.btnCorrer)
        self.verCodigoJS = QPushButton(self.horizontalLayoutWidget)
        self.verCodigoJS.setObjectName("verCodigoJS")
        self.verCodigoJS.setCursor(QCursor(Qt.OpenHandCursor))
        self.verCodigoJS.setStyleSheet("background-color: rgba(0,0,0,0);")
        icon3 = QIcon()
        icon3.addFile(":/icons/icons/js.png", QSize(), QIcon.Normal, QIcon.Off)
        self.verCodigoJS.setIcon(icon3)
        self.verCodigoJS.setIconSize(QSize(50, 50))

        self.horizontalLayout.addWidget(self.verCodigoJS)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName("frame_2")
        self.frame_2.setGeometry(QRect(0, 90, 871, 561))
        self.frame_2.setStyleSheet(
            "background-color: rgb(254, 249, 242)\n" "color: black;"
        )
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalScrollBar = QScrollBar(self.frame_2)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        self.horizontalScrollBar.setGeometry(QRect(10, 545, 991, 21))
        self.horizontalScrollBar.setOrientation(Qt.Horizontal)
        self.textEdit = QTextEdit(self.frame_2)
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setGeometry(QRect(0, 0, 661, 561))
        self.textEdit.setStyleSheet('font: 15pt "Fira Code";')
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName("frame_3")
        self.frame_3.setGeometry(QRect(660, 0, 211, 551))
        self.frame_3.setStyleSheet(
            "background-color: rgb(201, 233, 210);\n"
            "border-color: rgb(0, 0, 0);\n"
            "color: black;"
        )
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.btnDeclarar = QPushButton(self.frame_3)
        self.btnDeclarar.setObjectName("btnDeclarar")
        self.btnDeclarar.setGeometry(QRect(10, 110, 191, 41))
        self.btnDeclarar.setCursor(QCursor(Qt.OpenHandCursor))
        self.btnDeclarar.setStyleSheet(
            "background-color: rgb(251, 216, 124);\n"
            'font: 600 12pt "Cascadia Code SemiBold";\n'
            "border-radius: 10px;"
        )
        self.btnMostrar = QPushButton(self.frame_3)
        self.btnMostrar.setObjectName("btnMostrar")
        self.btnMostrar.setGeometry(QRect(10, 10, 191, 41))
        self.btnMostrar.setCursor(QCursor(Qt.OpenHandCursor))
        self.btnMostrar.setStyleSheet(
            "background-color: rgb(251, 216, 124);\n"
            'font: 600 12pt "Cascadia Code SemiBold";\n'
            "border-radius: 10px;"
        )
        self.btnLeer = QPushButton(self.frame_3)
        self.btnLeer.setObjectName("btnLeer")
        self.btnLeer.setGeometry(QRect(10, 60, 191, 41))
        self.btnLeer.setCursor(QCursor(Qt.OpenHandCursor))
        self.btnLeer.setStyleSheet(
            "background-color: rgb(251, 216, 124);\n"
            'font: 600 12pt "Cascadia Code SemiBold";\n'
            "border-radius: 10px;"
        )
        self.btnAsignar = QPushButton(self.frame_3)
        self.btnAsignar.setObjectName("btnAsignar")
        self.btnAsignar.setGeometry(QRect(10, 160, 191, 41))
        self.btnAsignar.setCursor(QCursor(Qt.OpenHandCursor))
        self.btnAsignar.setStyleSheet(
            "background-color: rgb(251, 216, 124);\n"
            'font: 600 12pt "Cascadia Code SemiBold";\n'
            "border-radius: 10px;"
        )
        self.btnCondicion = QPushButton(self.frame_3)
        self.btnCondicion.setObjectName("btnCondicion")
        self.btnCondicion.setGeometry(QRect(10, 210, 191, 41))
        self.btnCondicion.setCursor(QCursor(Qt.OpenHandCursor))
        self.btnCondicion.setStyleSheet(
            "background-color: rgb(251, 216, 124);\n"
            'font: 600 12pt "Cascadia Code SemiBold";\n'
            "border-radius: 10px;"
        )
        self.btnRepetirSi = QPushButton(self.frame_3)
        self.btnRepetirSi.setObjectName("btnRepetirSi")
        self.btnRepetirSi.setGeometry(QRect(10, 260, 191, 41))
        self.btnRepetirSi.setCursor(QCursor(Qt.OpenHandCursor))
        self.btnRepetirSi.setStyleSheet(
            "background-color: rgb(251, 216, 124);\n"
            'font: 600 12pt "Cascadia Code SemiBold";\n'
            "border-radius: 10px;"
        )
        # self.btnHacerHasta = QPushButton(self.frame_3)
        # self.btnHacerHasta.setObjectName("btnHacerHasta")
        # self.btnHacerHasta.setGeometry(QRect(10, 310, 191, 41))
        # self.btnHacerHasta.setCursor(QCursor(Qt.OpenHandCursor))
        # self.btnHacerHasta.setStyleSheet(
        #     "background-color: rgb(251, 216, 124);\n"
        #     'font: 600 12pt "Cascadia Code SemiBold";\n'
        #     "border-radius: 10px;"
        # )
        self.btnDefinirFuncion = QPushButton(self.frame_3)
        self.btnDefinirFuncion.setObjectName("btnDefinirFuncion")
        self.btnDefinirFuncion.setGeometry(QRect(10, 360, 191, 41))
        self.btnDefinirFuncion.setCursor(QCursor(Qt.OpenHandCursor))
        self.btnDefinirFuncion.setStyleSheet(
            "background-color: rgb(251, 216, 124);\n"
            'font: 600 12pt "Cascadia Code SemiBold";\n'
            "border-radius: 10px;"
        )

        self.btnDefinirFuncion.setEnabled(False)
        self.btnDefinirFuncion.setVisible(False)
        self.label.setVisible(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
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
        self.btnDefinirFuncion.clicked.connect(self.definir_funcion)
        self.btnImportar.clicked.connect(self.importar_archivo)
        self.btnExportar.clicked.connect(self.exportar_archivo)
        self.verCodigoJS.clicked.connect(self.abrir_codigo)
        self.btnCorrer.clicked.connect(self.abrir_exec)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.label.setText("")
        self.btnImportar.setText("")
        self.btnExportar.setText("")
        self.btnCorrer.setText("")
        self.verCodigoJS.setText("")
        # self.btnAyuda.setText("")
        self.btnDeclarar.setText(
            QCoreApplication.translate("MainWindow", "Declarar Variable", None)
        )
        self.btnMostrar.setText(
            QCoreApplication.translate("MainWindow", "Mostrar", None)
        )
        self.btnLeer.setText(QCoreApplication.translate("MainWindow", "Leer", None))
        self.btnAsignar.setText(
            QCoreApplication.translate("MainWindow", "Asignar Valor", None)
        )
        self.btnCondicion.setText(
            QCoreApplication.translate("MainWindow", "Establecer Condici\u00f3n", None)
        )
        self.btnRepetirSi.setText(
            QCoreApplication.translate("MainWindow", "Repetir Si", None)
        )
        # self.btnHacerHasta.setText(
        #     QCoreApplication.translate("MainWindow", "Hacer Hasta", None)
        # )
        self.btnDefinirFuncion.setText(
            QCoreApplication.translate("MainWindow", "Definir Funci\u00f3n", None)
        )

    # retranslateUi
    def inicializar_codigo(self):
        self.textEdit.setText("Inicio (NombreAlgoritmo)\n\nFin")
        self.textEdit.setTextColor(QColor(0, 255, 0))

    def importar_archivo(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        fileName, _ = QFileDialog.getOpenFileName(
            None, "Importar Archivo", "", "Archivos LogicFlow (*.sam)", options=options
        )
        if fileName:
            print(f"Archivo seleccionado: {fileName}")
            with open(fileName, "r") as file:
                codigo = file.read()
                self.textEdit.setText(codigo)

    def exportar_archivo(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        fileName, _ = QFileDialog.getSaveFileName(
            None, "Exportar Archivo", "", "Archivos LogicFlow (*.sam)", options=options
        )
        if fileName:
            print(f"Archivo seleccionado: {fileName}")
            codigo = self.exportar_codigo()
            with open(fileName, "w") as file:
                file.write(codigo)

    def abrir_codigo(self):
        self.code = QMainWindow()
        self.ui = codeui()
        self.ui.setupUi(self.code)
        traductor = TraductorJS()
        codigo = traductor.traducir(self.textEdit.toPlainText())
        self.ui.set_codigo(codigo)
        self.code.show()

    def exportar_codigo(self):
        codigo = self.textEdit.toPlainText()
        return codigo

    def mostrar(self):
        opciones = ["Texto", "Variable"]
        tipo, ok1 = QInputDialog.getItem(
            None, "Tipo de Salida", "Seleccione el tipo:", opciones, 0, False
        )
        if ok1 and tipo:
            if tipo == "Texto":
                texto, ok2 = QInputDialog.getText(
                    None, "Mostrar", "Ingrese el texto a mostrar:"
                )
                if ok2 and texto:
                    self.textEdit.insertPlainText(f'\tmostrar("{texto}")\n')
            elif tipo == "Variable":
                variable, ok2 = QInputDialog.getText(
                    None, "Mostrar", "Ingrese el nombre de la variable a mostrar:"
                )
                if ok2 and variable:
                    self.textEdit.insertPlainText(f"\tmostrar({variable})\n")

    def leer(self):
        variable, ok = QInputDialog.getText(
            None, "Leer", "Ingrese el nombre de la variable:"
        )
        if ok and variable:
            self.textEdit.insertPlainText(f"\tleer({variable})\n")

    def declarar(self):
        nombre, ok1 = QInputDialog.getText(
            None, "Declarar Variable", "Nombre de la variable:"
        )
        if ok1 and nombre:
            tipos = ["entero", "decimal", "cadena", "booleano"]
            tipo, ok2 = QInputDialog.getItem(
                None, "Tipo de Variable", "Seleccione el tipo:", tipos, 0, False
            )
            if ok2 and tipo:
                self.textEdit.insertPlainText(f"\tdeclarar {nombre} tipo: {tipo}\n")

    def asignar(self):
        variable, ok1 = QInputDialog.getText(
            None, "Asignar Valor", "Nombre de la variable:"
        )
        if ok1 and variable:
            valor, ok2 = QInputDialog.getText(
                None, "Asignar Valor", f"Valor para {variable}:"
            )
            if ok2 and valor:
                self.textEdit.insertPlainText(f"\t   {variable} = {valor}\n")

    def establecer_condicion(self):
        condicion, ok = QInputDialog.getText(
            None, "Condición", "Ingrese la condición (ej: x > 5):"
        )
        if ok and condicion:
            self.textEdit.insertPlainText(
                f"\t   si ({condicion}) ejecutar: \n\t\t...\n\t   si no: \n\t\t...\n"
            )

    def repetir_si(self):
        condicion, ok = QInputDialog.getText(
            None, "Repetir Si", "Ingrese la condición (ej: x < 10):"
        )
        if ok and condicion:
            self.textEdit.insertPlainText(
                f"\t   repetir si ({condicion}) ejecutar: \n\t...\n"
            )

    def hacer_hasta(self):
        condicion, ok = QInputDialog.getText(
            None, "Hacer Hasta", "Ingrese la condición (ej: x == 0):"
        )
        if ok and condicion:
            self.textEdit.insertPlainText(
                f"\t   hacer hasta ({condicion}): \n\t\t...\n"
            )

    def definir_funcion(self):
        nombre, ok1 = QInputDialog.getText(
            None, "Definir Función", "Nombre de la función:"
        )
        if ok1 and nombre:
            parametros, ok2 = QInputDialog.getText(
                None, "Parámetros", "Ingrese los parámetros (separados por comas):"
            )
            if ok2:
                params = parametros if parametros else ""
                self.textEdit.insertPlainText(
                    f"\t   definir {nombre}({params}): \n\t...\n"
                )

    def traducir_codigo(self, codigo):
        codigo = self.textEdit.toPlainText()
        traductor = TraductorJS()
        codigojs = traductor.traducir(codigo)
        self.abrir_codigo(codigojs)
    
    def aumentar_fuente(self):
        font = self.textEdit.font()
        font.setPointSize(font.pointSize() + 1)
        self.textEdit.setFont(font)
    def reducir_fuente(self):
        font = self.textEdit.font()
        font.setPointSize(font.pointSize() - 1)
        self.textEdit.setFont(font)

    def abrir_exec(self):
        self.exec = QMainWindow()
        self.ui = execui()
        self.ui.setupUi(self.exec)
        codigo = self.textEdit.toPlainText()
        self.ui.setCodigo(codigo)
        self.exec.show()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())