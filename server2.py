import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(2)

msg = ''

while msg != "exit":
    conn, addr = sock.accept()
    print("Connected: ", addr)
    msg = ''
    while True:
        data = conn.recv(1024)
        if not data:
            break
        msg += data.decode()
        conn.send(data.upper())
        print(msg)


conn.close()