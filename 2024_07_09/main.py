from flask import Flask,render_template


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html.jinja')

@app.route("/new")
def new():
    return render_template('index.html.jinja')

@app.route("/youbike")
def youbike():
    return render_template('index.html.jinja')

@app.route("/home")
def home():
    return render_template('index.html.jinja')

@app.route("/user/<username>")
def show_username(username):
    return f"<h1>{username}</h1>"

@app.route("/post/<int:post_id>")
def show_post(post_id):
    return f"<h1>{post_id}</h1>"