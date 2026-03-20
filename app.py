from flask import Flask, render_template

app = Flask(__name__) #creates a Flask application

@app.route("/") #startpage
def home():
    return render_template("index.html")

@app.route("/muchmore")
def therewillbemore():
    return render_template("more.html")

@app.route("/nerd")
def nerd():
    return render_template("nerd.html")

@app.route("/aboutflask")
def school():
    return render_template("school.html")

if __name__ == "__main__":
    app.run(debug=True)