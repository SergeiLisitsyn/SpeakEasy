import mysql.connector

# Создаем соединение с базой данных. База данных должна быть уже запущена в контейнере.
cnx = mysql.connector.connect(user='user', password='user_password',
                              host='127.0.0.1',
                              database='my_database')

if cnx and cnx.is_connected():
    with cnx.cursor() as cursor:
        result = cursor.execute("SELECT * FROM my_table;") #тестовый запрос в тестовую таблицу
        rows = cursor.fetchall()
        for rows in rows:
            print(rows) # результат (1, 'sergei')
                                  # (2, 'john')
    cnx.close()

else:
    print("Could not connect")
cnx.close() # незабываем закрыть подключение