from typing import Optional
import UniversalSpeech
from PyQt6.QtTextToSpeech import QTextToSpeech
STTS=UniversalSpeech.UniversalSpeech()
STTS.enable_native_speech(False)
def speak(text:str):
    STTS.say(text,True)
class QTTS(QTextToSpeech):
    def __init__(self, engine: Optional[str] = None, parent=None):
        super().__init__(engine, parent)
    def speak(self, msg: str) -> None:
        self.say(msg)