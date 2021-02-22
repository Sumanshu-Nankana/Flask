# install flask_ngrok on colab first
# !pip install flask_ngrok

from flask import Flask
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)

if __name__ == '__main__':
    app.run()