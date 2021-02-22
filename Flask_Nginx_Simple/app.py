from flask import Flask
import sys
import os

app1 = Flask(__name__)

@app1.route('/')
def function():
    return f'Response from {os.getpid()}'

if __name__ == "__main__":
    port = sys.argv[1]
    app1.run(debug=True, host='0.0.0.0', port=port)