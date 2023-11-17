import os
import sys
from pathlib import Path
from PySide6.QtCore import QUrl
from PySide6.QtGui import QGuiApplication, QSurfaceFormat
from PySide6.QtQml import QQmlApplicationEngine

from PySide6.QtQuick3D import QQuick3D


def window_open():
    app = QGuiApplication(sys.argv)

    QSurfaceFormat.setDefaultFormat(QQuick3D.idealSurfaceFormat(4))

    engine = QQmlApplicationEngine()
    qml_file = os.fspath(Path(__file__).resolve().parent / 'qml3d.qml')
    engine.load(QUrl.fromLocalFile(qml_file))
    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec())


if __name__ == "__main__":
    window_open()

