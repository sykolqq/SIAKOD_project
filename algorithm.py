class AlgorithmUnits:
    @staticmethod
    def create_table_for_member(len_quiz_list):
        table = [[0] * len_quiz_list for _ in range(len_quiz_list)]
        for i in range(len_quiz_list):
            table[i][i] = 1

        return table

    @staticmethod
    def create_table_with_all_members(list_with_tables_of_members):
        # Если участник был только один
        if len(list_with_tables_of_members) == 1:
            AlgorithmUnits.fill_the_table(list_with_tables_of_members[0])
            return list_with_tables_of_members[0]

        table3x = list_with_tables_of_members
        # Создание итоговой таблицы, в которой будут учитываться результаты всех участников
        new_table = [[1] * len(table3x[0]) for _ in range(len(table3x[0]))]

        # Перемножение каждой ячейки таблиц между собой
        #   table3x - трехмерный список, хранящий матрицы каждого участника
        for i in range(len(table3x)):
            # Заполнение таблицы текущего участника
            AlgorithmUnits.fill_the_table(table3x[i])
            for j in range(len(table3x[0])):
                for k in range(len(table3x[0][0])):
                    new_table[j][k] *= table3x[i][j][k]

        # Взятие корня n степени (n - количество участников)
        for i in range(len(new_table)):
            for j in range(len(new_table[0])):
                # Формула: n√(a1 * ... * an)
                new_table[i][j] = new_table[i][j] ** (1 / len(table3x))
        return new_table

    # Метод, который полностью заполняет таблицу значениями
    @staticmethod
    def fill_the_table(table):
        # Если матрица 2х2, то она и так заполнена
        if len(table) == 2:
            return
        n = len(table)

        # Первый шаг - заполнение первой строки матрицы
        for i in range(2, n):
            multi_of_cells = table[0][i - 1] * table[i - 1][i]
            multi_of_cells_reverse = multi_of_cells ** -1

            table[0][i] = AlgorithmUnits.return_rounded_value_of_element(multi_of_cells)
            table[i][0] = AlgorithmUnits.return_rounded_value_of_element(multi_of_cells_reverse)

        x = 0

        # Второй шаг - заполнение пустых ячеек матрицы парных сравнений
        for i in range(n):
            for j in range(n):
                # Если ячейка уже заполнена:
                if table[i][j] != 0:
                    continue
                # Код валиден, так как на первом шаге все фильмы сравнились с первым
                table[i][j] = table[i][0] * table[0][j]
                table[j][i] = table[j][0] * table[0][i]

    @staticmethod
    def return_rounded_value_of_element(multi_of_cells):
        if multi_of_cells > 11:
            return 11
        elif multi_of_cells < 0.09:
            return 0.09
        return multi_of_cells

    # Метод, уже работающий с финальной таблицей
    @staticmethod
    def paired_comparison_algorithm(table):
        n = len(table)

        # Третий шаг - нормализация данных
        list_of_row_multi = []
        sum_of_multiply = 0

        # Для каждой строки перемножаются значения этой строки и финальное значение возводится в степень 1/n, после
        #   чего это значение прибавляется к sum_of_multiply
        for i in range(n):
            multiply = 1
            for j in range(n):
                multiply *= table[i][j]
            multiply = multiply ** (1 / n)
            list_of_row_multi.append(multiply)
            sum_of_multiply += multiply
        # -------------------------------

        # Четвертый шаг - результаты каждого фильма
        list_results = []
        for i in range(n):
            # Формула (умножение_строки) / (сумма_умножений_строки)
            list_results.append(list_of_row_multi[i] / sum_of_multiply)

        # Округление результатов (нужно, так как у них 15 чисел после запятой)
        # for i in range(n):
        #     list_results[i] = round(list_results[i], 2)
        return list_results
