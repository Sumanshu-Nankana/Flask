from flask import Flask
from flask import escape

app = Flask(__name__)

@app.route('/')
def function1():
    # This will display
    return "Hello Normal Function"

@app.route('/2')
def function2():
    # This will NOT display
    return "<Hello Normal Function"

@app.route('/3')
def function3():
    # This will display
    return "Hello Normal Function>"

@app.route('/4')
def function4():
    # This will display
    return "& Hello Normal Function"

@app.route('/5')
def function5():
    # This will display
    return "Hello Normal Function &"

@app.route('/6')
def function6():
    # This will automatically changed to copyright symbol
    return "&copy Hello Normal Function"

@app.route('/7')
def function7():
    # This will NOT changed to copyright symbol
    return escape("&copy Hello Normal Function")

@app.route('/8')
def function8():
    # This will changed to BOLD
    return "<h1> Hello Normal Function <h1>"

@app.route('/9')
def function9():
    # This will NOT changed to BOLD
    return escape("<h1> Hello Normal Function <h1>")

@app.route('/10')
def function10():
    return "<Hello Without Escape Function>"

@app.route('/11')
def function11():
    return escape("<Hello With Escape Function>")

if __name__ == "__main__":
    app.run(debug=True)