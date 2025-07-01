import sys
from PySide6.QtWidgets import QApplication
from info import Info, QLabel
from buttons import Button, ButtonsGrid
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
    window.addWidgetToVLayout(info)


    # Display
    display = Display()
    window.addWidgetToVLayout(display)

    #Grid
    buttonsGrid = ButtonsGrid()
    window.vLayout.addLayout(buttonsGrid)

    # Botao
    buttonsGrid.addWidget(Button('7'), 0, 0)
    buttonsGrid.addWidget(Button('8'), 0, 1)
    buttonsGrid.addWidget(Button('9'), 0, 2)
    buttonsGrid.addWidget(Button('4'), 1, 0)
    buttonsGrid.addWidget(Button('5'), 1, 1)
    buttonsGrid.addWidget(Button('6'), 1, 2)
    buttonsGrid.addWidget(Button('1'), 2, 0)
    buttonsGrid.addWidget(Button('2'), 2, 1)
    buttonsGrid.addWidget(Button('3'), 2, 2)
    buttonsGrid.addWidget(Button('0'), 3, 0, 1,3)
    

    # Define um tamanho Fixo da janela
    window.adjustFixedSize()

    window.show()

    app.exec()