import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QPlainTextEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
from PyQt5 import QtCore

from ask import ask

class Chatbot(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Chatbot Cat")

        self.label = QLabel(self)
        self.label.setText("Chatbot Cat")
        self.label.move(0, 0)
        self.label.resize(720, 50)
        self.label.setStyleSheet("font-size: 24px; font-weight: bold; color: black; background-color: white")

        self.input_entry = QLineEdit(self)
        self.input_entry.move(50, 50)
        self.input_entry.resize(620, 450)
        self.input_entry.setStyleSheet("background-color: white; color: black; font-size: 16px")

        self.clear_button = QPushButton(self)
        self.clear_button.setText("Clear")
        self.clear_button.move(50, 550)
        self.clear_button.resize(150, 50)
        self.clear_button.setStyleSheet("background-color: white; color: black; font-size: 16px")
        self.clear_button.clicked.connect(self.clear_input)

        self.send_button = QPushButton(self)
        self.send_button.setText("Send")
        self.send_button.move(520, 550)
        self.send_button.resize(150, 50)
        self.send_button.setStyleSheet("background-color: white; color: black; font-size: 16px")
        self.send_button.clicked.connect(self.ask)

        self.quit_button = QPushButton(self)
        self.quit_button.setText("Quit")
        self.quit_button.move(285, 550)
        self.quit_button.resize(150, 50)
        self.quit_button.setStyleSheet("background-color: white; color: black; font-size: 16px")
        self.quit_button.clicked.connect(self.close)

        self.output_chatbot = QPlainTextEdit(self)
        self.output_chatbot.move(50, 650)
        self.output_chatbot.resize(620, 450)
        self.output_chatbot.setStyleSheet("background-color: white")

        # Add version label
        self.version_label = QLabel(self)
        self.version_label.setText("Version 1.1")
        self.version_label.setAlignment(QtCore.Qt.AlignCenter)
        self.version_label.resize(720, 30)
        self.version_label.move(0, 1120)
        self.version_label.setStyleSheet("font-size: 20px; color: black; background-color: white; border: 2px solid black;")


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Chatbot Cat"
        self.left = 100
        self.top = 100
        self.width = 720
        self.height = 1200
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create input label
        input_label = QLabel('Chatbot Cat 🐱', self)
        input_label.move(0, 0)
        input_label.resize(720, 100)
        input_label.setStyleSheet('font-size: 30px; color: black; background-color: white; border: 2px solid black;')
        
        # Create input textbox
        self.input_entry = QLineEdit(self)
        self.input_entry.move(50, 120)
        self.input_entry.resize(620, 450)
        self.input_entry.setStyleSheet('background-color: white; border: 2px solid black; font-size: 20px;')

        # Create output textbox
        self.output_chatbot = QPlainTextEdit(self)
        self.output_chatbot.move(50, 650)
        self.output_chatbot.resize(620, 450)
        self.output_chatbot.setStyleSheet('background-color: white; border: 2px solid black; font-size: 20px;')

        # Create clear button
        clear_btn = QPushButton('Clear', self)
        clear_btn.move(50, 580)
        clear_btn.resize(150, 50)
        clear_btn.setStyleSheet('background-color: white; color: black; font-size: 20px; border: 2px solid black;')
        clear_btn.clicked.connect(self.clear_input)

        # Create send button
        send_btn = QPushButton('Send', self)
        send_btn.move(520, 580)
        send_btn.resize(150, 50)
        send_btn.setStyleSheet('background-color: white; color: black; font-size: 20px; border: 2px solid black;')
        send_btn.clicked.connect(self.output)

        # Create quit button
        quit_btn = QPushButton('Quit', self)
        quit_btn.move(285, 580)
        quit_btn.resize(150, 50)
        quit_btn.setStyleSheet('background-color: white; color: black; font-size: 20px; border: 2px solid black;')
        quit_btn.clicked.connect(self.quit_app)

        # Add version label
        self.version_label = QLabel(self)
        self.version_label.setText("Version 29.8.23 - Generation 1")
        self.version_label.setAlignment(QtCore.Qt.AlignCenter)
        self.version_label.resize(720, 30)
        self.version_label.move(0, 1120)
        self.version_label.setStyleSheet("font-size: 20px; color: black; border: 0px solid black;")
    
        self.output_chatbot.insertPlainText(ask("check network"))

    def clear_input(self):
        self.input_entry.clear()
        self.output_chatbot.clear()

    def quit_app(self):
        QApplication.quit()
        
    def output(self):
    	self.output_chatbot.clear()
    	self.output_chatbot.insertPlainText(ask(self.input_entry.text()))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())