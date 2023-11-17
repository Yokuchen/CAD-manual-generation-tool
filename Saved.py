from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtWidgets import QVBoxLayout
from ui_saved import Ui_Dialog
from PySide6.QtCore import QUrl
from PySide6.QtGui import QGuiApplication, QSurfaceFormat
from PySide6.QtQml import QQmlApplicationEngine
import sys
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os


class MainApp(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        super(MainApp, self).__init__()
        self.setupUi(self)

        self.open_in_folder_button.clicked.connect(self.open_in_folder)
        self.return_button.clicked.connect(self.return_to_main)

    def open_in_folder(self, window):
        image = mpimg.imread("manual.png")
        plt.imshow(image)
        plt.show()

    def return_to_main(self):
        self.Generate.setCurrentIndex(2)


def main():
    app = QtWidgets.QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec())


if __name__ == "__main__":

    main()
