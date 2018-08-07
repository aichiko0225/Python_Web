from flask import request, Blueprint, jsonify
from models.user import User
from models import ResposeModel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# 创建一个 蓝图对象 并且路由定义在蓝图对象中
# 然后在 flask 主代码中「注册蓝图」来使用
# 第一个参数是蓝图的名字, 以后会有用(add函数里面就用到了)
# 第二个参数是套路
main = Blueprint('todo', __name__)


# # 初始化数据库连接:
engine = create_engine('mysql+pymysql://root:xucheng225917@localhost:3306/python_test', encoding="utf-8", echo=True)
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
# 创建session对象:
session = DBSession()


class UserInfo(object):
    nickname: str
    birthday: str

    @property
    def lalala(self):
        return "2222"

    def __init__(self, nickname: str, birthday: str):
        self.nickname = nickname
        self.birthday = birthday

    def __repr__(self):
        return "<UserInfo(nickname='%s', birthday='%s')>" % (self.nickname, self.birthday)


@main.route('/', methods=["POST"])
def json_index():
    # users = session.query(User).filter(User.id == 1000).all()
    # for user in users:
    #     print('type =', type(user))
    #     print('username =', user.username)
    # session.close()
    user = User(id=1000, username='ash', password='lalala')

    dic = {
        "id": user.id,
        "username": user.username,
        "password": user.password
    }
    response = ResposeModel(code=1, message="success", data=dic)
    # user_info = UserInfo('ash', '1989.09.17')
    return jsonify(response.__dict__)
    # return jsonify(json_list)


@main.route('/user', methods=['POST'])
def user():
    dic_arr: [dict] = []
    users = session.query(User).filter(User.id == 1000).all()
    print('users ====== ', users)
    for user in users:
        dic = {
            "id": user.id,
            "username": user.username,
            "password": user.password
        }
        dic_arr.append(dic)
    session.close()
    
    response = ResposeModel(code=1, message="success", data=dic)
    return jsonify(response.__dict__)
