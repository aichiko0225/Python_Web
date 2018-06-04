import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 2000

s.bind((host, port))

while True:
    print('before listen')
    s.listen(5)
    print('before accept')
    connection, address = s.accept()

    buffer_size = 1024
    r = b''
    while True:
        request = connection.recv(buffer_size)
        r += request
        if len(request) < buffer_size:
            break

    ip, port = s.getsockname()
    # header = request.header
    # print('header === %' % header) 
    print('ip and request === {} {}'.format(address, request.decode('utf-8')))

    response = b' HTTP/1.1\r\n  200 ash \r\n\r\n<h1>hello wolrd!<h1/>'
    connection.sendall(response)
    connection.close()
