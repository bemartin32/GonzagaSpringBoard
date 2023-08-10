from flask import Flask, request

app = Flask(__name__)


@app.route("/welcome")
def welcome():
    return """
    <html>
      <body>
        <h1>Welcome!</h1>
      </body>
    </html>"""


@app.route("/welcome/home")
def home():
    return """
    <html>
      <body>
        <h1>Welcome Home!</h1>
      </body>
    </html>"""


@app.route("/welcome/back")
def back():
    return """
    <html>
      <body>
        <h1>Welcome Back!</h1>
      </body>
    </html>"""
