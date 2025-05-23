# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'codeEDpsHA.ui'
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
    QPlainTextEdit, QPushButton, QSizePolicy, QWidget, QFileDialog)
from iconos_rc import *

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(660, 615)
        Ui_Form.codigo = ""
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 661, 81))
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
        self.horizontalLayoutWidget.setGeometry(QRect(80, 10, 366, 71))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btnExportar = QPushButton(self.horizontalLayoutWidget)
        self.btnExportar.setObjectName(u"btnExportar")
        self.btnExportar.setStyleSheet(u"background-color: rgba(0,0,0,0);")
        icon = QIcon()
        icon.addFile(u":/icons/icons/documento.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnExportar.setIcon(icon)
        self.btnExportar.setIconSize(QSize(80, 80))
        self.horizontalLayout.addWidget(self.btnExportar)
        self.btnAumentar = QPushButton(self.horizontalLayoutWidget)
        self.btnAumentar.setObjectName(u"btnAumentar")
        self.btnAumentar.setStyleSheet(u"background-color: rgba(0,0,0,0);")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/acercarse.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnAumentar.setIcon(icon3)
        self.btnAumentar.setIconSize(QSize(50, 50))

        self.horizontalLayout.addWidget(self.btnAumentar)

        self.btnReducir = QPushButton(self.horizontalLayoutWidget)
        self.btnReducir.setObjectName(u"btnReducir")
        self.btnReducir.setStyleSheet(u"background-color: rgba(0,0,0,0);")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/alejar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnReducir.setIcon(icon4)
        self.btnReducir.setIconSize(QSize(50, 50))
        self.horizontalLayout.addWidget(self.btnReducir)
        self.frame_Codigo = QFrame(Form)
        self.frame_Codigo.setObjectName(u"frame_Codigo")
        self.frame_Codigo.setGeometry(QRect(-10, 80, 681, 531))
        self.frame_Codigo.setStyleSheet(u"background-color: rgb(254, 249, 242);")
        self.frame_Codigo.setFrameShape(QFrame.StyledPanel)
        self.frame_Codigo.setFrameShadow(QFrame.Raised)
        self.plainTextEdit = QPlainTextEdit(self.frame_Codigo)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(10, 0, 661, 541))
        font = QFont()
        font.setFamilies([u"Fira Code SemiBold"])
        font.setBold(True)
        self.plainTextEdit.setFont(font)
        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)
        self.btnExportar.clicked.connect(self.exportar_archivo)
        self.btnAumentar.clicked.connect(self.aumentar_fuente)
        self.btnReducir.clicked.connect(self.reducir_fuente)

    def exportar_archivo(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        fileName, _ = QFileDialog.getSaveFileName(None, "Exportar Archivo", "", "Todos los archivos (*);;Archivos de texto (*.txt)", options=options)
        if fileName:
            print(f"Archivo seleccionado: {fileName}")
    
    def reducir_fuente(self):
        font = self.plainTextEdit.font()
        font.setPointSize(font.pointSize() - 1)
        self.plainTextEdit.setFont(font)

    def aumentar_fuente(self):
        font = self.plainTextEdit.font()
        font.setPointSize(font.pointSize() + 1)
        self.plainTextEdit.setFont(font)

    def set_codigo(self, codigo):
        self.plainTextEdit.setPlainText(codigo)
        Ui_Form.codigo = codigo

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.btnExportar.setText("")
        # self.btnCorrer.setText("")
        # self.btnParar.setText("")
        self.btnAumentar.setText("")
        self.btnReducir.setText("")
        self.plainTextEdit.setPlainText("")