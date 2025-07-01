# O básico sobre Signal e Slots (eventos e documentação)
import sys

from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow,
                               QPushButton, QWidget)


class MyWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        #Botão 1
        self.botao1 = QPushButton('Texto do botão')
        self.botao1.setStyleSheet('font-size: 80px;')
        self.botao1.clicked.connect(self.outro_slot)  



        self.central_widget = QWidget()

        self.setCentralWidget(self.central_widget)
        self.setWindowTitle('Minha janela bonita')


        #Botão 2
        self.botao2 = QPushButton('Botão 2')
        self.botao2.setStyleSheet('font-size: 40px;')

        #Botão 3
        self.botao3 = QPushButton('Botão 3')
        self.botao3.setStyleSheet('font-size: 40px;')

        #Grid
        self.grid_layout = QGridLayout()
        self.central_widget.setLayout(self.grid_layout)

        self.grid_layout.addWidget(self.botao1, 1, 1, 1, 1)
        self.grid_layout.addWidget(self.botao2, 1, 2, 1, 1)
        self.grid_layout.addWidget(self.botao3, 3, 1, 1, 2)


        # statusBar
        self.status_bar = self.statusBar()
        self.status_bar.showMessage('Mostrar mensagem na barra')

        # menuBar
        self.menu = self.menuBar()
        self.primeiro_menu = self.menu.addMenu('Primeiro menu')
        self.primeira_acao = self.primeiro_menu.addAction('Primeira ação')
        self.primeira_acao.triggered.connect(self.slot_example)  

        self.segunda_action = self.primeiro_menu.addAction('Segunda ação')
        self.segunda_action.setCheckable(True)
        self.segunda_action.toggled.connect(self.outro_slot)  
        self.segunda_action.hovered.connect(self.outro_slot) 


    @Slot()
    def slot_example(self):
        self.status_bar.showMessage('O meu slot foi executado')


    @Slot()
    def outro_slot(self):
        print('Está marcado?', self.segunda_action.isChecked())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec()  # O loop da aplicação







