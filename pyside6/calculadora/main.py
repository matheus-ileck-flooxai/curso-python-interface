import sys
from PySide6.QtWidgets import QApplication
from info import Info, QLabel
from buttons import Button
from display import Display
from main_window import MainWindow
from PySide6.QtGui import QIcon
from styles import setupTheme
from variables import ICON_PATH


if __name__ == '__main__':
    app = QApplication(sys.argv)
    setupTheme(app)
    window = MainWindow()
    
    # Define o icone
    icon = QIcon(str(ICON_PATH))
    window.setWindowIcon(icon)

    # Info
    info = Info('2.0 ^ 10.0 = 1024')
    window.addToVLayout(info)


    # Display
    display = Display()
    window.addToVLayout(display)

    # Botao
    button = Button('Texto do botão')
    window.addToVLayout(button)

    # Define um tamanho Fixo da janela
    window.adjustFixedSize()

    window.show()

    app.exec()