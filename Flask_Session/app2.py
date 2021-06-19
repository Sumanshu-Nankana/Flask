# This Code is to Store SESSION at SERVER-SIDE
# and in FILESYSTEM

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session
from flask_session import Session


app = Flask(__name__)

app.config['SECRET_KEY'] = "mysecretkey"

# one folder will be created with name flask_session 
# and in that  Session ID's will be STORED
app.config['SESSION_TYPE'] = "filesystem"
Session(app)


# Using Server Side Session
@app.route('/index1')
def index1():
	if session.get('name'):
		return render_template('index1.html')
	return redirect(url_for('login1'))

# Using Server Side Session
@app.route('/login1', methods=['GET', 'POST'])
def login1():
	if request.method == 'POST':
		session['name'] = request.form.get('username')
		return redirect(url_for('index1'))
	return render_template('login1.html')

# Using Server Side Session
@app.route('/logout')
def logout():
	session['name'] = None
	return redirect(url_for('index1'))

if __name__ == "__main__":
    app.run(debug=True)
