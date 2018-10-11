from flask import Flask, send_from_directory, request, render_template
import os

app = Flask(__name__)

@app.route('/favicon.ico')

def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/', methods=["GET", "POST"])

def signup():
    if request.method == "POST":
        username = request.form["username"]
        return render_template("welcome.html", username=username)
    else:
        return render_template("signup.html")

if __name__ == "__main__":
    app.run(debug = True)