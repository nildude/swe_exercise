from flask import Flask
import os
import psycopg2

app = Flask(__name__)
app.config['DEBUG'] = True


#db = os.environ['POSTGRES_PORT']+
db = 'dbname=testdb user=postgres'
conn = psycopg2.connect(db)

@app.route("/")
def hello():
    cur = conn.cursor()
    cur.execute("SELECT count from COUNTER LIMIT 1")
    count = cur.fetchone()[0]
    txt = "UPDATE counter SET count={} +1 WHERE count = {}".format(count,count)
    cur.execute(txt)
    conn.commit()
    return "<p>Hello World!</p><p> You are number %d</p>" % count

if __name__ == "__main__":

    app.run(host='0.0.0.0',port=5000)
