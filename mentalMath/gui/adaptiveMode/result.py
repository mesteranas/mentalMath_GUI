import guiTools
import PyQt6.QtWidgets as qt
import PyQt6.QtCore as qt2
import PyQt6.QtGui as qt1


class Result(qt.QDialog):
    def __init__(
        self,
        p,
        questionTimes: list,
        correct: int,
        encorrect: int,
        wrongAnswerExplaining:str,
        level:int
    ):
        super().__init__(p)

        self.questionsCount = correct + encorrect

        self.setWindowTitle(_("Test result"))
        self.setWindowFlag(
            qt2.Qt.WindowType.WindowContextHelpButtonHint,
            False
        )

        self.resize(500, 350)

        layout = qt.QVBoxLayout(self)

        # Wrong answers
        self.wrongAnswers=guiTools.QReadOnlyTextEdit()
        self.wrongAnswers.setText(wrongAnswerExplaining)
        self.wrongAnswers.setAccessibleName(_("Wrong answers"))
        layout.addWidget(self.wrongAnswers)

        # Results list
        self.resultList = qt.QListWidget()
        self.resultList.setAccessibleName(
            _("Test statistics")
        )

        layout.addWidget(self.resultList)
        # Your current level
        self.resultList.addItem(_("Current level:{}").format(level))
        # Correct answers
        self.resultList.addItem(
            _("You answered {} out of {} questions correctly").format(
                correct,
                self.questionsCount,
            )
        )

        # Accuracy
        accuracy = (
            (correct / self.questionsCount) * 100
            if self.questionsCount
            else 0
        )

        self.resultList.addItem(
            _("Accuracy percentage: {:.2f}%").format(
                accuracy
            )
        )

        # Average time
        self.averageTime = (
            sum(questionTimes) / len(questionTimes)
            if questionTimes
            else 0
        )

        self.resultList.addItem(
            _("Average answer time: {:.2f} seconds").format(
                self.averageTime
            )
        )

        # Buttons
        buttonLayout = qt.QHBoxLayout()
        layout.addLayout(buttonLayout)

        buttonLayout.addStretch()

        self.closeButton = qt.QPushButton(
            _("Close")
        )

        self.closeButton.setDefault(True)
        self.closeButton.clicked.connect(
            self.accept
        )

        buttonLayout.addWidget(
            self.closeButton
        )

        self.resultList.setFocus()