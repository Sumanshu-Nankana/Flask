from flask import Flask
import os

app1 = Flask(__name__)

@app1.route('/')
def function():
    return f'Response from App1'

if __name__ == "__main__":
    app1.run(debug=True, host='0.0.0.0')