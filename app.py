from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('welcome.html')

@app.route('/stocks')
def stocks():
    return "Stocks page"

@app.route('/learn')
def learn():
    return "Learn page"

@app.route('/trends')
def trends():
    return "Trends"

if __name__ == "__main__":
    app.run(debug=True)
