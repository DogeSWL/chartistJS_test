from flask import redirect, render_template
from app import app

@app.route("/index")
def home():

    return render_template('index.html')

@app.route("/")
def index():
    return redirect('/index')

if __name__ == "__main__":
    app.run()
