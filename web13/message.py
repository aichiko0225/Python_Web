from flask import Flask, redirect, render_template, request
import time
import logging

print(Flask)
print('233')

logging.basicConfig(level=logging.INFO)
app = Flask(__name__)

messageList = []

# 用 log 函数把所有输出写入到文件，这样就能很方便地掌控全局了
# 即便你关掉程序，也能再次打开来查看，这就是个时光机


def log(*args, **kwargs):
    format = '%Y/%m/%d %H:%M:%S'
    value = time.localtime(int(time.time()))
    dt = time.strftime(format, value)
    with open('./web13/log.txt', 'a', encoding='utf-8') as f:
        # 通过 file 参数可以把输出写入到文件 f 中
        # 需要注意的是 **kwargs 必须是最后一个参数
        print(dt, *args, file=f, **kwargs)


@app.route('/')
def hello():
    return render_template('hello.html')


@app.route('/message', methods=['GET'])
def message():
    log('请求方法', request.method)
    form = request.form
    content = {
        'content': form.get('msg', '')
    }
    messageList.append(content)
    log(content)
    return render_template('message_index.html', messages=messageList)


@app.route('/message/add', methods=['POST'])
def addMessage():
    # 打印请求的方法 GET 或者 POST
    log('message_add 请求方法', request.method)

    # request.form 是 flask 保存 POST 请求的表单数据的属性
    log('request, POST 的 form 表单数据', request.form)
    # 把数据生成一个 dict 存到 message_list 中去
    msg = {
        'content': request.form.get('msg_post', ''),
    }
    messageList.append(msg)
    # 这和我们写过的函数是一样的
    return redirect('/message')


# render_template('sss')
if __name__ == "__main__":
    config = dict(debug=True, host='localhost', port=5000)
    app.run(**config)
