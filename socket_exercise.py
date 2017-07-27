import socket

so = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
so.connect(('data.pr4e.org', 80))
cmd = "GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n".encode()
so.send(cmd)

while True:
    data = so.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
so.close()