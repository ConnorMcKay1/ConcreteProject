from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    # This will render the index.html file from the templates folder
    return render_template("index.html")






# # Route for the Structural page
# @app.route("/structural")
# def about():
#     return render_template("structural.html")

# # Route for the Thermal Dynamics page
# @app.route("/Thermal")
# def contact():
#     return render_template("thermal.html")

# # Route for the Fluid Dynamics page
# @app.route("/Fluid")
# def contact():
#     return render_template("fluid.html")

# # Route for the Concrete prediction page
# @app.route("/Fluid")
# def contact():
#     return render_template("fluid.html")




if __name__ == "__main__":
    app.run(debug=True)