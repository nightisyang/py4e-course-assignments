import socket

# mysock is an object, makes doorway
# filehandle without any data yet
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# make connection, with a tupple ()
mysock.connect(('data.pr4e.org', 80))

# send command with a black line
# encode with utf-8
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    # up to 512 characters
    data = mysock.recv(512)

    # if no data recieve, break
    if len(data) < 1:
        break

    # decode utf-8
    print(data.decode())

# close connection
mysock.close()
