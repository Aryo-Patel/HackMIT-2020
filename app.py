from flask import Flask, url_for, render_template, request
from retrieveStockInfo import stock_info
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('welcome.html')

@app.route('/stocks', methods= ['GET', 'POST'])
def stocks():
    if request.method == 'POST':
        #ticker_tag is the stock they pick
        ticker_tag = request.form['stock-input']
        analysis = stock_info(ticker_tag)
        results = analysis.get_info()
        
        #add your code here

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
