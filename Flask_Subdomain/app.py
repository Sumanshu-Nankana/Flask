from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Index Page\n"


@app.route('/apis', subdomain = 'api')
def function1():
    return "Test API Page\n"

if __name__ == "__main__":
    app.config['SERVER_NAME'] = 'sumanshu.com:5000'
    app.run(debug=True)
