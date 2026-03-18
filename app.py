from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    homepage = "<h1>蔡純珍Python網頁</h1>"
    homepage += '<a href="/mis">MIS</a><br>'
    homepage += '<a href="/today">顯示日期時間</a><br>'
    homepage += '<a href="/me">蔡純珍簡介網頁</a><br>'
    return homepage

@app.route("/mis")
def course():
    return "<h1>資訊管理導論</h1>"

@app.route("/today")
def today():
    now = datetime.now()
    formatted_now = now.strftime("%Y年%m月%d日")
    return render_template("today.html", datetime = formatted_now)

@app.route("/me")
def me():
    now = datetime.now()
    formatted_now = now.strftime("%Y-%m-%d")
    return render_template("me.html", datetime = formatted_now)

if __name__ == "__main__":
    app.run(debug=True)