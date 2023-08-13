import pandas as pd
import numpy as np
from flask import render_template, Flask, request
from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message
app = Flask(__name__)

port = int(os.environ.get("PORT", 5000))

# Configure Flask-Mail for Gmail
app.config['MAIL_SERVER'] = 'smtp.office365.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'designlabswork@outlook.com'  # Replace with your Gmail address
app.config['MAIL_PASSWORD'] = 'google12'   # Replace with your Gmail password
app.config['MAIL_DEFAULT_SENDER'] = 'designlabswork@outlook.com'


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')



@app.route('/portfolio', methods=['GET', 'POST'])
def portfolio():
    return render_template('portfolio.html')


mail = Mail(app)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        msg = Message('New Contact Form Submission', recipients= ['designlabswork@outlook.com'])  # Replace with recipient's email
        msg.body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
        mail.send(msg)

        msg = Message('New Contact Form Submission', recipients=[email])  # Replace with recipient's email
        msg.body = f"Hello, {name}\n We have received your query.\nWe will contact you soon\nThank you so much for your trust\n Best Regards,\n Team Design Labs"
        mail.send(msg)

        return redirect(url_for('contact'))

    return render_template('contact.html')
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port)
