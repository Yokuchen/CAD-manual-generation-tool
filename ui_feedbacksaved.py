# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'feedbacksavedGUytrB.ui'
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
        Dialog.resize(481, 281)
        self.textEditSaveInfo = QTextEdit(Dialog)
        self.textEditSaveInfo.setObjectName(u"textEditSaveInfo")
        self.textEditSaveInfo.setGeometry(QRect(220, 30, 241, 231))
        self.textEditSaveInfo.setReadOnly(True)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 481, 291))
        font = QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setPixmap(QPixmap(u"feedbackSent.png"))
        self.label.setScaledContents(True)
        self.feedbackclose = QPushButton(Dialog)
        self.feedbackclose.setObjectName(u"feedbackclose")
        self.feedbackclose.setGeometry(QRect(30, 240, 75, 24))
        self.label.raise_()
        self.textEditSaveInfo.raise_()
        self.feedbackclose.raise_()

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.textEditSaveInfo.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Version: 0.236<br />OS: Windows 11 Pro x64 (10.0.0.22621)<br />Microsoft .NET Framework: 4.8 (4.8.09032)<br />AviSynth: 2.6.0.6 (22-10-2016)<br />============================<br />Name: user<br />Email: ABC@email.com<br />Title: title<br />Log: none</p></body></html>", None))
        self.label.setText("")
        self.feedbackclose.setText(QCoreApplication.translate("Dialog", u"Return", None))
    # retranslateUi

