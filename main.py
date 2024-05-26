import sys  # sys нужен для передачи argv в QApplication
import time

from PyQt5 import QtWidgets

import ui_main_window  # Это наш конвертированный файл дизайна

from movie_widget import MovieWidget
from widget_choose_count_of_members import WidgetCountOfMembers
from widget_quiz_round import WidgetQuizRound


class Window(QtWidgets.QMainWindow, ui_main_window.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

        # Мой код

        # Стили
        self.btn_start_quiz.setStyleSheet("color: rgb(100, 100, 100)")

        # Создание списка для опроса
        self.quiz_list = []
        self.count_of_rounds = len(self.quiz_list)

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
                search_information = search_information[:30] + "..."
            self.add_movie_widget(search_information)

    def delete_text(self):
        self.label_search.setText("")

    def add_movie_widget(self, search_information):
        try:
            database = open("mini_database/title.akas.txt", encoding="utf-8")
            self.data = database.readlines()
        finally:
            database.close()

        for line in self.data:
            searching = line.find(search_information)
            movie_name = line.split('\t')[2]
            if searching != -1 and movie_name not in self.quiz_list:
                self.search_movie_widgets_layout.addWidget(MovieWidget(self.quiz_list, self.btn_start_quiz, movie_name))

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
        # TODO: добавить копирование layout'a перед удалением

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
        # Передача количества раундов
        self.count_of_rounds = len(self.quiz_list) - 1

        # Начало опроса
        # TODO: ПЕРЕДЕЛАТЬ ЭТУ ЧАСТЬ, ОНА НУЖНА ДЛЯ ПРИМЕРА
        self.table = QtWidgets.QTableWidget(self)
        self.table.setRowCount(len(self.quiz_list))
        self.table.setColumnCount(len(self.quiz_list))

        self.table.setHorizontalHeaderLabels(self.quiz_list)
        self.table.setVerticalHeaderLabels(self.quiz_list)

        self.table.setStyleSheet('''QTableView QTableCornerButton::section {
                                                background-color: #ccccff;
                                            }'''"QHeaderView::section { background-color: #ccccff; }")

        self.data = [[0] * len(self.quiz_list) for _ in range(len(self.quiz_list))]
        for i in range(len(self.quiz_list)):
            self.data[i][i] = 1

        self.quiz_rounds(1)
        # Конец опроса

    def quiz_rounds(self, current_round: int):
        # Если подошел к концу опрос
        if current_round - 1 == self.count_of_rounds:
            self.show_quiz_results()
            return

        # Удаление текущей страницы
        while self.horizontalLayout.count() > 0:
            item = self.horizontalLayout.takeAt(0)
            item.widget().deleteLater()
        # Немного ЭсТеТиКи
        time.sleep(0.25)

        # Изменение полей раунда
        text_current_round = "РАУНД " + str(current_round) + "/" + str(self.count_of_rounds)
        # Создание добавление текущего раунда
        widget_quiz_round = WidgetQuizRound(text_current_round, self.quiz_list.pop(0), self.quiz_list[0])
        self.horizontalLayout.addWidget(widget_quiz_round)

        widget_quiz_round.ui.btn_next_round.clicked.connect(lambda: self.quiz_rounds(current_round + 1))

    def show_quiz_results(self):
        while self.horizontalLayout.count() > 0:
            item = self.horizontalLayout.takeAt(0)
            item.widget().deleteLater()

        # TODO: сделать страницу с результатами
        # Пока тестовый вид
        # Заполнение таблицы данными
        for i, row in enumerate(self.data):
            for j, value in enumerate(row):
                item = QtWidgets.QTableWidgetItem(str(value))
                self.table.setItem(i, j, item)

        self.horizontalLayout.addWidget(self.table)


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = Window()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
