from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# # 初始化数据库连接:
# engine = create_engine('mysql+pymysql://root:xucheng225917@localhost:3306/python_test', encoding="utf-8", echo=True)
# 创建DBSession类型:
# DBSession = sessionmaker(bind=engine)
# 创建session对象:
# session = DBSession()


class ResposeModel(object):

    code: int
    message: str

    def __init__(self, code: int, message: str, data):
        self.code = code
        self.message = message
        if data is not None:
            self.data = data


