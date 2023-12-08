from flask import Flask, request, render_template
import pickle
import pandas as pd


app = Flask(__name__)
d=pd.read_csv('insurance.csv')
model = pickle.load(open(r"C:\Users\amrit\Desktop\Insurance-project\rf_tuned.pkl", "rb"))


#age,sex,bmi,children,smoker,region,charges
@app.route('/')

def hello_world():
    return render_template('home2.html')

@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        age = int(request.form["age"])
        sex = request.form["sex"]
        bmi = request.form["bmi"]
        children = int(request.form["children"])
        smoker = request.form["smoker"]
        region = request.form["region"]


        prediction = model.predict([[
        age,sex,bmi,children,smoker,region

        ]])

        output = round(prediction[0], 3)

        return render_template('home2.html', prediction_text="Your charge is Rs. {}".format(output))


if __name__ == "__main__":
    app.run(debug=True)

