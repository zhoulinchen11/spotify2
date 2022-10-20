from flask import Flask

app = Flask(__name__)

@app.route('/data')
def my_profile():
    response_body = {
        "name": "Nagato",
        "about" :"Hello"
   }

    return response_body