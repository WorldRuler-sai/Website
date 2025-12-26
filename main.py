from flask import Flask

# Create a Flask application instance with the name of the current module
app = Flask(__name__)

# A decorator that maps the root URL ("/") to this function
@app.route("/")
def hello_world():
    return "Hello, World!"

# This block allows you to run the app directly using 'python app.py'
if __name__ == "__main__":
    app.run(debug=True)
