from flask import Flask, render_template, request, flash, jsonify
import pyrebase
from config import firebaseConfig
from gpt_practice import generate_text

app = Flask(__name__)
app.secret_key = "randomaf"
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

@app.route('/',methods=["GET","POST"])
def index():
    return render_template('index.html')

@app.route('/chat', methods=["POST"])
def chat():
    user_input = request.json.get("message")
    response = generate_text(user_input)

    return jsonify({"reply":response})


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == "testtest" and password == "123123":
            print("Good")
            return render_template('login.html')
        else:
            flash("Wrong username or password")
            return render_template('login.html')
        return render_template('login.html')
    else:
        return render_template('login.html')

def add_user():
    username = "test2@test.com"
    password = "1231234"
    try:
        user = auth.create_user_with_email_and_password(username, password)
    except:
        print("Error")
if __name__ == '__main__':
    # add_user()
    app.run(debug=True)