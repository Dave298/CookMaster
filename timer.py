# timer.py

from PyQt6.QtWidgets import (
    QWidget, QLabel, QSpinBox, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
)
from PyQt6.QtCore import QTimer

class TimerManager(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cooking Timer")
        self.resize(300, 200)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)

        self.time_left = 0

        # UI elements
        self.label = QLabel("Set Timer (in minutes):")
        self.time_input = QSpinBox()
        self.time_input.setRange(1, 180)

        self.start_button = QPushButton("Start Timer")
        self.start_button.clicked.connect(self.start_timer)

        self.time_display = QLabel("00:00")
        self.time_display.setStyleSheet("font-size: 24px;")

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)

        time_layout = QHBoxLayout()
        time_layout.addWidget(self.time_input)
        time_layout.addWidget(self.start_button)
        layout.addLayout(time_layout)

        layout.addWidget(self.time_display)
        self.setLayout(layout)

    def start_timer(self):
        minutes = self.time_input.value()
        self.time_left = minutes * 60  # convert to seconds
        self.update_display()
        self.timer.start(1000)

    def update_timer(self):
        self.time_left -= 1
        self.update_display()
        if self.time_left <= 0:
            self.timer.stop()
            QMessageBox.information(self, "Time's Up", "Your timer has finished!")

    def update_display(self):
        minutes = self.time_left // 60
        seconds = self.time_left % 60
        self.time_display.setText(f"{minutes:02d}:{seconds:02d}")
