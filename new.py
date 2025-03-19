import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QWidget()
    w.setWindowTitle("QBoxLayout Example")

    layout = QVBoxLayout()

    button1 = QPushButton("Button 1")
    button2 = QPushButton("Button 2")

    layout.addWidget(button1)
    layout.addWidget(button2)

    w.setLayout(layout)

    w.resize(300, 200)
    w.show()

    sys.exit(app.exec_())