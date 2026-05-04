from flask import Flask, render_template

app = Flask(__name__)

# Route for the homepage
@app.route("/")
def home():
    # This will render the index.html file from the templates folder
    return render_template("index.html")


# Route for the Structural page
@app.route("/structural")
def structural():
    return render_template("structural.html")


# Route for the Thermal Dynamics page
@app.route("/thermal")
def thermal():
    return render_template("thermal.html")


# Route for the Fluid Dynamics page
@app.route("/fluid")
def fluid():
    return render_template("fluid.html")


# Route for the Concrete prediction page
@app.route("/concrete")
def concrete():
    return render_template("concrete.html")




if __name__ == "__main__":
    app.run(debug=True)
