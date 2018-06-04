import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'g.cn'
port = 80

s.connect((host, port))


ip, port = s.getsockname()

print('ip and port === {} {}'.format(ip, port))

http_request = 'GET / HTTP/1.1\r\nhost:{}\r\n\r\n'.format(host)

request = http_request.encode('utf-8')

print(request)

s.send(request)

response = s.recv(1024)

responseStr = response.decode('utf-8')

print(responseStr)


"""
HTTP/1.1 301 Moved Permanently
Location: http://www.google.cn/
Date: Mon, 04 Jun 2018 01:44:19 GMT
Expires: Mon, 04 Jun 2018 01:44:19 GMT
Cache-Control: private, max-age=2592000
Content-Type: text/html; charset=UTF-8
Server: gws
Content-Length: 218
X-XSS-Protection: 1; mode=block
X-Frame-Options: SAMEORIGIN

<HTML><HEAD><meta http-equiv="content-type" content="text/html;charset=utf-8">
<TITLE>301 Moved</TITLE></HEAD><BODY>
<H1>301 Moved</H1>
The document has moved
<A HREF="http://www.google.cn/">here</A>.
</BODY></HTML>
"""
