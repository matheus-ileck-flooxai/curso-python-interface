import sys
import time

from PySide6.QtCore import QObject, Signal, Slot
from PySide6.QtWidgets import QApplication, QWidget
from ui_workerui import Ui_myWidget


class Worker1(QObject):
    started = Signal(str)
    progress = Signal(str)
    finished = Signal(str)

    def run(self):
        value = '0'
        self.started.emit(value)
        for i in range(5):
            value = str(i)
            self.progress.emit(value)
            time.sleep(1)

        self.finished.emit(value)

class MyWidget(QWidget, Ui_myWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.button1.clicked.connect(self.hardWork1)
        self.button2.clicked.connect(self.hardWork2)

    def hardWork1(self):
       
        self.label1.setText('1 Terminado')
        


    def hardWork2(self):
        time.sleep(5)

        self.label2.setText('hardwork2 Terminado ')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    MyWidget = MyWidget()
    MyWidget.show()
    app.exec()