import base64
import io
import os
import pandas as pd
from flask import Flask, render_template, request, jsonify

from AppliedProbStatsConcrete.main import predict_concrete
from AppliedProbStatsConcrete.utilsProbs import ThetaFinder, MatrixDummyColumn, TargetVector, Predict
from AppliedProbStatsConcrete.plotting import PlotDiagnostics 

app = Flask(__name__)


DATA_FOLDER = "./AppliedProbStatsConcrete"


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


# Route for the Concrete page
@app.route("/concrete", methods=["GET"])
def concrete():
    csv_files = [f for f in os.listdir(DATA_FOLDER) if f.endswith(".csv")]
    return render_template("concrete.html", csv_files=csv_files, csv_preview=None, row_count=None)

# Route for CSV preview
@app.route("/concrete/preview", methods=["POST"])
def concrete_preview():
    selected_csv = request.form.get("selected_csv")
    if not selected_csv:
        return jsonify({"error": "No CSV selected"}), 400

    df = pd.read_csv(os.path.join(DATA_FOLDER, selected_csv))
    preview_data = df.head(5).to_dict(orient="records")
    row_count = len(df)
    columns = df.columns.tolist()

    return jsonify({
        "preview": preview_data,
        "row_count": row_count,
        "columns": columns
    })


# route for getting user ingredient amounts
import json
import numpy as np

@app.route("/concrete/run_prediction", methods=["POST"])
def run_prediction():
    selected_csv = request.form.get("selected_csv")
    ingredients = request.form.get("ingredients")

    if not selected_csv or not ingredients:
        return jsonify({"error": "Missing CSV or ingredient inputs"}), 400

    ingredients = json.loads(ingredients)

    x_new = np.array([
        ingredients["cement"],
        ingredients["slag"],
        ingredients["fly_ash"],
        ingredients["water"],
        ingredients["super_plasticizer"],
        ingredients["coarse_agg"],
        ingredients["fine_agg"],
        ingredients["age"]
    ])

    result = predict_concrete(os.path.join(DATA_FOLDER, selected_csv), x_new)


    return jsonify({
        "theta": result["theta"].flatten().tolist(),
        "epsilon_sample": result["epsilon"].flatten()[:10].tolist(),
        "predicted_y": float(np.array(result["y_pred"]).flatten()[0])
    })


# route for getting data for the plot diagnostics
@app.route("/concrete/plot_diagnostics", methods=["POST"])
def plot_diagnostics_route():
    selected_csv = request.form.get("selected_csv")
    if not selected_csv:
        return jsonify({"error": "No CSV selected"}), 400

    try:
        df = pd.read_csv(os.path.join(DATA_FOLDER, selected_csv))

        # Compute predicted values and residuals using your existing functions
        theta, epsilon, y_hat = ThetaFinder(df)
        y_actual = TargetVector(df)  # last column of df

        # Generate diagnostics plot as base64
        img_base64 = PlotDiagnostics(y_actual, y_hat, epsilon)

        return jsonify({
            "plot_url": f"data:image/png;base64,{img_base64}",
            "epsilon_sample": epsilon[:10].flatten().tolist()
            })
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    
    
    
    
    
    

# #  main entry point
if __name__ == "__main__":
    app.run(debug=True)
