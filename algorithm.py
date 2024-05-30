class AlgorithmUnits:

    @staticmethod
    def paired_comparison_algorithm(table):
        if len(table) == 2:
            # Если таблица 2х2, то нет смысла выполнять 1 и 2 шаги
            return AlgorithmUnits.third_and_fourth_steps(table)

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
