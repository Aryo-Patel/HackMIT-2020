from flask import Flask, url_for, render_template, request
from retrieveStockInfo import stock_info
from Prediction import ML
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('welcome.html')

@app.route('/stocks', methods= ['GET', 'POST'])
def stocks():
    if request.method == 'POST':
        ticker_tag = ""
        use_analysis = ""
        #ticker_tag is the stock they pick
        try:
            ticker_tag = request.form['stock-input']
            use_analysis = request.form['our-analysis']
        except:
            pass
       
        print(request.form)
        results = {}
        analysis = ""
        if ticker_tag != "":
            analysis = stock_info(ticker_tag)
            results = analysis.get_info()

        if use_analysis == 'on' and ticker_tag != "":
            x = ML(ticker_tag)
            x.get_prediction()
       
        print(results)

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
