import socket
import ssl


def parsed_url(url: str):
    protocol = 'http'
    if url[:7] == 'http://':
        u = url.split('://')[1]
    elif url[:8] == 'https://':
        protocol = 'https'
        u = url.split('://')[1]
    else:
        u = url

    i = u.find('/')
    if i == -1:
        host = u
        path = '/'
    else:
        host = u[:i]
        path = u[i:]

    port_dict = {'http': 80, 'https': 443}

    port = port_dict[protocol]

    if ':' in host:
        h = host.split(':')
        host = h[0]
        port = int(h[1])

    return protocol, host, port, path


def test_parsed():
    http = 'http'
    https = 'https'
    host = 'g.cn'
    path = '/'
    test_items = [
        ('http://g.cn', (http, host, 80, path)),
        ('http://g.cn/', (http, host, 80, path)),
        ('http://g.cn:90', (http, host, 90, path)),
        ('http://g.cn:90/', (http, host, 90, path)),
        ('https://g.cn', (https, host, 443, path)),
        ('https://g.cn:233/', (https, host, 233, path)),
    ]

    for t in test_items:
        url, expected = t
        u = parsed_url(url)
        e = 'parsed_url ERROR , ({}) ({}) ({})'.format(url, u, expected)
        assert u == expected, e


def test():
    test_parsed()


def get(url: str):
    protocol, host, port, path = parsed_url(url)
    s = socket_by_protocol(protocol)
    s.connect((host, port))
    request = 'GET {} / HTTP/1.1\r\nhost:{}\r\nConnection: close\r\n\r\n'.format(
        host, path)
    encoding = 'utf-8'
    s.sendall(request.encode(encoding))
    response = response_by_socket(s)
    r = response.decode(encoding)

    status_code, headers, body = response_parsed(r)
    if status_code in [301, 302]:
        url = headers['Location']
        return get(url)
    return status_code, headers, body


def socket_by_protocol(protocol: str):
    if protocol == 'http':
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    elif protocol == 'https':
        s = ssl.wrap_socket(socket.socket())
    return s


def response_by_socket(s: socket):
    response = b''
    buffer_size = 1024
    while True:
        r = s.recv(buffer_size)
        if len(r) == 0:
            break
        response += r
    return response


def response_parsed(response: str):
    headers, body = response.split('\r\n', 1)
    h = headers.split('\r\n')
    # HTTP/ 1.1 200 OK
    status_code = h[0].split()[1]
    status_code = int(status_code)
    headers = {}
    for line in h[1:]:
        k, v = line.split(':')
        headers[k] = v
    return status_code, headers, body


def test_get():
    urls = ['http://movie.douban.com/top250', 'https://movie.douban.com/top250']
    for url in urls:
        status_code, headers, body = get(url)
        print(status_code, '\n', headers, '\n', body)


if __name__ == '__main__':
    test_get()
