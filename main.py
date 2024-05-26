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

            movie_widget = MovieWidget(self.quiz_list, self.btn_start_quiz, movie_name)
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

        self.start_quiz_rounds()
        # Конец опроса

    def start_quiz_rounds(self):
        while self.horizontalLayout.count() > 0:
            item = self.horizontalLayout.takeAt(0)
            item.widget().deleteLater()
        # Немного ЭсТеТиКи
        time.sleep(0.25)
        # Изменение полей раунда
        current_round = 1
        text_current_round = "РАУНД " + str(current_round) + "/" + str(self.count_of_rounds)

        # Создание добавление текущего раунда
        widget_quiz_round = WidgetQuizRound(text_current_round, self.quiz_list[current_round - 1],
                                            self.quiz_list[current_round])
        self.horizontalLayout.addWidget(widget_quiz_round)
        widget_quiz_round.ui.btn_next_round.clicked.connect(
            lambda: self.quiz_round(current_round + 1, widget_quiz_round.ui.slider.value()))

    def quiz_round(self, current_round: int, value_of_slider: int):
        while self.horizontalLayout.count() > 0:
            item = self.horizontalLayout.takeAt(0)
            item.widget().deleteLater()
        # Немного ЭсТеТиКи
        time.sleep(0.25)

        # Обработка значений слайдера
        if value_of_slider == 10:
            value_of_slider = 1
        else:
            value_of_slider = (11 - value_of_slider) if (value_of_slider < 10) else ((value_of_slider - 9) ** -1)

        self.data[current_round - 2][current_round - 1] = round(value_of_slider, 2)
        self.data[current_round - 1][current_round - 2] = round(value_of_slider ** -1, 2)

        if current_round - 1 == self.count_of_rounds:
            self.show_quiz_results()
            return
        # Изменение полей раунда
        text_current_round = "РАУНД " + str(current_round) + "/" + str(self.count_of_rounds)

        # Создание добавление текущего раунда
        widget_quiz_round = WidgetQuizRound(text_current_round, self.quiz_list[current_round - 1],
                                            self.quiz_list[current_round])
        self.horizontalLayout.addWidget(widget_quiz_round)
        widget_quiz_round.ui.btn_next_round.clicked.connect(
            lambda: self.quiz_round(current_round + 1, widget_quiz_round.ui.slider.value()))

    def show_quiz_results(self):
        # TODO: сделать страницу с результатами
        list_of_results = self.paired_comparison_algorithm()
        # Пока тестовый вид
        # Заполнение таблицы данными
        for i, row in enumerate(self.data):
            for j, value in enumerate(row):
                item = QtWidgets.QTableWidgetItem(str(value))
                self.table.setItem(i, j, item)

        self.horizontalLayout.addWidget(self.table)

        # Таблица с результатами
        table_of_results = QtWidgets.QTableWidget(self)
        table_of_results.setRowCount(len(self.quiz_list))
        table_of_results.setColumnCount(1)
        #
        table_of_results.setVerticalHeaderLabels(self.quiz_list)
        table_of_results.setHorizontalHeaderLabels(["Результат"])
        # table_of_results.setHorizontalHeaderLabels()

        table_of_results.setStyleSheet('''QTableView QTableCornerButton::section {
                                                        background-color: #ccccff;
                                                    }'''"QHeaderView::section { background-color: #ccccff; }")

        for i, value in enumerate(list_of_results):
            item = QtWidgets.QTableWidgetItem(str(value))
            table_of_results.setItem(i, 0, item)

        self.horizontalLayout.addWidget(table_of_results)

    def paired_comparison_algorithm(self):
        table = self.data
        if len(table) == 2:
            return

        n = len(table)

        # Первый шаг - обработка первой строки матрицы
        for i in range(2, n):
            sum_of_cells = (table[0][i - 1] * table[i - 1][i]) if (table[0][i - 1] * table[i - 1][i] < 11) else 11
            if sum_of_cells > 11:
                sum_of_cells = 11
            table[0][i] = round(sum_of_cells, 2)
            table[i][0] = round(sum_of_cells ** -1, 2)

        # Второй шаг - заполнение пустых ячеек матрицы парных сравнений
        for i in range(n // 2 + 1):
            for j in range(n):
                if table[i][j] != 0:
                    continue
                # Код валиден, так как на первом шаге все фильмы сравнились с первым
                cell_i_j = table[i][0] * table[0][j] if table[i][0] * table[0][j] < 11 else 11
                cell_j_i = table[j][0] * table[0][i] if table[j][0] * table[0][i] < 11 else 11
                table[i][j] = round(cell_i_j, 2)
                table[j][i] = round(cell_j_i, 2)

        # Третий шаг - нормализация данных
        list_of_row_multi = []
        sum_of_multiply = 0
        for i in range(n):
            multiply = 1
            for j in range(n):
                multiply *= table[i][j]
            multiply = multiply ** (1 / n)
            list_of_row_multi.append(multiply)
            sum_of_multiply += multiply

        # Четвертый шаг - результаты каждого фильма
        list_results = []
        for i in range(n):
            list_results.append(list_of_row_multi[i] / sum_of_multiply)

        # Округление результатов
        for i in range(n):
            list_results[i] = round(list_results[i], 2)
        return list_results


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = Window()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
