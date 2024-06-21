import sys  # sys нужен для передачи argv в QApplication
import time
import algorithm  # файл с алгоритмом

from PyQt5 import QtWidgets

import ui.ui_main_window  # Это наш конвертированный файл дизайна

from movie_widget import MovieWidget
from widget_choose_count_of_members import WidgetCountOfMembers
from widget_quiz_round import WidgetQuizRound
from widget_page_results import WidgetPageResults
from movie_widget_results import MovieWidgetResults

import sqlite3
import json

from Movie import Movie
from socket import *

# Настройки клиента
IP = '127.0.0.1'
PORT = 65432
CHUNK_SIZE = 4096

client = socket(AF_INET, SOCK_STREAM)
client.connect((IP, PORT))


class Window(QtWidgets.QMainWindow, ui.ui_main_window.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.main_window()

    # Этот метод нужен для того, чтобы была возможность вернуться к начальному окну после окончания опроса
    def main_window(self):
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

        # Стили
        self.btn_start_quiz.setStyleSheet("color: rgb(100, 100, 100)")

        # Создание списка для опроса
        self.quiz_list = []
        self.count_of_rounds = len(self.quiz_list)

        # Создание переменной для хранения количества участников (понадобится потом)
        self.count_of_members = 0

        # Подключение действий к кнопкам
        self.btn_search.clicked.connect(self.search)
        self.btn_delete.clicked.connect(self.delete_text_in_search_label)
        self.btn_start_quiz.clicked.connect(self.go_to_count_members_page)

    def search(self):
        search_information = self.label_search.text()
        # TODO: search_information изменить и передавать в в метод add_movie_widget
        if search_information != "":
            self.clear_search_scroll_area()
            if len(search_information) > 30:
                search_information = search_information[:30] + "..."
            self.add_movie_widget(search_information)

    def delete_text_in_search_label(self):
        self.label_search.setText("")

    def add_movie_widget(self, search_information):
        client.send(search_information.encode('utf-8'))

        data = b''
        while True:
            chunk = client.recv(CHUNK_SIZE)
            if b'END_OF_DATA' in chunk:
                break
            data += chunk

        search_result = json.loads(data.decode('utf-8'))

        for movie in search_result:
            if movie[1] not in self.quiz_list:
                self.search_movie_widgets_layout.addWidget(
                    MovieWidget(self.quiz_list, self.btn_start_quiz, self.movie_widgets_for_quiz_layout,
                                Movie(movie[0], movie[1], movie[2], movie[3].split(","), movie[4], movie[5])))

        # Если не нашлось ни одного фильма
        if self.search_movie_widgets_layout.count() == 0:
            label_no_movie = QtWidgets.QLabel("Фильм с таким названием не найден")
            label_no_movie.setStyleSheet("color: rgb(150, 150, 150);")
            self.search_movie_widgets_layout.addWidget(label_no_movie)

    def clear_search_scroll_area(self):
        while self.search_movie_widgets_layout.count() > 0:
            item = self.search_movie_widgets_layout.takeAt(0)
            item.widget().deleteLater()

    def clear_page(self):
        while self.horizontalLayout.count() > 0:
            item = self.horizontalLayout.takeAt(0)
            item.widget().deleteLater()

        # Пауза во время смены страниц (для ЭсТеТиКи)
        time.sleep(0.25)

    def go_to_count_members_page(self):
        self.clear_page()

        # Создание страницы с выбором количества участников
        widget_count_of_members = WidgetCountOfMembers()
        self.horizontalLayout.addWidget(widget_count_of_members)

        # Передача следующей функции количества участников при нажатии на кнопку
        widget_count_of_members.ui.btn_next_window.clicked.connect(lambda: self.go_to_quiz_window(
            widget_count_of_members.ui.spinBox_coun_of_members.value()
        ))

    def go_to_quiz_window(self, spinbox_value):
        self.clear_page()

        # Поля
        self.count_of_members = spinbox_value
        self.count_of_rounds = len(self.quiz_list) - 1

        self.current_member = 0

        self.list_with_tables_of_members = []

        self.start_quiz_rounds()

    def start_quiz_rounds(self):
        self.current_member += 1
        # Если все участники прошли опрос
        if self.current_member == self.count_of_members + 1:
            self.go_to_page_results()
            return

        # Создание таблицы для данного участника
        table_of_member = algorithm.AlgorithmUnits.create_table_for_member(len(self.quiz_list))
        self.current_member_table = table_of_member

        self.setWindowTitle("УЧАСТНИК " + str(self.current_member) + "/" + str(self.count_of_members))
        # Функция создает первую страницу, после чего функцией quiz_round создаются другие

        # Изменение полей раунда
        current_round = 1
        text_current_round = "РАУНД " + str(current_round) + "/" + str(self.count_of_rounds)

        # Создание добавление текущего раунда
        widget_quiz_round = WidgetQuizRound(text_current_round, self.quiz_list[current_round - 1],
                                            self.quiz_list[current_round])
        self.horizontalLayout.addWidget(widget_quiz_round)
        # С помощью лямбда-выражения передается значение раунда и значение со слайдера
        widget_quiz_round.ui.btn_next_round.clicked.connect(
            lambda: self.quiz_round(current_round + 1, widget_quiz_round.ui.slider.value()))

    def quiz_round(self, current_round: int, value_of_slider: int):
        self.clear_page()

        # Обработка значений слайдера
        if value_of_slider == 10:
            value_of_slider = 1
        else:
            value_of_slider = (11 - value_of_slider) if (value_of_slider < 10) else ((value_of_slider - 9) ** -1)
        # ____________________________

        # Заполняются значения матрицы a[i][j] и a[j][i]
        self.current_member_table[current_round - 2][current_round - 1] = value_of_slider
        self.current_member_table[current_round - 1][current_round - 2] = value_of_slider ** -1

        # Если для данного участника закончились фильмы для опроса (он завершил опрос)
        if current_round - 1 == self.count_of_rounds:
            self.list_with_tables_of_members.append(self.current_member_table)
            self.start_quiz_rounds()
            return
        # Изменение полей раунда
        text_current_round = "РАУНД " + str(current_round) + "/" + str(self.count_of_rounds)

        # Создание и добавление на экран текущего раунда
        widget_quiz_round = WidgetQuizRound(
            text_current_round, self.quiz_list[current_round - 1], self.quiz_list[current_round])
        self.horizontalLayout.addWidget(widget_quiz_round)

        widget_quiz_round.ui.btn_next_round.clicked.connect(
            lambda: self.quiz_round(current_round + 1, widget_quiz_round.ui.slider.value()))

    def go_to_page_results(self):
        self.clear_page()
        self.setWindowTitle("РЕЗУЛЬТАТЫ")

        # Создание таблицы, в которой учитываются результаты всех участников
        table = algorithm.AlgorithmUnits.create_table_with_all_members(self.list_with_tables_of_members)
        # Список, хранящий оценки фильмов (индексы одинаковы)
        list_of_results = algorithm.AlgorithmUnits.paired_comparison_algorithm(table)

        self.show_page_results(list_of_results)

    def show_page_results(self, list_with_results):
        self.clear_page()
        # Добавление виджета с результатами
        page_result = WidgetPageResults()
        self.horizontalLayout.addWidget(page_result)

        # Сортировка фильмов в соответствии с их коэффициентами
        algorithm.AlgorithmUnits.quicksort(list_with_results, self.quiz_list, 0, len(list_with_results))
        self.quiz_list.reverse()
        list_with_results.reverse()

        # Создание своего виджета для каждого фильма
        for i in range(len(list_with_results)):
            movie_widget = MovieWidgetResults(self.quiz_list[i])
            movie_widget.ui.label_place.setText(str(i + 1) + " место")
            movie_widget.ui.label_percents.setText(str(round(list_with_results[i] * 100, 2)) + "%")
            page_result.ui.layout_for_movie_widgets.addWidget(movie_widget)

        # Подключение к кнопке возврат к начальному экрану
        page_result.ui.btn_return.clicked.connect(self.main_window)


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = Window()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
