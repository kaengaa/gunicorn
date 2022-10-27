import os

from flask import Flask
import pymysql

app = Flask(__name__)

##views.py
@app.route('/hello')
def get():
    host = os.environ['DB_HOST']
    user = os.environ['DB_USER']
    password = os.environ['MYSQL_ROOT_PASSWORD']
    db = os.environ['DB_NAME']
    conn = pymysql.connect(
        host=host,
        user=user,
        password=pasword,
        db=db,
        port=port
    )

    curs = conn.cursor()
    sql = "SELECT * FROM student;"
    curs.execute(sql)
    rows = curs.fetchall()
    conn.close()

    result = {"code": 200, "message": rows}
    return result


##manage.py
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)

