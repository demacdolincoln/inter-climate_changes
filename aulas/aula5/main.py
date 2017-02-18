from flask import Flask, render_template

app = Flask(__name__)
app.config["SECRET_KEY"] = "carbono"

@app.route("/", methods=["GET", "POST"])
def calculadora():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
