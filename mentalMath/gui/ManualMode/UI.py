import guiTools
import PyQt6.QtWidgets as qt
import PyQt6.QtCore as qt2
import PyQt6.QtGui as qt1
from PyQt6 import QtTextToSpeech
enjen=QtTextToSpeech.QTextToSpeech()
class UI(qt.QDialog):
    def __init__(self,p,submitDict):
        super().__init__(p)
        self.submitDict=submitDict
        self.setWindowTitle(_("Math setion"))
        layout=qt.QVBoxLayout(self)