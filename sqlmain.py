import base64
import time
import pymysql
from flask import Flask, request, make_response

import configparser
import pymysql

config = configparser.ConfigParser()

config.read('config.ini')

dbhost = config['DB']['MysqlDBIP']
dbuser = config['DB']['MysqlDBUser']
dbpwd = config['DB']['MysqlDBPWD']
dbtable = config['DB']['MysqlDB']

db = pymysql.connect(host=dbhost, port=3306, user=dbuser, passwd=dbpwd, db=dbtable, charset='utf8')
cursor = db.cursor()

conn = 0
app = Flask(__name__)



@app.route('/', methods=['GET'])
def server():
    return make_response('Todo: Create a nice page.', 200)

@app.route('/calc', methods=['GET'])
def calc():
    s1 = request.args
    s2 = s1['input']
    if len(s2) <= 9:
        return make_response("input長度錯誤", 406)
    elif s2.isdigit():
        rowadd = cursor.execute('SELECT cache FROM cache where cache =' + s2 + ';')
        global conn
        d2 = s2.encode("utf-8")
        d3 = base64.b64encode(d2)
        conn += 1
        rsp = (int(conn*4))
        if cursor.rowcount == 0:
            time.sleep(rsp)
            print("回應時間：" + str(rsp) + "秒")
            conn -= 1
        else:
            time.sleep(0.5)
            print("回應時間： 0.2秒")
            conn -= 1
        if conn>=70:
            return make_response("server is overloaded!", 503)

        else:
            rowadd = cursor.execute('SELECT cache FROM cache where cache =' + s2 + ';')

            if cursor.rowcount == 0:
                rowadd = cursor.execute("INSERT INTO cache (cache) VALUES (" + (s2) + ")" + ";")
                db.commit()
                return make_response(d3, 200)
            else:
                return make_response(d3, 200)
    else:
        return make_response("請輸入數字", 406)



@app.route('/healthcheck', methods=['GET'])
def hc():
    global conn
    if conn >=70:
        return "server is overloaded"
    else:
        return "Current continue task : " + str(conn)
if __name__ == '__main__':
    app.run(host="0.0.0.0", port="80")
