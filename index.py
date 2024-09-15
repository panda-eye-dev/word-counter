from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route("/", methods =["GET", "POST"])
def home():
    user_input = request.form.get("user_input")
    if user_input:
        print(user_input)
    return render_template("index.html")

""" Step 1 - User types or paste in text
    Step 2 - As soon as someone types in the function
    in python starts """
if __name__ == '__main__':
    app.run(debug=True)
