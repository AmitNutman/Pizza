#https://github.com/AmitNutman/Pizza

import  socket


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server.bind(("0.0.0.0", 1002))
server.listen()

while True:
    client, addr = server.accept()
    order = client.recv(1024).decode()

    print(order)

    client.send("READY\n".encode())

    client.close()