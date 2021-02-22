from flask import Flask
import os

app2 = Flask(__name__)

@app2.route('/')
def function():
    return f'Response from APP2'

if __name__ == "__main__":
    app2.run(debug=True, host='0.0.0.0')