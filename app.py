from flask import Flask, render_template

app = Flask(__name__) #creates a Flask application

@app.route("/") #startpage
def home():
    return render_template("index.html")

@app.route("/rollerskate")
def rollerskate():
    return render_template("rollerskate.html")

@app.route("/nerd")
def nerd():
    return render_template("nerd.html")

if __name__ == "__main__":
    app.run(debug=True)