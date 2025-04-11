# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'instructionsyAhCDg.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

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
    QGridLayout,
    QLabel,
    QPushButton,
    QSizePolicy,
    QWidget,
)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.resize(501, 140)
        self.frame = QFrame(Form)
        self.frame.setObjectName("frame")
        self.frame.setGeometry(QRect(0, 0, 501, 41))
        self.frame.setStyleSheet("background-color: rgb(201, 233, 210)")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(0, 10, 101, 16))
        self.label.setStyleSheet('font: 700 12pt "Yu Gothic UI";')
        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName("frame_2")
        self.frame_2.setGeometry(QRect(0, 40, 501, 101))
        self.frame_2.setStyleSheet("background-color: rgb(254, 249, 242)")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget = QWidget(self.frame_2)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 501, 101))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.btnResultado = QPushButton(self.gridLayoutWidget)
        self.btnResultado.setObjectName("btnResultado")
        self.btnResultado.setStyleSheet('font: 700 12pt "Yu Gothic UI";')

        self.gridLayout.addWidget(self.btnResultado, 3, 0, 1, 1)

        self.btnDef = QPushButton(self.gridLayoutWidget)
        self.btnDef.setObjectName("btnDef")
        self.btnDef.setStyleSheet('font: 700 12pt "Yu Gothic UI";')

        self.gridLayout.addWidget(self.btnDef, 3, 2, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet('font: 700 12pt "Yu Gothic UI";')

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.btnInit = QPushButton(self.gridLayoutWidget)
        self.btnInit.setObjectName("btnInit")
        self.btnInit.setStyleSheet('font: 700 12pt "Yu Gothic UI";')

        self.gridLayout.addWidget(self.btnInit, 2, 2, 1, 1)

        self.line_2 = QFrame(self.gridLayoutWidget)
        self.line_2.setObjectName("line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_2, 2, 1, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet('font: 700 12pt "Yu Gothic UI";')
        self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1)
        self.line = QFrame(self.gridLayoutWidget)
        self.line.setObjectName("line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.gridLayout.addWidget(self.line, 3, 1, 1, 1)
        self.btnIngreso = QPushButton(self.gridLayoutWidget)
        self.btnIngreso.setObjectName("btnIngreso")
        self.btnIngreso.setStyleSheet('font: 700 12pt "Yu Gothic UI";')
        self.gridLayout.addWidget(self.btnIngreso, 2, 0, 1, 1)
        self.line_3 = QFrame(self.gridLayoutWidget)
        self.line_3.setObjectName("line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.gridLayout.addWidget(self.line_3, 1, 1, 1, 1)
        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    # setupUi
    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", "Form", None))
        self.label.setText(
            QCoreApplication.translate("Form", "Instrucci\u00f3nes", None)
        )
        self.btnResultado.setText(QCoreApplication.translate("Form", "Resultado", None))
        self.btnDef.setText(QCoreApplication.translate("Form", "Definici\u00f3n", None))
        self.label_2.setText(
            QCoreApplication.translate("Form", "Ingreso/Resultado", None)
        )
        self.btnInit.setText(
            QCoreApplication.translate("Form", "Inicializaci\u00f3n", None)
        )
        self.label_3.setText(QCoreApplication.translate("Form", "Datos", None))
        self.btnIngreso.setText(QCoreApplication.translate("Form", "Ingreso", None))

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Form = QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())