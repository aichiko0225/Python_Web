from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

# 创建对象的基类:
Base = declarative_base()


class User(Base):
    """
    定义User对象:
    """
    # 表的名字:
    __tablename__ = "auth_user"

    # 表的结构:
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(length=30), unique=True)
    password = Column(String(length=128))
    # addresses = relationship("Address", order_by=Address.id, back_populates="user")

    def __repr__(self):
        return "<User(name='%s', password='%s')>" % (self.username, self.password)
