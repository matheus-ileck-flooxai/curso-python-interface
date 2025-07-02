from typing import TYPE_CHECKING
from PySide6.QtWidgets import QPushButton, QGridLayout
from PySide6.QtCore import Slot
from variables import MEDIUM_FONT_SIZE
from utils import isNumOrDot, isEmpty, isValidNumber

if TYPE_CHECKING:
    from display import Display
    from info import Info


class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.configStyle()

    def configStyle(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(75, 75)



class ButtonsGrid(QGridLayout):
    def __init__(self, display: 'Display', info: 'Info',*args, **kwargs):
        super().__init__(*args,**kwargs)

        self._grid_mask = [
            ['C', '<', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['', '0', '.', '='],
        ]
        self.display = display
        self.info = info
        self.info.setText('Sua conta')
        self._equation = ''
        self._makegrid()

    @property
    def equation(self):
        return self._equation
    
    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)


    def _makegrid(self):
        for row_number, row_data in enumerate(self._grid_mask):
            for column_number, button_text in enumerate(row_data):
                button = Button(button_text)
                
                if not isNumOrDot(button_text) and not isEmpty(button_text):
                    button.setProperty('cssClass', 'specialButton')
                    self._configSpecialButton(button)     

                self.addWidget(button, row_number, column_number)
                slot = self._makeSlot(self._insertButtonTextToDisplay, button)
                self._connectButtonClicked(button, slot)


    def _connectButtonClicked(self, button, slot):
        button.clicked.connect(slot)  


    def _configSpecialButton(self, button):
        text = button.text()

        if text == 'C':
            self._connectButtonClicked(button, self._clear)


    def _makeSlot(self, func, *args, **kwargs):
        @Slot(bool)
        def realSlot(_):
            func(*args, **kwargs)
        return realSlot

    def _insertButtonTextToDisplay(self, button):
        buttonText = button.text()
        newDisplayValue = self.display.text() + buttonText

        if not isValidNumber(newDisplayValue):
            return
        
        self.display.insert(buttonText)

    def _clear(self):
        self.display.clear()