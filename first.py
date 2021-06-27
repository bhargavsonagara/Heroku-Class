from flask import Flask, render_template, request
import joblib

app = Flask(__name__, template_folder='template')
model = joblib.load('model_j')


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/submit", methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        exp = float(request.form['exp'])
        ts = float(request.form['ts'])
        isc = float(request.form['isc'])
    ans = model.predict([[exp, ts, isc]])
    return render_template('index.html', ans=f"Employer Salary should be ${round(ans[0], 2)}")


if __name__ == '__main__':
    app.debug = True
    app.run(port=8000)
