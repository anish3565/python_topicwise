from flask import Flask
'''
It create an instance of flask class,
which will be your WSGI (Web Server Gateway Interface) application.
'''

## WSGI Application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to this Flask app, this is first page. Cool name"

@app.route("/index")
def indexPage():
    return "Welcome to the index page."

if __name__=="__main__":
    app.run(debug=True)