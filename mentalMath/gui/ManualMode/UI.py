from . import handler
import guiTools
import winsound
import PyQt6.QtWidgets as qt
import PyQt6.QtCore as qt2
import PyQt6.QtGui as qt1
from PyQt6 import QtTextToSpeech
enjen=QtTextToSpeech.QTextToSpeech()
class UI(qt.QDialog):
    def __init__(self,p,submitDict):
        super().__init__(p)
        self.submitDict=submitDict
        self.result=0
        self.correctAnswers=0
        self.wrongAnswers=0
        self.questionCount=submitDict["questions_count"]
        self.questionSolved=0
        self.setWindowTitle(_("Math setion"))
        layout=qt.QVBoxLayout(self)
        self.timer=qt2.QTimer(self)
        # Time label
        self.timeLabel=qt.QLabel()
        self.timeLabel.setFocusPolicy(qt2.Qt.FocusPolicy.StrongFocus)
        self.timeLabel.setVisible(self.submitDict["time_limit_enabled"])
        layout.addWidget(self.timeLabel)
        self.equation=guiTools.QReadOnlyTextEdit()
        self.equation.setAccessibleName(_("Equation"))
        layout.addWidget(self.equation)
        self.answer=qt.QLineEdit()
        self.answer.setPlaceholderText(_("Type your answer"))
        self.answer.setAccessibleName(_("Type your answer"))
        self.answer.setAccessibleDescription(_("Press enter to submit"))
        self.answer.setFocus()
        self.answer.textChanged.connect(self.answerTextHandler)
        self.answer.returnPressed.connect(self.onSubmit)
        layout.addWidget(self.answer)
        qt1.QShortcut("escape",self)
        self.getQuestion()
        qt1.QShortcut("f2",self).activated.connect(lambda:enjen.say(self.equation.toPlainText()))
    def getQuestion(self):
        if self.questionCount==self.questionSolved:
            self.close()
        self.answer.setText("")
        operations=[]
        level=self.submitDict["level"]
        if self.submitDict["addition"]:
            operations.append("+")
        if self.submitDict["subtraction"]:
            operations.append("-")
        if self.submitDict["multiplication"]:
            operations.append("*")
        if self.submitDict["division"]:
            operations.append("/")
        equation,result=handler.number2Equation(level,operations)
        self.equation.setText(equation)
        self.result=result
        enjen.say(equation)
        self.questionSolved+=1
    def onSubmit(self):
        try:
            if self.result==int(self.answer.text()):
                winsound.PlaySound("data/sounds/1.wav",1)
                self.correctAnswers+=1
            else:
                winsound.PlaySound("data/sounds/2.wav",1)
                self.wrongAnswers+=1
        except Exception as e:
            print(e)
            winsound.PlaySound("data/sounds/2.wav",1)
            self.wrongAnswers+=1
        self.getQuestion()
    def answerTextHandler(self,text):
        try:
            if not text[-1].isdigit():
                self.answer.setText(text[:-2])
        except:
            pass