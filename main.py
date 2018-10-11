from flask import Flask, send_from_directory, request, render_template
import os
from wtforms import Form, BooleanField, StringField, PasswordField, validators

class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25), validators.DataRequired()])
    email = StringField('Email Address', [validators.Length(min=6, max=35), validators.DataRequired()])
    password = PasswordField('New Password', [
        validators.DataRequired()
    ])
    confirm = PasswordField('Repeat Password', [
        validators.DataRequired(),
        validators.EqualTo('password', message='Passwords must match')
    ])
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])
    
app = Flask(__name__)

@app.route('/favicon.ico')

def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/', methods=["GET", "POST"])

def signup():
    form = RegistrationForm(request.form)
    if request.method == "POST" and form.validate():
        username = form.username.data
        return render_template("welcome.html", username=username)
    else:
        return render_template("signup.html", form=form)

if __name__ == "__main__":
    app.run(debug = True)