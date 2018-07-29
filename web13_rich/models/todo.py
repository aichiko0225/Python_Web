import time
from models import Model, load


class Todo(Model):
    @classmethod
    def new(cls, form):
        """
        创建并保存一个 todo 并且返回它
        Todo.new({'title': '吃饭'})
        :param form: 一个字典 包含了 todo 的数据
        :return: 创建的 todo 实例
        """
        # 下面一行相当于 t = Todo(form)
        t = cls(form)
        t.save()
        return t

    @classmethod
    def update(cls, id, form):
        t = cls.find(id)
        valid_names = [
            'title',
            'completed'
        ]
        for key in form:
            # 这里只应该更新我们想要更新的东西
            if key in valid_names:
                setattr(t, key, form[key])
        t.save()
        return t

    @classmethod
    def complete(cls, id, completed=True):
        """
        用法很方便
        Todo.complete(1)
        Todo.complete(2, False)
        """
        t = cls.find(id)
        t.completed = completed
        t.save()
        return t

    def __init__(self, form: dict):
        self.id = None
        self.title = form.get('title', '')
        # 下面的是默认的数据
        self.completed = False
        # ct ut 分别是 created_time  updated_time
        # 创建时间和 更新时间
        self.ct = int(time.time())
        self.ut = self.ct

    @classmethod
    def all(cls):
        """
        all 方法(类里面的函数叫方法)使用 load 函数得到所有的 models
        """
        path = cls.db_path()
        models = load(path)
        # 这里用了列表推导生成一个包含所有 实例 的 list
        # 因为这里是从 存储的数据文件 中加载所有的数据
        # 所以用 _new_from_dict 这个特殊的函数来初始化一个数据
        ms = []
        for m in models:
            m = cls._new_from_dict(m)
            if m.ct > 0:
                format = '%Y/%m/%d %H:%M:%S'
                value = time.localtime(m.ct)
                m.dt = time.strftime(format, value)
            ms.append(m)
        return ms

