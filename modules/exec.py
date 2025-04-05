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
    QVBoxLayout, QWidget)
import iconos_rc
from core import Interprete as core
class Ui_Ejecucion(object):
    def setupUi(self, Ejecucion):
        Ui_Ejecucion.codigo = ""
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
        self.frame_2.setStyleSheet(u"background-image: url(:/fondos/fondos/fondo.jpg);\n"
"background-whidt: 300px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalScrollBar = QScrollBar(self.frame_2)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setGeometry(QRect(550, 0, 16, 451))
        self.verticalScrollBar.setOrientation(Qt.Vertical)
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

        self.btnAumentar = QPushButton(self.verticalLayoutWidget)
        self.btnAumentar.setObjectName(u"btnAumentar")
        self.btnAumentar.setStyleSheet(u"background-color: rgba(0,0,0,0);")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/acercarse.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnAumentar.setIcon(icon3)
        self.btnAumentar.setIconSize(QSize(50, 50))

        self.verticalLayout.addWidget(self.btnAumentar)

        self.btnReducir = QPushButton(self.verticalLayoutWidget)
        self.btnReducir.setObjectName(u"btnReducir")
        self.btnReducir.setStyleSheet(u"background-color: rgba(0,0,0,0);")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/alejar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnReducir.setIcon(icon4)
        self.btnReducir.setIconSize(QSize(50, 50))

        self.verticalLayout.addWidget(self.btnReducir)

        self.verCodigoJS = QPushButton(self.verticalLayoutWidget)
        self.verCodigoJS.setObjectName(u"verCodigoJS")
        self.verCodigoJS.setCursor(QCursor(Qt.OpenHandCursor))
        self.verCodigoJS.setStyleSheet(u"background-color: rgba(0,0,0,0);")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/js.png", QSize(), QIcon.Normal, QIcon.Off)
        self.verCodigoJS.setIcon(icon5)
        self.verCodigoJS.setIconSize(QSize(50, 50))
        self.verticalLayout.addWidget(self.verCodigoJS)
        Ejecucion.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Ejecucion)
        self.statusbar.setObjectName(u"statusbar")
        Ejecucion.setStatusBar(self.statusbar)
        self.retranslateUi(Ejecucion)
        QMetaObject.connectSlotsByName(Ejecucion)

    # setupUi

    def set_code(self, code):
        Ui_Ejecucion.codigo = code
        print(code)
        
    def retranslateUi(self, Ejecucion):
        Ejecucion.setWindowTitle(QCoreApplication.translate("Ejecucion", u"MainWindow", None))
        self.pushButton.setText("")
        self.btnCorrer.setText("")
        self.btnParar.setText("")
        self.btnAumentar.setText("")
        self.btnReducir.setText("")
        self.verCodigoJS.setText("")
    # retranslateUi

