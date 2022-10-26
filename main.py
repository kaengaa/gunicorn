from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/*":{"origins":"*"}})

##views.py
@app.route('/hello')
def get():
    result = {"code": 200, "message":"hello"}
    return result


##manage.py
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)

