from flask import Flask
import logging
from routes.todo import main as todo_routes
logging.basicConfig(level=logging.INFO)


app = Flask(__name__)
# 设置 secret_key 来使用 flask 自带的 session
# 这个字符串随便你设置什么内容都可以
app.secret_key = 'random string'

app.register_blueprint(todo_routes, url_prefix='/todo')

if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)
