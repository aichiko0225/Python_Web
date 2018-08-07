from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey


# 创建对象的基类:
ModelBase = declarative_base()


class Address(ModelBase):
    """
    定义Address对象:
    """
    __tablename__ = "addresses"
    id = Column(Integer, primary_key=True, autoincrement=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('auth_user.id'))
    user = relationship("User", back_populates="addresses")

    def __repr__(self):
        return "<Address(email_address='%s')>" % self.email_address


class User(ModelBase):
    """
    定义User对象:
    """
    # 表的名字:
    __tablename__ = "auth_user"

    # 表的结构:
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(length=30), unique=True)
    password = Column(String(length=128))
    addresses = relationship("Address", order_by=Address.id, back_populates="user")

    def __repr__(self):
        return "<User(name='%s', password='%s')>" % (self.username, self.password)


# # 初始化数据库连接:
engine = create_engine('mysql+pymysql://root:xucheng225917@localhost:3306/python_test', encoding="utf-8", echo=True)
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
# 创建session对象:
session = DBSession()

if __name__ == "__main__":
    # 创建新User对象:
    # new_user = User(username='ash', password='xucheng')
    # 添加到session:
    # session.add(new_user)
    # 提交即保存到数据库:
    # session.commit()

    # users1 = session.query(User).filter_by(user_id=1000)
    # print(users1)
    # for user in users1:
    #     print('type =', type(user))
    #     print('username =', user.username)
    users = session.query(User).filter(User.id == 1000).all()
    for user in users:
        print('type =', type(user))
        print('username =', user.username)
        # print('addresses =', user.addresses)

        # jack = User(username='jack', password='gjffdd')
        # print(jack.addresses)
        # jack.addresses = [Address(email_address='jack@google.com')]
        # print(jack.addresses[0].user)
        # session.add(jack)
        # session.commit()

        jacks = session.query(User).filter_by(username='jack').all()
        for jack in jacks:
            print(jack)
            print(jack.addresses)
        print('=============================')
        for u, a in session.query(User, Address).filter(User.id == Address.user_id).filter(Address.email_address == 'jack@google.com').all():
            print(u)
            print(a)
    # 关闭session:
    session.close()


