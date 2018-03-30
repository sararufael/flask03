from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/loadform')
def login():
    return render_template("login.html")


@app.route('/processform', methods=['POST'])
def processform():
    user = request.form['user']
    return render_template("index.html", username=user)

if __name__ == '__main__':
    app.run()