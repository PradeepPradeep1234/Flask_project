from flask import *

app = Flask(__name__)
credentials={}
@app.route("/")
@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="POST":
        NAME=request.form.get("user_name")
        PASSWORD=request.form.get("Pass_word")

        if NAME==credentials["name"] and PASSWORD==credentials["password"]:
            return "Login Success"
        else:
            return "Check your login credentials"
    return render_template("login.html",title_name="Login Page")

@app.route("/register",methods=["POST","GET"])
def register():
    if request.method=="POST":
        NAME_1=request.form.get("UserName")
        PASSWORD_1=request.form.get("PassWord")
        credentials["name"]=NAME_1
        credentials["password"]=PASSWORD_1
        return redirect(url_for("login"))
    return render_template("register.html",title_name="Register page")

if __name__ == '__main__':
    app.run(debug=True)
