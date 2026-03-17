from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return ""

@app.route("/mis")
def course():
    return "<h1>資訊管理導論</h1>"

@app.route("/today")
def today():
    now = datetime.now()
    year = str(now.year)
    month = now.month
    day = now.day
    now = year + "年" + month + "月" + day + "日" +
    return render_template("today.html",datetime = now)
if __name__ == "__main__":
    app.run(debug=True)
