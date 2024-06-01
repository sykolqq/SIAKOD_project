class AlgorithmUnits:
    @staticmethod
    def create_table(count_of_members, len_quiz_list):
        pass

    @staticmethod
    def create_table_for_member(len_quiz_list):
        table = [[0] * len_quiz_list for _ in range(len_quiz_list)]
        for i in range(len_quiz_list):
            table[i][i] = 1

        return table

    @staticmethod
    def create_list_with_results():
        pass

    @staticmethod
    def create_table_with_all_members(list_with_tables_of_members):
        if len(list_with_tables_of_members) == 1:
            AlgorithmUnits.first_and_second_steps(list_with_tables_of_members[0])
            return list_with_tables_of_members[0]

        table3x = list_with_tables_of_members
        new_table = [[1] * len(table3x[0]) for _ in range(len(table3x[0]))]

        # Перемножение каждой ячейки таблиц между собой
        for i in range(len(table3x)):
            AlgorithmUnits.first_and_second_steps(table3x[i])
            for j in range(len(table3x[0])):
                for k in range(len(table3x[0][0])):
                    new_table[j][k] *= table3x[i][j][k]

        # Взятие корня n степени (n - количество участников)
        for i in range(len(new_table)):
            for j in range(len(new_table[0])):
                new_table[i][j] = new_table[i][j]**(1/len(table3x))
        return new_table

    @staticmethod
    def first_and_second_steps(table):
        if len(table) == 2:
            return
        n = len(table)

        # Первый шаг - обработка первой строки матрицы
        for i in range(2, n):
            sum_of_cells = (table[0][i - 1] * table[i - 1][i]) if (table[0][i - 1] * table[i - 1][i] < 11) else 11
            sum_of_cells_reverse = (sum_of_cells ** -1) if (sum_of_cells ** -1 < 11) else 11
            table[0][i] = round(sum_of_cells, 2)
            table[i][0] = round(sum_of_cells_reverse, 2)

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

    @staticmethod
    def paired_comparison_algorithm(table):
        # if len(table) == 2:
        #     # Если таблица 2х2, то нет смысла выполнять 1 и 2 шаги
        #     return AlgorithmUnits.third_and_fourth_steps(table)
        #
        # n = len(table)
        #
        # # Первый шаг - обработка первой строки матрицы
        # for i in range(2, n):
        #     sum_of_cells = (table[0][i - 1] * table[i - 1][i]) if (table[0][i - 1] * table[i - 1][i] < 11) else 11
        #     sum_of_cells_reverse = (sum_of_cells ** -1) if (sum_of_cells ** -1 < 11) else 11
        #     table[0][i] = round(sum_of_cells, 2)
        #     table[i][0] = round(sum_of_cells_reverse, 2)
        #
        # # Второй шаг - заполнение пустых ячеек матрицы парных сравнений
        # for i in range(n // 2 + 1):
        #     for j in range(n):
        #         if table[i][j] != 0:
        #             continue
        #         # Код валиден, так как на первом шаге все фильмы сравнились с первым
        #         cell_i_j = table[i][0] * table[0][j] if table[i][0] * table[0][j] < 11 else 11
        #         cell_j_i = table[j][0] * table[0][i] if table[j][0] * table[0][i] < 11 else 11
        #         table[i][j] = round(cell_i_j, 2)
        #         table[j][i] = round(cell_j_i, 2)

        return AlgorithmUnits.third_and_fourth_steps(table)

    @staticmethod
    def third_and_fourth_steps(table):
        n = len(table)

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
