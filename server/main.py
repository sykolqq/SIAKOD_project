from socket import *
from threading import Thread

import json
import sqlite3


# Настройки сервера
IP = '127.0.0.1'
PORT = 65432
CHUNK_SIZE = 4096


def search_movies(search_information):
    # Подключение к БД
    db_title = sqlite3.connect("../mini_database/title.db")
    db_title_cursor = db_title.cursor()

    # Поиск по названию
    db_title_cursor.execute(f'''
            SELECT
                akas.titleId,
                akas.title,
                akas.region,
                basics.genres,
                crew.directors,
                ratings.averageRating
            FROM
                title_akas akas
            JOIN
                title_basics basics ON akas.titleId = basics.titleId,
                title_crew crew ON akas.titleId = crew.titleId,
                title_ratings ratings ON akas.titleId = ratings.titleId
            WHERE
                akas.title LIKE '%{search_information}%'
            ''')
    search_result = db_title_cursor.fetchall()

    # Закрыть подключенную БД
    db_title_cursor.close()
    db_title.close()

    # Возвращаем результат
    search_result = [list(row) for row in search_result]
    return search_result


class Server:
    def __init__(self, ip, port):
        print(f"Сервер инициализирован на {ip}:{port}")
        self.server = socket(AF_INET, SOCK_STREAM)
        self.server.bind((ip, port))
        self.server.listen(10)

    # Функция для запуска сервера
    def start_server(self):
        while True:
            conn, addr = self.server.accept()
            Thread(target=self.handle_client, args=(conn, addr,)).start()

    # Обработка каждого пользователя
    def handle_client(self, conn, addr):
        print(f"Новое подключение: {addr}")
        is_work = True

        while is_work:
            try:
                data = conn.recv(1024)
                if not data:
                    break

                client_data = data.decode('utf-8')

                if client_data == 'disconnect':
                    conn.close()
                    is_work = False
                else:
                    # conn.send(json.dumps(search_movies(client_data)).encode('utf-8'))
                    result = search_movies(client_data)
                    result_json = json.dumps(result)
                    result_bytes = result_json.encode('utf-8')

                    # Отправляем данные по частям
                    for i in range(0, len(result_bytes), CHUNK_SIZE):
                        chunk = result_bytes[i:i + CHUNK_SIZE]
                        conn.sendall(chunk)

                    # Уведомляем клиента об окончании передачи данных
                    conn.sendall(b'END_OF_DATA')

            except Exception as e:
                is_work = False


if __name__ == '__main__':
    server = Server(IP, PORT)
    server.start_server()
