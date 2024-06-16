from PyQt5.QtWidgets import QWidget, QPushButton, QLabel

from movie_widget_delete import MovieWidgetDelete
from ui.ui_movie_widget import Ui_MovieWidget

from Movie import Movie


class MovieWidget(QWidget):
    def __init__(self, quiz_list: list,  btn_start_quiz: QPushButton, movie_widgets_for_quiz_layout, movie: Movie, parent=None):
        # TODO: добавить поле, которое будет обладать всеми полями фильма
        # "Приклеивание" внешних элементов приложения
        self.quiz_list = quiz_list
        self.btn_start_quiz = btn_start_quiz
        self.movie_widgets_for_quiz_layout = movie_widgets_for_quiz_layout

        # Основные элементы
        super(MovieWidget, self).__init__(parent)
        self.movie = movie
        self.ui = Ui_MovieWidget()
        self.ui.setupUi(self)

        self.movie_title = movie.title
        self.genres = movie.genres

        self.ui.groupBox.setTitle(movie.title)
        self.ui.label_director.setText("Директор: хуйня")
        # self.ui.label_genres.setText(movie.genres)

        self.ui.btn_add_to_quiz.clicked.connect(self.add_to_quiz)

    def add_to_quiz(self):
        # TODO: добавлять не название фильма, а все данные про этот фильм
        self.quiz_list.append(self.movie_title)

        # Отрисовка данного фильма во второй вкладке
        self.movie_widgets_for_quiz_layout.addWidget(
             MovieWidgetDelete(self.quiz_list, self.btn_start_quiz, self.movie_widgets_for_quiz_layout, self.movie)
        )

        # Деактивация кнопки после того, как фильм добавили в quiz_list
        self.ui.btn_add_to_quiz.setEnabled(False)
        self.ui.btn_add_to_quiz.setStyleSheet("color: rgb(100, 100, 100);")

        # Активация кнопки "Начать опрос", если количество элементов в списке больше 1
        if not self.btn_start_quiz.isEnabled():
            if len(self.quiz_list) > 1:
                self.btn_start_quiz.setStyleSheet("color: #fff;\n"
                                                  "background-color: rgb(94, 91, 110);")
                self.btn_start_quiz.setEnabled(True)
