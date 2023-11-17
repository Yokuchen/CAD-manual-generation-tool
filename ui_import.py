# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'importiiCuPh.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QToolButton,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(663, 476)
        self.line = QFrame(Dialog)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(120, 430, 431, 21))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.open_import = QPushButton(Dialog)
        self.open_import.setObjectName(u"open_import")
        self.open_import.setGeometry(QRect(470, 400, 75, 31))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(230, 120, 181, 221))
        self.label.setFrameShape(QFrame.Box)
        self.label.setFrameShadow(QFrame.Raised)
        self.label.setPixmap(QPixmap(u"Explodedview.jpg"))
        self.label.setScaledContents(True)
        self.label.setMargin(1)
        self.label.setOpenExternalLinks(False)
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(120, 10, 431, 371))
        self.frame.setAutoFillBackground(False)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(110, 340, 51, 16))
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(110, 20, 191, 51))
        font = QFont()
        font.setPointSize(20)
        font.setBold(False)
        self.label_3.setFont(font)
        self.label_3.setTextFormat(Qt.RichText)
        self.label_3.setScaledContents(True)
        self.openFolder_import = QToolButton(Dialog)
        self.openFolder_import.setObjectName(u"openFolder_import")
        self.openFolder_import.setGeometry(QRect(450, 400, 21, 31))
        self.lineEdit_import = QLineEdit(Dialog)
        self.lineEdit_import.setObjectName(u"lineEdit_import")
        self.lineEdit_import.setGeometry(QRect(130, 400, 321, 31))
        self.frame.raise_()
        self.label.raise_()
        self.line.raise_()
        self.open_import.raise_()
        self.openFolder_import.raise_()
        self.lineEdit_import.raise_()

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.open_import.setText(QCoreApplication.translate("Dialog", u"open", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Vale.cad", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Recent Projects", None))
        self.openFolder_import.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.lineEdit_import.setPlaceholderText(QCoreApplication.translate("Dialog", u"Last: C:/system/Appdata/Roam/CADM/doc/Vale.cad", None))
    # retranslateUi

