import guiTools,gui
import PyQt6.QtWidgets as qt
import PyQt6.QtCore as qt2
import PyQt6.QtGui as qt1

class PracticeMode(qt.QWidget):
    def __init__(self):
        super().__init__()
        layout = qt.QVBoxLayout(self)
        layout.setSpacing(15)

        # -------------------------
        # Level Selection
        # -------------------------
        levelLabel = qt.QLabel(_("Choose your level"))
        layout.addWidget(levelLabel)

        self.levelSelection = qt.QSlider(
            qt2.Qt.Orientation.Horizontal
        )
        self.levelSelection.setRange(1, 5)
        self.levelSelection.setValue(1)

        self.levelSelection.setAccessibleName(
            _("Level")
        )
        self.levelSelection.setAccessibleDescription(
            _("Choose a difficulty level from 1 to 5.")
        )

        layout.addWidget(self.levelSelection)

        # Questions count
        self.questionsCount=qt.QSlider(
            qt2.Qt.Orientation.Horizontal
        )
        self.questionsCount.setAccessibleName(
            _("Questions count")
        )
        self.questionsCount.setRange(10,1000)
        self.questionsCount.setValue(15)
        questionsCountLabel=qt.QLabel(
            _("Questions count")
        )
        layout.addWidget(questionsCountLabel)
        layout.addWidget(self.questionsCount)
        # -------------------------
        # Time Limit
        # -------------------------
        self.timeLimitCheckBox = qt.QCheckBox(
            _("Enable time limit")
        )

        self.timeLimitCheckBox.setAccessibleName(
            _("Enable time limit")
        )

        layout.addWidget(self.timeLimitCheckBox)

        timeLayout = qt.QHBoxLayout()

        timeLabel = qt.QLabel(
            _("Time in seconds:")
        )
        timeLayout.addWidget(timeLabel)

        self.timeSpinBox = qt.QSpinBox()
        self.timeSpinBox.setRange(5, 3600)
        self.timeSpinBox.setValue(60)
        self.timeSpinBox.setEnabled(False)

        self.timeSpinBox.setAccessibleName(
            _("Time limit in seconds")
        )

        self.timeSpinBox.setAccessibleDescription(
            _("Choose the time limit for each question.")
        )

        timeLayout.addWidget(self.timeSpinBox)

        layout.addLayout(timeLayout)

        self.timeLimitCheckBox.toggled.connect(
            self.timeSpinBox.setEnabled
        )

        # -------------------------
        # Operations
        # -------------------------
        operationsGroup = qt.QGroupBox(
            _("Allowed operations")
        )

        operationsLayout = qt.QVBoxLayout()

        self.additionCheckBox = qt.QCheckBox(
            _("Addition")
        )

        self.subtractionCheckBox = qt.QCheckBox(
            _("Subtraction")
        )

        self.multiplicationCheckBox = qt.QCheckBox(
            _("Multiplication")
        )

        self.divisionCheckBox = qt.QCheckBox(
            _("Division")
        )

        self.additionCheckBox.setChecked(True)
        self.subtractionCheckBox.setChecked(True)
        self.multiplicationCheckBox.setChecked(True)
        self.divisionCheckBox.setChecked(True)

        self.additionCheckBox.checkStateChanged.connect(self.submitButtonStates)
        self.subtractionCheckBox.checkStateChanged.connect(self.submitButtonStates)
        self.multiplicationCheckBox.checkStateChanged.connect(self.submitButtonStates)
        self.divisionCheckBox.checkStateChanged.connect(self.submitButtonStates)
        operationsLayout.addWidget(
            self.additionCheckBox
        )

        operationsLayout.addWidget(
            self.subtractionCheckBox
        )

        operationsLayout.addWidget(
            self.multiplicationCheckBox
        )

        operationsLayout.addWidget(
            self.divisionCheckBox
        )

        operationsGroup.setLayout(
            operationsLayout
        )

        layout.addWidget(
            operationsGroup
        )

        # -------------------------
        # Mixed Operations
        # -------------------------
        self.mixedOperationsCheckBox = qt.QCheckBox(
            _("Enable mixed operations")
        )

        self.mixedOperationsCheckBox.setAccessibleName(
            _("Enable mixed operations")
        )

        layout.addWidget(
            self.mixedOperationsCheckBox
        )

        # -------------------------
        # Submit Button
        # -------------------------
        self.submitButton = guiTools.QPushButton(
            _("Start Practice")
        )
        self.submitButton.setShortcut("ctrl+return")
        self.submitButton.setAccessibleDescription("CTRL+Enter")

        self.submitButton.setAccessibleName(
            _("Start practice")
        )

        self.submitButton.clicked.connect(
            self.submitConfiguration
        )

        layout.addWidget(
            self.submitButton
        )

        # -------------------------
        # Accessibility Styling
        # -------------------------
        self.setStyleSheet("""
            QWidget {
                font-size: 14pt;
            }

            QPushButton {
                min-height: 45px;
                padding: 8px;
            }

            QCheckBox {
                padding: 4px;
            }

            QSlider {
                min-height: 30px;
            }

            QSpinBox {
                min-height: 35px;
            }

            QPushButton:focus,
            QCheckBox:focus,
            QSpinBox:focus,
            QSlider:focus {
                border: 2px solid #0078d7;
            }
        """)

    def submitConfiguration(self):
        config = {
            "level": self.levelSelection.value(),
            "time_limit_enabled":
                self.timeLimitCheckBox.isChecked(),
            "time_limit":
                self.timeSpinBox.value(),
            "addition":
                self.additionCheckBox.isChecked(),
            "subtraction":
                self.subtractionCheckBox.isChecked(),
            "multiplication":
                self.multiplicationCheckBox.isChecked(),
            "division":
                self.divisionCheckBox.isChecked(),
            "mixed_operations":
                self.mixedOperationsCheckBox.isChecked(),
            "questions_count":
            self.questionsCount.value()
        }
        gui.practiceMode.UI(self,config).exec()
    def submitButtonStates(self,state):
        plus=not self.additionCheckBox.isChecked()
        mines=not self.subtractionCheckBox.isChecked()
        mulitbly=not self.multiplicationCheckBox.isChecked()
        devited=not self.divisionCheckBox.isChecked()
        if plus and mines and mulitbly and devited:
            self.submitButton.setDisabled(True)
        else:
            self.submitButton.setEnabled(True)