from PyQt5.QtWidgets import QWidget

import Movie
from ui.ui_quiz_round import Ui_WidgetQuizRound


class WidgetQuizRound(QWidget):
    def __init__(self, current_round: str, movie1: Movie, movie2: Movie, parent=None):
        super(WidgetQuizRound, self).__init__(parent)
        self.ui = Ui_WidgetQuizRound()
        self.ui.setupUi(self)

        self.ui.label_current_round.setText(current_round)
        # Первый groupBox
        self.ui.label_movie1_title.setText(movie1.title)
        self.ui.label_movie1_genre.setText("Жанры: " + ', '.join(movie1.director))
        self.ui.label_movie1_producer.setText("Директор: " + "NaN")
        # self.ui.label_director.setText("Директор: " + movie.rating)
        self.ui.label_movie1_region.setText("Страна: " + movie1.region)
        self.ui.label_movie1_rating.setText("Рейтинг: " + str(movie1.genres))

        # Второй groupBox
        self.ui.label_movie2_title.setText(movie2.title)
        self.ui.label_movie2_genre.setText("Жанры: " + ', '.join(movie2.director))
        self.ui.label_movie2_producer.setText("Директор: " + "NaN")
        # self.ui.label_director.setText("Директор: " + movie.rating)
        self.ui.label.setText("Страна: " + movie2.region)
        self.ui.label_movie2_rating.setText("Рейтинг: " + str(movie2.genres))
