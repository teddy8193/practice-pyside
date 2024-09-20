import sys
from PySide6.QtWidgets import QApplication
from .model import CounterModel
from .view import CounterView
from .controller import CounterController


def main():
    app = QApplication(sys.argv)

    model = CounterModel()
    view = CounterView()
    controller = CounterController(model, view)

    view.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
