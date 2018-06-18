import socket


def log(*args, **kwargs):
    print('log', *args, **kwargs)


def route_index():
    header = 'HTTP/1.x 200 OK \r\nContent-Type: text/html\r\n'
    body = '<h1>hello world!!!</h1><img src="/dog.gif"/>'
    r = header + '\r\n' + body
    return r.encode(encoding='utf-8')


def route_image():
    with open('./web2/dog.gif', 'rb') as f:
        header = b'HTTP/1.x 200 OK\r\nContent-Type: image/gif\r\n\r\n'
        img = header + f.read()
        return img


def route_msg():
    def page(name):
        with open('./web2/' + name, encoding='utf-8') as s:
            return s.read()

    header = 'HTTP/1.x 200 OK \r\nContent-Type: text/html\r\n'
    # body = '<h1>hello world!!!</h1><img src="/dog.gif"/>'
    body = page('index.html')
    r = header + '\r\n' + body
    return r.encode(encoding='utf-8')


def error(code=404):
    e = {404: b'HTTP/1.1 404 NOT FOUND \r\n\r\n<h1>NOT FOUND</h1>'}
    return e.get(code, b'')


def response_for_path(path):
    r = {
        '/': route_index,
        '/dog.gif': route_image,
        '/msg': route_msg
    }
    response = r.get(path, error)
    return response()


def run(host='', port=3000):
    with socket.socket() as s:
        s.bind((host, port))
        while True:
            s.listen(5)
            connention, address = s.accept()
            request = connention.recv(1024)
            request = request.decode('utf-8')
            log('ip and request, {}\n{}'.format(address, request))
            try:
                path = request.split()[1]
                response = response_for_path(path)
                connention.send(response)
            except Exception as e:
                log('sss', e)
            connention.close()


if __name__ == '__main__':
    config = dict(host='', port=3000)
    run(**config)
