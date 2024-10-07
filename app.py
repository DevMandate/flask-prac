from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/converter", methods = ["GET" , "POST"])
def converter():
    if request.method == "GET":
        return render_template("programs.html")
    else:
        value = int(request.form["amt"])

        usd = value / 129

        return render_template("programs.html", your_value = usd)

@app.route("/bmi", methods = ["GET" , "POST"])
def bmi():
    if request.method == "GET":
        return render_template("programs.html")      
    else:
        val1 = int(request.form["weight"])
        val2 = float(request.form["height"])  

        bmi = val1 / (val2 * val2)

        return render_template("programs.html", actual_bmi = bmi)

@app.route("/volume", methods = ["GET" , "POST" ])
def volume():
    if request.method == "GET":
        return render_template("programs.html")
    else:
        r = int(request.form["radius"])

        volume = (4/3) * (22/7) * (r * r * r)

        return render_template("programs.html", volume_sphere = volume)



#  Binonmial Distribution Probabilty formula





app.run(debug=True)