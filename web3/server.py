import urllib


class Request(object):
    def __init__(self):
        self.method = 'GET'
        self.path = ''
        self.query = ''
        self.body = {}

    def form(self):
        body = urllib.parse.unquote(self.body)
        args = body.split('&')
        f = {}
        for arg in args:
            k, v = arg.split('=')
            f[k] = v
        return f
