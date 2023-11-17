from PyQt6 import QtWidgets, QtQuickWidgets
from index import Ui_Dialog  # Importing the UI class from index.py
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt6.QtQuickWidgets import QQuickWidget
from PyQt6.QtCore import QUrl
import os
import sys
from pathlib import Path

# from PySide6.QtQuick3D import QQuick3D


class MainApp(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        super(MainApp, self).__init__()
        self.setupUi(self)

        # Connect the button to the method to switch tabs
        self.open_in_editor_button.clicked.connect(self.open_editor_tab)

        self.layout = QVBoxLayout(self)
        self.setLayout(self.layout)

        # Create a QQuickWidget for your 3D view
        self.quickWidget.setSource(QUrl.fromLocalFile("main.qml"))

    def open_editor_tab(self):
        # Switch to the 'tab_modify' tab
        self.Generate.setCurrentIndex(1)  # Assuming 'tab_modify' is at index 1

    def open_3d_window(self):
        # Switch to the 'tab_modify' tab
        self.Generate.setCurrentIndex(1)  # Assuming 'tab_modify' is at index 1


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec())
