# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'savedVaAKBS.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QTextEdit, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(542, 292)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 541, 291))
        self.label.setPixmap(QPixmap(u"fileSaved.png"))
        self.label.setScaledContents(True)
        self.open_in_folder_button = QPushButton(Dialog)
        self.open_in_folder_button.setObjectName(u"open_in_folder_button")
        self.open_in_folder_button.setGeometry(QRect(30, 240, 101, 31))
        self.return_button = QPushButton(Dialog)
        self.return_button.setObjectName(u"return_button")
        self.return_button.setGeometry(QRect(140, 240, 101, 31))
        self.textEditSaveInfo = QTextEdit(Dialog)
        self.textEditSaveInfo.setObjectName(u"textEditSaveInfo")
        self.textEditSaveInfo.setGeometry(QRect(270, 20, 261, 251))
        self.textEditSaveInfo.setReadOnly(True)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText("")
        self.open_in_folder_button.setText(QCoreApplication.translate("Dialog", u"Open in folder", None))
        self.return_button.setText(QCoreApplication.translate("Dialog", u"Return", None))
        self.textEditSaveInfo.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ID: 1<br />Size: 348KB<br />Pages: 1<br />Container: PDF<br />Format profile: High@L4<br />Page size: 21.587 x 27.937<br />Color space: YUV<br />Stream size: 4.34 GiB (97%)<br />Writing library: core 157 r2969 d4099dd<br /><br />Author information:<br />Date: dd/mm/yyyy<br />Security: None<br />Read only: No<br /></p></body></html>", None))
    # retranslateUi

