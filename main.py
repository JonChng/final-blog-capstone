from flask import Flask, render_template, request
import requests
import smtplib
import os
import dotenv

dotenv.load_dotenv()
email_= os.environ['EMAIL']
password_ = os.environ['PASSWORD']


app = Flask(__name__)

data = "https://api.npoint.io/b3493c05712de3a10f7f"
response = requests.get(data).json()

@app.route("/")
def home():
    return render_template("index.html", resp=response)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/post/<id>")
def post(id):
    for post in response:
        if post['id'] == int(id):
            to_post = post
    return render_template("post.html", posted = to_post)

@app.route('/form-entry', methods=["POST"])
def receive_data():
    data = request.form
    msg = f"Subject: New Contact us!\n\n" \
          f"Name: {data['name']}\n" \
          f"Email: {data['email']}\n" \
          f"HP: {data['hp']}\n" \
          f"Message: {data['message']}"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email_, password=password_)
        connection.sendmail(to_addrs=os.environ["TO"], from_addr=email_, msg=msg)

    return "<h1>Successfully Sent Message!</h1>"




if __name__ == "__main__":
    app.run(port=5000, debug=True)