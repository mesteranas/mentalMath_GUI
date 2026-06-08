from ..practiceMode import handler
from .result import Result
import guiTools
import winsound
import PyQt6.QtWidgets as qt
import PyQt6.QtCore as qt2
import PyQt6.QtGui as qt1
class UI(qt.QDialog):
    def __init__(self,p,submitDict):
        super().__init__(p)
        self.enjen=guiTools.QTTS()
        self.submitDict=submitDict
        self.wrongAnswersExplaination=""
        self.questionTimes=[]
        self.alabsedTime=0
        self.result=0
        self.correctAnswers=0
        self.wrongAnswers=0
        self.setWindowTitle(_("Math setion"))
        layout=qt.QVBoxLayout(self)
        self.timer=qt2.QTimer(self)
        self.timer.timeout.connect(self.onTimeTregared)
        self.timer.start(1000)
        self.equation=guiTools.QReadOnlyTextEdit()
        self.equation.setAccessibleName(_("Equation"))
        layout.addWidget(self.equation)
        self.answer=qt.QLineEdit()
        self.answer.setPlaceholderText(_("Type your answer"))
        self.answer.setAccessibleName(_("Type your answer"))
        self.answer.setAccessibleDescription(_("Press enter to submit"))
        self.answer.setValidator(qt1.QDoubleValidator())
        self.answer.returnPressed.connect(self.onSubmit)
        layout.addWidget(self.answer)
        qt1.QShortcut("escape",self)
        self.getQuestion()
        qt1.QShortcut("f2",self).activated.connect(lambda:self.enjen.say(self.equation.toPlainText()))
        qt1.QShortcut("shift+f2",self).activated.connect(lambda:guiTools.speak(self.equation.toPlainText()))
        self.answer.setFocus()
    def getQuestion(self):
        self.answer.setText("")
        self.questionTimes.append(self.alabsedTime)
        self.alabsedTime=0
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
        if self.submitDict["mixed_operations"]:
            equation,result=handler.mixedEquation(level,operations)
        else:
            equation,result=handler.number2Equation(level,operations)
        self.equation.setText(equation)
        self.result=result
        self.enjen.speak(equation)
    def onSubmit(self):
        try:
            if self.result==int(self.answer.text()):
                winsound.PlaySound("data/sounds/1.wav",1)
                self.correctAnswers+=1
            else:
                winsound.PlaySound("data/sounds/2.wav",1)
                self.wrongAnswers+=1
                self.wrongAnswersExplaination+=_("{}\nYour answer : {}\nCorrect answer : {}\n").format(self.equation.toPlainText(),self.answer.text(),self.result)
        except Exception as e:
            print(e)
            winsound.PlaySound("data/sounds/2.wav",1)
            self.wrongAnswers+=1
            self.wrongAnswersExplaination+=_("{}\nYour answer : {}\nCorrect answer : {}\n").format(self.equation.toPlainText(),self.answer.text(),self.result)
        self.getQuestion()
    def onTimeTregared(self):
        self.alabsedTime+=1
    def closeEvent(self, a0):
        self.timer.stop()
        a0.accept()
        Result(self,self.questionTimes,self.correctAnswers,self.wrongAnswers,self.wrongAnswersExplaination).exec()
