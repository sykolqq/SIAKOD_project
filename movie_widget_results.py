from PyQt5.QtWidgets import QWidget, QPushButton

from ui.ui_movie_widget_results import Ui_MovieWidget_results

from Movie import Movie


class MovieWidgetResults(QWidget):
    def __init__(self, movie_title, parent=None):
        # Основные элементы
        super(MovieWidgetResults, self).__init__(parent)
        self.ui = Ui_MovieWidget_results()
        self.ui.setupUi(self)

        self.ui.groupBox_movie.setTitle(movie_title)
