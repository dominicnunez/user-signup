from flask import Flask, send_from_directory, request, render_template

app = Flask(__name__)

@app.route('/favicon.ico')

def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/', methods=["GET", "POST"])

def index():
    if request.method == "POST":
        # username = request.form["username"]
        return render_template("hello.html")
    else:
        render_template("index.html")