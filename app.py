from flask import Flask,render_template,request
from co2 import pred
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/res',methods = ["POST","GET"])
def he():
    if request.method == "POST":
        n =  request.form["user_input"]
        if int(n) > 248:
            return render_template("error.html")
        n = pred(int(n))
        
        return render_template("result.html", j = n)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)