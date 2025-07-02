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
                
                self.addWidget(button, row_number, column_number)
                buttonSlot = self._makeButtonDisplaySlot(
                    self._insertButtonTextToDisplay,
                    button,
                )
                button.clicked.connect(buttonSlot)  # type: ignore

    def _makeButtonDisplaySlot(self, func, *args, **kwargs):
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