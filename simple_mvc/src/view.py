import sys
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QApplication


class CounterView(QWidget):
    def __init__(self):
        super().__init__()

        self.label = QLabel("Count: 0", self)
        self.increment_button = QPushButton("Increment", self)
        self.reset_button = QPushButton("Reset", self)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.increment_button)
        layout.addWidget(self.reset_button)

        self.setLayout(layout)
        self.setWindowTitle("MVC Counter Example")
        self.resize(200, 100)

    def update_label(self, count):
        self.label.setText(f"Count: {count}")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    view = CounterView()
    view.show()

    sys.exit(app.exec())
