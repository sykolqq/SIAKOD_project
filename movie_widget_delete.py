from PyQt5.QtWidgets import QWidget, QPushButton

from ui.ui_movie_widget_delete import Ui_MovieWidget

from Movie import Movie


class MovieWidgetDelete(QWidget):
    def __init__(self, quiz_list: list,  btn_start_quiz: QPushButton, movie_widgets_for_quiz_layout, movie: Movie, parent=None):
        # TODO: добавить поле, которое будет обладать всеми полями фильма
        # "Приклеивание" внешних элементов приложения
        self.quiz_list = quiz_list
        self.btn_start_quiz = btn_start_quiz
        self.movie_widgets_for_quiz_layout = movie_widgets_for_quiz_layout

        # Основные элементы
        super(MovieWidgetDelete, self).__init__(parent)
        self.ui = Ui_MovieWidget()
        self.ui.setupUi(self)
        self.movie = movie

        self.ui.groupBox.setTitle(movie.title)
        # Жанры
        self.ui.label_genres.setText("Жанры: " + ', '.join(movie.director))
        # Директор (надо исправить)
        self.ui.label_director.setText("Директор: " + "NaN")
        # self.ui.label_director.setText("Директор: " + movie.rating)
        # Регион
        self.ui.label_region.setText("Страна: " + movie.region)
        # Рейтинг
        self.ui.label_rating.setText("Рейтинг: " + str(movie.genres))

        self.ui.btn_delete_from_quiz.clicked.connect(self.delete_from_quiz)

    def delete_from_quiz(self):
        # TODO: удалять не название фильма, а все данные про этот фильм
        index = self.quiz_list.index(self.movie)
        self.quiz_list.remove(self.movie)

        # Удаление элемента со страницы
        item = self.movie_widgets_for_quiz_layout.takeAt(index)
        item.widget().deleteLater()

        # Деактивация кнопки "Начать опрос", если количество элементов в списке меньше 2
        if self.btn_start_quiz.isEnabled():
            if len(self.quiz_list) < 2:
                self.btn_start_quiz.setStyleSheet("color: rgb(100, 100, 100)")
                self.btn_start_quiz.setEnabled(False)
