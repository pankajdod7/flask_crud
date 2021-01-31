from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__,template_folder='template')


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/register",methods = ['POST','GET'])
def register():
    if request.method == 'POST':
        html = "hrllo"
        return html
    else:
        return render_template("home.html")

'''
@app.route("/log",methods=['GET'])
def m2():
    uname = request.args.get("t1")
    password = request.args.get("t2")
    print("User Name---", uname)
    print("Password---", password)

    return render_template("success.html")

'''

if __name__=='__main__':
    app.run(debug=True)