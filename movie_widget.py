from PyQt5.QtWidgets import QWidget, QPushButton

from ui.ui_movie_widget import Ui_MovieWidget


class MovieWidget(QWidget):
    def __init__(self, quiz_list: list, btn_start_quiz: QPushButton, movie_title: str, parent=None):
        # TODO: добавить поле, которое будет обладать всеми полями фильма
        # "Приклеивание" внешних элементов приложения
        self.quiz_list = quiz_list
        self.btn_start_quiz = btn_start_quiz

        # Основные элементы
        super(MovieWidget, self).__init__(parent)
        self.ui = Ui_MovieWidget()
        self.ui.setupUi(self)
        self.movie_title = movie_title
        self.ui.groupBox.setTitle(movie_title)
        self.ui.btn_add_to_quiz.clicked.connect(self.add_to_quiz)

    def add_to_quiz(self):
        # TODO: добавлять не название фильма, а все данные про этот фильм
        self.quiz_list.append(self.movie_title)

        # Деактивация кнопки после того, как фильм добавили в quiz_list
        self.ui.btn_add_to_quiz.setEnabled(False)
        self.ui.btn_add_to_quiz.setStyleSheet("color: rgb(100, 100, 100);")

        # Активация кнопки "Начать опрос", если количество элементов в списке больше 2
        if not self.btn_start_quiz.isEnabled():
            if len(self.quiz_list) > 1:
                self.btn_start_quiz.setStyleSheet("color: #FFFFFF")
                self.btn_start_quiz.setEnabled(True)