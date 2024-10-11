import pickle
from flask import Flask, request, app,jsonify,url_for, render_template
import numpy as np
import pandas as pd

# Initialize the Flask app
app = Flask(__name__)

# Load the model and the scalar
regmodel = pickle.load(open('regmodel.pkl', 'rb'))
scalar = pickle.load(open('scaling.pkl', 'rb'))

# Home route
@app.route('/')
def home():
    return render_template('home.html')

# Predict API route
@app.route('/predict_api', methods=['POST'])
def predict_api():
    # Get the data from the POST request
    data = request.json['data']
    print(data)
    
    # Reshape and scale the data
    new_data = scalar.transform(np.array(list(data.values())).reshape(1, -1))
    
    # Make the prediction
    output = regmodel.predict(new_data)
    print(output[0])
    
    # Return the prediction result as JSON
    return jsonify(output[0])

#Making new html page for the inputs of the Users:
@app.route('/predict',methods=['POST'])
def predict():
    # Get the data from the POST request
    data=[float(x) for x in request.form.values()]
    final_input = scalar.transform(np.array(data).reshape(1,-1))
    print(final_input)
    output = regmodel.predict(final_input)[0]
    return render_template('home.html',prediction_text = "The house Price prediction is {}".format(output))
    


# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
