from flask import Flask
from flask_cors import CORS
import pymysql
import os


app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/hello")
def hello():

    result = {"code": 200, "message": "jenkins test"}
    return result
