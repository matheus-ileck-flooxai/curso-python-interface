import sys
from PySide6.QtWidgets import QApplication
from display import Display
from main_window import MainWindow
from PySide6.QtGui import QIcon

from variables import ICON_PATH


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    
    # Define o icone
    icon = QIcon(str(ICON_PATH))
    window.setWindowIcon(icon)

    # Display
    display = Display()
    window.addToVLayout(display)

    # Define um tamanho Fixo da janela
    window.adjustFixedSize()

    window.show()

    app.exec()