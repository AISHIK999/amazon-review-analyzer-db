from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/review')
def review():
    data = pd.read_csv('temp/reviews.csv')
    return render_template('review.html', data=data.to_html())


if __name__ == "__main__":
    app.run(debug=True, port=5000)
