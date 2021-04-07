import socket

sock = socket.socket()
port = input("Введите порт:")
if port == '':
    port = 9090
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('', int(port)))

while True:
    print("Слушаем порт", int(port))
    sock.listen(1)

    try:
        conn, addr = sock.accept()
    except KeyboardInterrupt as k:
        print(k)
        print("Остановка программы!")
        exit()

    print('Соединение установлено:', addr[1])

    while True:

        try:
            data = conn.recv(1024).decode("utf8")
        except ConnectionResetError as e:
            print(e)
            print("Потеряно соединение с клиентом!")
            exit()
        except KeyboardInterrupt as k:
            print(k)
            print("Остановка программы!")
            print("Потеряно соединение с клиентом!")
            exit()

        if not data:
            print("Конец связи!")
            break

        if "sstop" in data:
            break
        conn.send(data.upper().encode())

    if "sstop" in data:
        break

conn.close()
