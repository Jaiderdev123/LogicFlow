# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'homeLnuDxX.ui'
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
    QStatusBar, QWidget, QFileDialog)
import iconos_rc
from code import Ui_Form as codeui
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1019, 669)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 1021, 81))
        self.frame.setStyleSheet(u"background-color: rgb(201, 233, 210)")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 61, 61))
        self.label.setStyleSheet(u"border-radius: 5px;")
        self.label.setPixmap(QPixmap(u":/icons/icons/logo-logicflow.png"))
        self.label.setScaledContents(True)
        self.horizontalLayoutWidget = QWidget(self.frame)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(90, 10, 571, 71))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btnImportar = QPushButton(self.horizontalLayoutWidget)
        self.btnImportar.setObjectName(u"btnImportar")
        self.btnImportar.setStyleSheet(u"background-color: rgba(0,0,0,0);")
        icon = QIcon()
        icon.addFile(u":/icons/icons/carpeta-abierta.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnImportar.setIcon(icon)
        self.btnImportar.setIconSize(QSize(50, 50))

        self.horizontalLayout.addWidget(self.btnImportar)

        self.btnExportar = QPushButton(self.horizontalLayoutWidget)
        self.btnExportar.setObjectName(u"btnExportar")
        self.btnExportar.setStyleSheet(u"background-color: rgba(0,0,0,0);")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/documento.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnExportar.setIcon(icon1)
        self.btnExportar.setIconSize(QSize(80, 80))

        self.horizontalLayout.addWidget(self.btnExportar)

        self.btnCorrer = QPushButton(self.horizontalLayoutWidget)
        self.btnCorrer.setObjectName(u"btnCorrer")
        self.btnCorrer.setStyleSheet(u"background-color: rgba(0,0,0,0);")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/boton-de-play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnCorrer.setIcon(icon2)
        self.btnCorrer.setIconSize(QSize(50, 50))

        self.horizontalLayout.addWidget(self.btnCorrer)

        self.btnParar = QPushButton(self.horizontalLayoutWidget)
        self.btnParar.setObjectName(u"btnParar")
        self.btnParar.setStyleSheet(u"background-color: rgba(0,0,0,0);")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/detener.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnParar.setIcon(icon3)
        self.btnParar.setIconSize(QSize(50, 50))

        self.horizontalLayout.addWidget(self.btnParar)

        self.btnAnadirFuncion = QPushButton(self.horizontalLayoutWidget)
        self.btnAnadirFuncion.setObjectName(u"btnAnadirFuncion")
        self.btnAnadirFuncion.setStyleSheet(u"background-color: rgba(0,0,0,0);")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/rompecabezas.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnAnadirFuncion.setIcon(icon4)
        self.btnAnadirFuncion.setIconSize(QSize(50, 50))

        self.horizontalLayout.addWidget(self.btnAnadirFuncion)

        self.verCodigoJS = QPushButton(self.horizontalLayoutWidget)
        self.verCodigoJS.setObjectName(u"verCodigoJS")
        self.verCodigoJS.setStyleSheet(u"background-color: rgba(0,0,0,0);")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/js.png", QSize(), QIcon.Normal, QIcon.Off)
        self.verCodigoJS.setIcon(icon5)
        self.verCodigoJS.setIconSize(QSize(50, 50))

        self.horizontalLayout.addWidget(self.verCodigoJS)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 80, 1021, 571))
        self.frame_2.setStyleSheet(u"background-color: rgb(254, 249, 242)")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalScrollBar = QScrollBar(self.frame_2)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setGeometry(QRect(1000, 0, 20, 571))
        self.verticalScrollBar.setOrientation(Qt.Vertical)
        self.horizontalScrollBar = QScrollBar(self.frame_2)
        self.horizontalScrollBar.setObjectName(u"horizontalScrollBar")
        self.horizontalScrollBar.setGeometry(QRect(10, 545, 991, 21))
        self.horizontalScrollBar.setOrientation(Qt.Horizontal)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)
        self.btnImportar.clicked.connect(self.importar_archivo)
        self.btnExportar.clicked.connect(self.exportar_archivo)
        self.verCodigoJS.clicked.connect(self.abrir_codigo)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.btnImportar.setText("")
        self.btnExportar.setText("")
        self.btnCorrer.setText("")
        self.btnParar.setText("")
        self.btnAnadirFuncion.setText("")
        self.verCodigoJS.setText("")
    
    def importar_archivo(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        fileName, _ = QFileDialog.getOpenFileName(None, "Importar Archivo", "", "Todos los archivos (*);;Archivos de texto (*.txt)", options=options)
        if fileName:
            print(f"Archivo seleccionado: {fileName}")
    
    def exportar_archivo(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        fileName, _ = QFileDialog.getSaveFileName(None, "Exportar Archivo", "", "Todos los archivos (*);;Archivos de texto (*.txt)", options=options)
        if fileName:
            print(f"Archivo seleccionado: {fileName}")
    
    def abrir_codigo(self):
        self.code = QMainWindow()
        self.ui = codeui()
        self.ui.setupUi(self.code)
        self.code.show()

    # retranslateUi
#Main method
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())