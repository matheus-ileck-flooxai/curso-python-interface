import sys
from PySide6.QtWidgets import QApplication, QLabel
from main_window import MainWindow
from PySide6.QtGui import QIcon

from variables import ICON_PATH

def temp_label(text):
    label1= QLabel(text)
    label1.setStyleSheet('font-size:60px;')

    return label1


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    
    #Define o icone
    icon = QIcon(str(ICON_PATH))
    
    window.setWindowIcon(icon)

    window.addWidgetToVLayout(temp_label('Teste 1'))

    #Define um tamanho Fixo da janela
    window.adjustFixedSize()

    window.show()

    app.exec()