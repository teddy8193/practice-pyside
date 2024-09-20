from PySide6.QtCore import QObject, Signal, SignalInstance


class CounterModel(QObject):
    count_changed: SignalInstance = Signal(int)

    def __init__(self):
        super().__init__()
        self.count = 0

    def increment(self):
        self.count += 1
        self.count_changed.emit(self.count)

    def reset(self):
        self.count = 0
        self.count_changed.emit(self.count)

    def get_count(self):
        return self.count
