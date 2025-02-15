import sys
import shutil
import os
import subprocess
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton,
    QFileDialog, QLabel, QFrame, QSizePolicy
)
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox
from qt_material import apply_stylesheet

class VideoEditorGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.input_file = ""  # To store the selected video file path
        self.initUI()

    def initUI(self):
        self.setWindowTitle("VideoEditBot Client")
        self.setWindowIcon(QIcon("ic/Body.png"))
        self.setGeometry(100, 100, 400, 200)  # Increased height to better fit banner

        layout = QVBoxLayout()

        # Banner at the top
        self.banner = QLabel(self)
        self.banner.setAlignment(Qt.AlignCenter)

        # Using an image as a banner (uncomment if you have an image)
        pixmap = QPixmap("banner-sz.png")
        self.banner.setPixmap(pixmap)
        
        # Text-based banner
        # self.banner.setText("Video Editor")
        # self.banner.setFont(QFont("Arial", 24, QFont.Bold))
        self.banner.setFixedHeight(96)  # Set a fixed height for the banner
        self.banner.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        layout.addWidget(self.banner)

        # Horizontal line separator
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        layout.addWidget(line)

        # Label and input field for command-line arguments
        self.args_label = QLabel("Enter arguments:")
        layout.addWidget(self.args_label)

        self.args_line = QLineEdit(self)
        layout.addWidget(self.args_line)

        # Button to select the input video file
        self.file_button = QPushButton("Select Input File", self)
        self.file_button.clicked.connect(self.select_file)
        layout.addWidget(self.file_button)

        # Button to run the command
        self.run_button = QPushButton("Run Command", self)
        self.run_button.clicked.connect(self.run_command)
        layout.addWidget(self.run_button)

        # Label to display status or output messages
        self.status_label = QLabel("")
        layout.addWidget(self.status_label)
        
        # Label and input field for command-line arguments
        self.beh_label = QLabel(f"Copy the file you want to edit to the root folder of this app in order for it to work.")
        layout.addWidget(self.beh_label)

        # Label and input field for command-line arguments
        self.conk_label = QLabel(f"Credit to GanerCodes for the original VideoEditBot")
        layout.addWidget(self.conk_label)

        self.setLayout(layout)
        
    def select_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select Video File",
            "",
            "Compatible files (*.mp4 *.avi *.mkv *.webm *.mov *.png *.jpeg *.jpg *.gif) ",
        )
        if file_path:
            self.input_file = os.path.basename(file_path)
            self.status_label.setText(f"Selected file: {file_path}")

    def run_command(self):
        if not self.input_file:
            self.status_label.setText("Please select an input file.")
            return

        args = self.args_line.text().strip()
        input_file_name = os.path.basename(self.input_file)  # Get the file name
        app_root = os.getcwd()  # Get the current working directory (root of the app)
        input_file_in_root = os.path.join(app_root, input_file_name)  # Path to file in root

        # Build the command string using the copied file name
        command = f"destroy \"{args}\" \"{input_file_name}\""
        self.status_label.setText(f"Running: {command}")

        try:
            result = subprocess.run(
                command,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            if result.returncode == 0:
                self.status_label.setText("Command executed successfully!")
                # Show success popup
                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Information)
                msg_box.setWindowTitle("Success")
                msg_box.setText("The command was executed successfully!")
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()
            else:
                error_message = result.stderr or "An unknown error occurred."
                self.status_label.setText(f"Error: {error_message}")
                # Show error popup
                error_box = QMessageBox()
                error_box.setIcon(QMessageBox.Critical)
                error_box.setWindowTitle("Error")
                error_box.setText("The command failed to execute.")
                error_box.setInformativeText(error_message)
                error_box.setStandardButtons(QMessageBox.Ok)
                error_box.exec_()
        except Exception as e:
            self.status_label.setText(f"Exception: {e}")
            # Show exception popup
            exception_box = QMessageBox()
            exception_box.setIcon(QMessageBox.Critical)
            exception_box.setWindowTitle("Exception")
            exception_box.setText("An exception occurred while running the command.")
            exception_box.setInformativeText(str(e))
            exception_box.setStandardButtons(QMessageBox.Ok)
            exception_box.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_amber.xml')  # Set the application style to Fusion
    gui = VideoEditorGUI()
    gui.show()
    sys.exit(app.exec_())