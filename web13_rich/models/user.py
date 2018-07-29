from models import Model
import hashlib
from models.todo import Todo


class User(Model):
    """
    User 是一个保存用户数据的 model
    现在只有两个属性 username 和 password
    """

    def __init__(self, form: dict):
        self.id = form.get('id', None)
        self.username = form.get('username', '')
        self.password = form.get('password', '')

    def salted_password(self, password, salt='$!@><?>HUI&DWQa`'):
        def sha256(ascii_str: str):
            return hashlib.sha256(ascii_str.encode('ascii')).hexdigest()
        hash1 = sha256(password)
        hash2 = sha256(hash1 + salt)
        return hash2

    def hashed_password(self, password):
        # 用 ascii 编码转换成 bytes 对象
        p = password.encode('ascii')
        s = hashlib.sha256(p)
        # 返回摘要字符串
        return s.hexdigest()

    def validate_register(self):
        pwd = self.password
        self.password = self.salted_password(pwd)
        if User.find_by(username=self.username) is None:
            self.save()
            return self
        else:
            return None

    def validate_login(self):
        u = User.find_by(username=self.username)
        if u is not None:
            return u.password == self.salted_password(self.password)
        else:
            return False

    def todos(self):
        # 列表推倒和过滤
        # return [t for t in Todo.all() if t.user_id == self.id]
        ts = []
        for t in Todo.all():
            if t.user_id == self.id:
                ts.append(t)
        return ts
        
