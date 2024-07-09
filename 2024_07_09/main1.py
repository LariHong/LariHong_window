from flask import Flask,url_for

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with  app.test_request_context():
    print("77777777777777777777777")

#當有request就執行
# url_for() 參數要放function名
# url_for() 主要是傳出一個網址
with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))