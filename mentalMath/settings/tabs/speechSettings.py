from settings import settings_handler,app
import PyQt6.QtWidgets as qt
import PyQt6.QtGui as qt1
from PyQt6.QtCore import Qt
class speechSettings(qt.QWidget):
    def __init__(self,p):
        super().__init__()
        layout=qt.QVBoxLayout(self)
        self.disableEntrnalSpeech=qt.QCheckBox(_("Disable enternal speech"))
        self.disableEntrnalSpeech.setChecked(p.cbts(settings_handler.get("speech","disable")))
        layout.addWidget(self.disableEntrnalSpeech)