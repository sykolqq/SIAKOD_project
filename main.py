import sys  # sys нужен для передачи argv в QApplication
import time

from PyQt5 import QtWidgets

import ui_main_window  # Это наш конвертированный файл дизайна
from movie_widget import MovieWidget
from widget_choose_count_of_members import WidgetCountOfMembers


class Window(QtWidgets.QMainWindow, ui_main_window.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

        # Мой код

        # Стили
        # Стиль кнопок у tab_widget
        # self.tab_search.setStyleSheet("""
        #         QTabBar {
        #             background-color: #777777;
        #             border: 2px solid #C4C4C3;
        #             border-bottom-color: #C2C7CB; /* same as the pane color */
        #             border-top-left-radius: 4px;
        #             border-top-right-radius: 4px;
        #             min-width: 8ex;
        #             padding: 2px;
        #         }
        #         """)
        self.btn_start_quiz.setStyleSheet("color: rgb(100, 100, 100)")

        # Создание списка для опроса
        self.quiz_list = []

        # Создание переменной для хранения количества участников (понадобится потом)
        self.count_of_members = 0

        # Подключение действий к кнопкам
        self.btn_search.clicked.connect(self.search)
        self.btn_delete.clicked.connect(self.delete_text)
        self.btn_start_quiz.clicked.connect(self.start_quiz)

    def search(self):
        self.clear_area()
        search_information = self.label_search.text()
        # TODO: search_information изменить и передавать в в метод add_movie_widget
        if search_information != "":
            if len(search_information) > 30:
                # TODO: Поменять на 62 или 50
                search_information = search_information[:30]
            self.add_movie_widget(search_information)

    def delete_text(self):
        self.label_search.setText("")

    def add_movie_widget(self, search_information):
        # TODO: вместо цикла найти по search_info фильмы (может быть меньше 5)
        for i in range(1, 6):
            movie_name = search_information + " " + str(i)
            # Проверка: есть ли данный фильм уже в quiz_list
            if movie_name in self.quiz_list:
                continue

            movie_widget = MovieWidget(self.quiz_list, self.btn_start_quiz,movie_name)
            self.search_movie_widgets_layout.addWidget(movie_widget)

        # Если не нашлось ни одного фильма
        if self.search_movie_widgets_layout.count() == 0:
            label_no_movie = QtWidgets.QLabel("Фильм с таким названием не найден")
            label_no_movie.setStyleSheet("color: rgb(150, 150, 150);")
            self.search_movie_widgets_layout.addWidget(label_no_movie)

    def clear_area(self):
        while self.search_movie_widgets_layout.count() > 0:
            item = self.search_movie_widgets_layout.takeAt(0)
            item.widget().deleteLater()

    def start_quiz(self):
        # Удаление основного окна
        while self.horizontalLayout.count() > 0:
            item = self.horizontalLayout.takeAt(0)
            item.widget().deleteLater()

        # Пауза во время смены страниц (для ЭсТеТиКи)
        time.sleep(0.25)

        # Переход на новую страницу
        widget_count_of_members = WidgetCountOfMembers()
        self.horizontalLayout.addWidget(widget_count_of_members)

        # Привязка кнопки из widget_count_of_members основному окну
        self.btn_next_window = widget_count_of_members.ui.btn_next_window
        self.btn_next_window.clicked.connect(lambda: self.go_to_next_window(widget_count_of_members))

    def go_to_next_window(self, widget_count_of_members: WidgetCountOfMembers):
        # Передача приложению количества участников
        self.count_of_members = widget_count_of_members.ui.spinBox_count_of_members.value()

        # Удаление текущей страницы
        while self.horizontalLayout.count() > 0:
            item = self.horizontalLayout.takeAt(0)
            item.widget().deleteLater()

        # Немного ЭсТеТиКи
        time.sleep(0.25)

        # TODO: продолжить


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = Window()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
