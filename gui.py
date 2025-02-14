import sys
import os
import subprocess
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton,
    QFileDialog, QLabel, QFrame, QSizePolicy
)
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox

class VideoEditorGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.input_file = ""  # To store the selected video file path
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Video Editor GUI Frontend")
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
        self.beh_label = QLabel(f"When processing, the edited video replaces the input video. Remember to BACK UP YOUR WORK! ")
        layout.addWidget(self.beh_label)

        # Label and input field for command-line arguments
        self.conk_label = QLabel(f"Built on PyQt5, and VEB rev. 527c8a3. Credit to GanerCodes for the original VEB.")
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
            self.status_label.setText("Please select an input video file.")
            return

        args = self.args_line.text().strip()
        # Build the command string. Adjust if your command needs a different structure.
        command = f"destroy \"{args}\" \"{self.input_file}\""
        self.status_label.setText(f"Running: {command}")

        try:
            result = subprocess.run(command)
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
                error_message = result.stderr or "An error occurred."
                self.status_label.setText(f"Error: {error_message}")
                print(result)
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
    app.setStyle('Fusion')  # Set the application style to Fusion
    gui = VideoEditorGUI()
    gui.show()
    sys.exit(app.exec_())