# this code is from chat Gpt 
from flask import Flask
# now check the code 
app = Flask(__name__)
# this code is just for the example 
@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/about")
def about():
    return 'this'
    return "This is the About page."

if __name__ == "__main__":
    app.run(debug=True)
