# This Code is to Store SESSION at SERVER-SIDE
# and in DATABASE - SQLITE

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)

app.config['SECRET_KEY'] = "mysecretkey"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(minutes=1)

db = SQLAlchemy(app)
app.config['SESSION_SQLALCHEMY'] = db

# one table will be created with name 'sessions'  This is default Table Name
# and in that  Session ID's will be STORED
# if we want to store Session ID's in some different table
# we need to use app.config['SESSION_SQLALCHEMY_TABLE'] = TABLE_NAME

app.config['SESSION_TYPE'] = "sqlalchemy"  

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
	session.pop('name', None)
	return redirect(url_for('index1'))

if __name__ == "__main__":
    app.run(debug=True)
