from PyQt5.QtWidgets import QWidget

from ui.ui_quiz_round import Ui_WidgetQuizRound


class WidgetQuizRound(QWidget):
    def __init__(self, current_round: str, movie1_title: str, movie2_title: str, parent=None):
        super(WidgetQuizRound, self).__init__(parent)
        self.ui = Ui_WidgetQuizRound()
        self.ui.setupUi(self)

        self.ui.label_current_round.setText(current_round)
        self.ui.label_movie1_title.setText(movie1_title)
        self.ui.label_movie2_title.setText(movie2_title)
