from flask import Flask ,render_template, request, redirect, url_for
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello_2.html', person=name)


@app.route('/test')
def test():
    return render_template('hello.html')

@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user_name = request.form["name"]
        if user_name:
            return redirect(url_for("test"))

    return render_template("login.html")

        

if __name__ == '__main__':
    app.run()



