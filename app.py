from flask import Flask, url_for, render_template, request
from retrieveStockInfo import stock_info
from Predictions import ML
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('welcome.html')

@app.route('/stocks', methods= ['GET', 'POST'])
def stocks():
    if request.method == 'POST':
        ticker_tag = request.form['stock-input']
        analysis = stock_info(ticker_tag)
        results = analysis.get_info()
        print(results)
        x = ML(ticker_tag)
        x.get_prediction()
        return render_template('stocks.html', results = results)
    else:
        pass
    return render_template('stocks.html', results = {})

@app.route('/learn')
def learn():
    return render_template('learn.html')

@app.route('/trends')
def trends():
    return "Trends"

if __name__ == "__main__":
    app.run(debug=True)
