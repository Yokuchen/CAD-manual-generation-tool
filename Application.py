from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtWidgets import QVBoxLayout
from ui_index import Ui_Dialog
from PySide6.QtCore import QUrl
from PySide6.QtGui import QGuiApplication, QSurfaceFormat
from PySide6.QtQml import QQmlApplicationEngine
from ui_saved import Ui_Dialog as Ui_Dialog_2
from ui_import import Ui_Dialog as Ui_Dialog_3
import sys
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PySide6.QtCore import Signal, Slot
from PySide6.QtPrintSupport import QPrinter
from PySide6.QtWidgets import QApplication, QDialog, QFileDialog
from ui_feedback import Ui_Dialog as Ui_FeedbackDialog
from ui_feedbacksaved import Ui_Dialog as Ui_FeedbackSavedDialog
import time


class MainApp(QtWidgets.QDialog, Ui_Dialog):
    # Define signals
    zoomChanged = Signal(float)
    transparencyChanged = Signal(float)
    materialChanged = Signal(bool, str)

    def __init__(self):
        super(MainApp, self).__init__()
        self.second_window = None
        self.setupUi(self)

        # Connect the button to the method to switch tabs
        self.open_in_editor_button.clicked.connect(self.open_editor_tab)
        self.generate_button.clicked.connect(self.open_save_tab)
        self.generate_button_2.clicked.connect(self.open_save_tab)
        self.save_cancel.clicked.connect(self.open_generate_tab)
        self.openFolder.clicked.connect(self.file_browse_save)

        self.save_save.clicked.connect(self.open_save_window)
        self.layout = QVBoxLayout(self)
        self.setLayout(self.layout)
        self.pushButton_5.clicked.connect(self.open_view_tab)
        self.pushButton_5.clicked.connect(self.import_annotations_to_textEdit)
        self.pushButton_5.clicked.connect(self.save_text)

        # Create a QQuickWidget for 3D view
        self.quickWidget.setSource(QUrl.fromLocalFile("main.qml"))
        # self.horizontalSlider.valueChanged.connect(self.onZoomChanged)
        # self.horizontalSlider_2.valueChanged.connect(self.onTransparencyChanged)
        # (lambda state, model_id="model_cu_1": self.onMaterialChanged(state, model_id))
        # self.checkBox.stateChanged.connect(lambda state, model_id="": self.onMaterialChanged(state, model_id))
        # Dictionary to map checkboxes to their respective texts with default values
        # Connections for the second group of checkboxes
        self.checkBox_4.clicked.connect(lambda: self.checkbox_clicked_group2(self.checkBox_4))
        self.checkBox_5.clicked.connect(lambda: self.checkbox_clicked_group2(self.checkBox_5))
        self.checkBox_6.clicked.connect(lambda: self.checkbox_clicked_group2(self.checkBox_6))
        self.checkBox_7.clicked.connect(lambda: self.checkbox_clicked_group2(self.checkBox_7))

        self.checkboxTexts = {
            self.checkBox_4: "Annotation of part 1 - ",
            self.checkBox_5: "Annotation of part 2 - ",
            self.checkBox_6: "Annotation of part 3 - ",
            self.checkBox_7: "Annotation of part 4 - "  # New checkbox
        }

        # Track the currently active checkbox
        self.currentCheckbox = None

        # Connections for checkboxes
        self.checkBox_4.clicked.connect(lambda: self.update_textEdit(self.checkBox_4))
        self.checkBox_5.clicked.connect(lambda: self.update_textEdit(self.checkBox_5))
        self.checkBox_6.clicked.connect(lambda: self.update_textEdit(self.checkBox_6))
        self.checkBox_7.clicked.connect(lambda: self.update_textEdit(self.checkBox_7))  # New connection

        # Connect the save button
        self.pushButton_2.clicked.connect(self.save_text)
        # Connect buttons to their respective methods
        self.pushButton_3.clicked.connect(self.import_annotations_to_textEdit)
        self.pushButton.clicked.connect(self.save_as_pdf)  # Save as PDF
        self.pushButton_4.clicked.connect(self.add_image)  # Add Image
        # Connect the feedback button to the method to open the feedback dialog
        self.feedback_button.clicked.connect(self.show_feedback_dialog)
        self.save_text()

    def checkbox_clicked_group2(self, clicked_checkbox):
        # Logic for the second group
        self.checkBox_4.setChecked(False)
        self.checkBox_5.setChecked(False)
        self.checkBox_6.setChecked(False)
        self.checkBox_7.setChecked(False)
        clicked_checkbox.setChecked(True)

    def update_textEdit(self, clicked_checkbox):
        # Save the current text before changing the checkbox
        if self.currentCheckbox:
            self.checkboxTexts[self.currentCheckbox] = self.textEdit.toPlainText()

        # Update the QTextEdit with the text related to the clicked checkbox
        self.textEdit.setText(self.checkboxTexts[clicked_checkbox])
        self.currentCheckbox = clicked_checkbox

    def open_editor_tab(self):
        self.Generate.setCurrentIndex(1)

    def open_save_tab(self):
        self.Generate.setCurrentIndex(2)

    def open_generate_tab(self):
        self.Generate.setCurrentIndex(0)

    def open_view_tab(self):
        self.Generate.setCurrentIndex(3)

    def file_browse_save(self):
        filename = QtWidgets.QFileDialog.getSaveFileName(parent=self, caption='Save as', dir='.')

        if filename:
            self.lineEdit_2.setText(filename[0])

    def file_browse_open(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(parent=self, caption='Open file', dir='.')

    @Slot(int)
    def onZoomChanged(self, value):
        # Convert value to appropriate scale
        self.zoomChanged.emit(value)

    @Slot(int)
    def onTransparencyChanged(self, value):
        # Convert value to appropriate scale
        self.transparencyChanged.emit(value)

    @Slot(int)
    def onMaterialChanged(self, state, model_id):
        print(state == QtCore.Qt.CheckState)
        if state == 0:
            state_pass = False
        else:
            state_pass = True
        print(state, model_id, state_pass)
        self.materialChanged.emit(state_pass, model_id)

    def open_save_window(self):
        if not self.second_window:
            self.second_window = SecondApp()
        self.second_window.show()

    def add_image(self):
        # Open a file dialog to select an image
        image_path, _ = QFileDialog.getOpenFileName(self, "Select an image",
                                                    "", "Images (*.png *.xpm *.jpg *.jpeg *.bmp *.gif)")
        if image_path:
            # Insert image at the current cursor position in textEdit_2
            self.textEdit_2.insertHtml(f"<img src='{image_path}'/><br>")

    def save_text(self):
        # Define the file path
        file_path = os.path.join(os.path.dirname(__file__), 'annotations.txt')

        # Write all annotations to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            for checkbox, text in self.checkboxTexts.items():
                file.write(f"{checkbox.objectName()}: {text}\n\n")

        print("All annotations saved to", file_path)

    def save_as_pdf(self):
        # Open a file dialog to specify the PDF file path
        pdf_path, _ = QFileDialog.getSaveFileName(self, "Save as PDF", "", "PDF files (*.pdf)")
        if pdf_path:
            printer = QPrinter(QPrinter.HighResolution)
            printer.setOutputFormat(QPrinter.PdfFormat)
            printer.setOutputFileName(pdf_path)
            self.textEdit_2.document().print_(printer)
            print("Document saved as PDF to", pdf_path)

    def import_annotations_to_textEdit(self):
        file_path = os.path.join(os.path.dirname(__file__), 'annotations.txt')
        print("Importing from file path:", os.path.abspath(file_path))  # Print the absolute file path

        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.readlines()

            processed_content = ""
            for line in content:
                # Split the line at the first colon and take the second part
                parts = line.split(':', 1)
                if len(parts) == 2:
                    processed_content += parts[1].strip() + "\n"

            self.textEdit_2.setText(processed_content)
        except FileNotFoundError:
            print("File not found:", file_path)

    def save_text(self):
        # Update the current checkbox's annotation with the latest text
        if self.currentCheckbox:
            self.checkboxTexts[self.currentCheckbox] = self.textEdit.toPlainText()

        # Now proceed to save all annotations
        file_path = os.path.join(os.path.dirname(__file__), 'annotations.txt')
        with open(file_path, 'w', encoding='utf-8') as file:
            for checkbox, text in self.checkboxTexts.items():
                file.write(f"{checkbox.objectName()}: {text}\n\n")

    def show_feedback_dialog(self):
        dialog = FeedbackDialog(self)
        dialog.exec()  # Changed from exec_() to exec()


class SecondApp(QtWidgets.QDialog, Ui_Dialog_2):
    def __init__(self):
        super(SecondApp, self).__init__()
        self.setupUi(self)
        self.open_in_folder_button.clicked.connect(self.close)
        self.open_in_folder_button.clicked.connect(self.open_in_folder)

        self.return_button.clicked.connect(self.close)

    def open_in_folder(self):
        # image = mpimg.imread("manual.jpg")
        # plt.imshow(image)
        # plt.show()
        # subprocess.call(["xdg-open", "GearboxProductManual.pdf"])
        os.startfile("GearboxProductManual.pdf")


class ImportApp(QtWidgets.QDialog, Ui_Dialog_3):
    def __init__(self):
        super(ImportApp, self).__init__()
        self.main_window = None
        self.setupUi(self)
        self.openFolder_import.clicked.connect(self.file_browse_open)

        self.open_import.clicked.connect(self.open_main_window)
        self.open_import.clicked.connect(self.close)

    def open_main_window(self):
        if not self.main_window:
            self.main_window = MainApp()
        self.main_window.show()

    def file_browse_open(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(parent=self, caption='Open file', dir='.')
        if filename:
            self.lineEdit_import.setText(filename[0])


class FeedbackDialog(QtWidgets.QDialog, Ui_FeedbackDialog):
    def __init__(self, parent=None):
        super(FeedbackDialog, self).__init__(parent)
        self.setupUi(self)

        # Connect the Submit and Cancel buttons to their respective slots
        self.Submitfeedback.clicked.connect(self.submit_feedback)
        self.cancelfeedback.clicked.connect(self.close)

    def submit_feedback(self):
        # Implement the logic for submitting feedback
        # For example, fetch text from self.textEdit and self.textEdit_2
        feedback = self.textEdit.toPlainText()
        email = self.textEdit_2.toPlainText()

        # Process the feedback and email as needed
        print("Feedback submitted:", feedback, "Email:", email)
        # Close the current dialog
        self.close()

        # Open the feedback saved dialog
        feedback_saved_dialog = FeedbackSavedDialog(self.parent())
        feedback_saved_dialog.exec()


class FeedbackSavedDialog(QtWidgets.QDialog, Ui_FeedbackSavedDialog):
    def __init__(self, parent=None):
        super(FeedbackSavedDialog, self).__init__(parent)
        self.setupUi(self)
        # Ensure this button exists in the UI file
        self.feedbackclose.clicked.connect(self.close)


def main():
    app = QtWidgets.QApplication(sys.argv)
    main_app = MainApp()
    import_app = ImportApp()
    import_app.show()
    # main_app.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
