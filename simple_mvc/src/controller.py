from .view import CounterView
from .model import CounterModel


class CounterController:
    def __init__(self, model, view):
        self.model: CounterModel = model
        self.view: CounterView = view

        self.view.increment_button.clicked.connect(self.model.increment)
        self.view.reset_button.clicked.connect(self.model.reset)

        self.model.count_changed.connect(self.view.update_label)
