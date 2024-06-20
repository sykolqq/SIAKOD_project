from PyQt5.QtWidgets import QWidget, QPushButton

from ui.ui_movie_widget_results import Ui_MovieWidget_results

from Movie import Movie


class MovieWidgetResults(QWidget):
    def __init__(self, movie: Movie, parent=None):
        # Основные элементы
        super(MovieWidgetResults, self).__init__(parent)
        self.ui = Ui_MovieWidget_results()
        self.ui.setupUi(self)

        self.ui.groupBox_movie.setTitle(movie.title)
        self.ui.label_genres.setText("Жанры: " + ', '.join(movie.director))
        self.ui.label_director.setText("Директор: " + "NaN")
        self.ui.label_region.setText("Страна: " + movie.region)
        self.ui.label_rating.setText("Рейтинг: " + str(movie.genres))
