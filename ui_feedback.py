# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'feedbackGTOcPU.ui'
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
        Dialog.resize(544, 351)
        self.textEdit = QTextEdit(Dialog)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(30, 170, 421, 171))
        self.textEdit_2 = QTextEdit(Dialog)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(90, 20, 441, 31))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 20, 51, 31))
        font = QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.Submitfeedback = QPushButton(Dialog)
        self.Submitfeedback.setObjectName(u"Submitfeedback")
        self.Submitfeedback.setGeometry(QRect(460, 280, 75, 24))
        self.cancelfeedback = QPushButton(Dialog)
        self.cancelfeedback.setObjectName(u"cancelfeedback")
        self.cancelfeedback.setGeometry(QRect(460, 310, 75, 24))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 70, 51, 31))
        self.label_2.setFont(font)
        self.textEdit_3 = QTextEdit(Dialog)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(90, 70, 441, 31))
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 120, 51, 31))
        self.label_3.setFont(font)
        self.textEdit_4 = QTextEdit(Dialog)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setGeometry(QRect(90, 120, 441, 31))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.textEdit.setMarkdown("")
        self.textEdit.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"List your question:  ", None))
        self.textEdit_2.setPlaceholderText(QCoreApplication.translate("Dialog", u"User", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Name*:", None))
        self.Submitfeedback.setText(QCoreApplication.translate("Dialog", u"Submit", None))
        self.cancelfeedback.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Email*:", None))
        self.textEdit_3.setPlaceholderText(QCoreApplication.translate("Dialog", u"user@mail.com", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Title*:", None))
        self.textEdit_4.setPlaceholderText(QCoreApplication.translate("Dialog", u"Short description of problem", None))
    # retranslateUi

