# This CODE is without using SESSION
# Rather than we pass the DATA as an args to another request

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for


app = Flask(__name__)


# Route without Session
@app.route('/')
def home():
    return render_template("index.html")

# Route without Session
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # We can access values from form  in below two ways #
        userName = request.form.get('username')
        userName1 = request.form['username']

        return redirect(url_for('user', username=userName))
    else:
        return render_template('login.html')

# Route without Session - Thus passing Data as an args
@app.route('/user')
def user():
    return f"Hello <h1>{ request.args.get('username') }</h1>"


if __name__ == "__main__":
    app.run(debug=True)
