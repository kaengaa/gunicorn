from flask import Flask

app = Flask(__name__)

##views.py
@app.route('/hello')
def get():
    result = {"code": 200, "message":"hello"}
    return result


##manage.py
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)

