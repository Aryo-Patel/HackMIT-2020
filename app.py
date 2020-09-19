from flask import Flask, url_for, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('welcome.html')

@app.route('/stocks', methods= ['GET', 'POST'])
def stocks():
    if request.method == 'POST':
        ticker_tag = request.form['stock-input']
        print(ticker_tag)
    else:
        pass
    return render_template('stocks.html')

@app.route('/learn')
def learn():
    return render_template('learn.html')

@app.route('/trends')
def trends():
    return "Trends"

if __name__ == "__main__":
    app.run(debug=True)
