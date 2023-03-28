from flask import Flask, render_template
import requests

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



if __name__ == "__main__":
    app.run(port=5000, debug=True)