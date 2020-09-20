import pandas as pd
import warnings
warnings.filterwarnings('ignore')
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
from pylab import rcParams
rcParams['figure.figsize'] = 10, 6
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima_model import ARIMA
from pmdarima.arima import auto_arima
from sklearn.metrics import mean_squared_error, mean_absolute_error
import math
import numpy as np

class ML:
    def __init__(self, ticker_symbol):
        self.val = ticker_symbol
    def get_prediction(self):
        company = self.val
        format = 'http://download.macrotrends.net/assets/php/stock_data_export.php?t='
        url = format + company
        # print(url)
        stock_price = pd.read_csv(url, skiprows=14)
        # print(stock_price)
        close = list(stock_price.close)
        dates = list(stock_price.date)

        stock_price.columns = ['date', 'open', 'high', 'low', 'close', 'volume']
        stock_price = stock_price.dropna()
        stock_price['date'] = pd.to_datetime(stock_price['date'], yearfirst=True)
        stock_price.set_index('date', inplace=True) #set date as index
        stock_price.head()
        del stock_price['open']
        del stock_price['high']
        del stock_price['low']
        del stock_price['volume']

        rolmean = stock_price.rolling(12).mean()
        rolstd = stock_price.rolling(12).std()

        adft = adfuller(stock_price, autolag='AIC')


        result = seasonal_decompose(stock_price, model='multiplicative', freq=30)

        rcParams['figure.figsize'] = 10, 6
        stock_price_log = np.log(stock_price)
        moving_avg = stock_price_log.rolling(12).mean()
        std_dev = stock_price_log.rolling(12).std()


        train_data, test_data = stock_price_log[3:int(len(stock_price_log)*0.9)], stock_price_log[int(len(stock_price_log)*0.9):]
        plt.figure(figsize=(12,8))
        plt.grid(True)
        plt.xlabel('Dates (Years)')
        plt.ylabel('Closing Prices (USD)')
        plt.yticks(np.arange(min(close), max(close), (max(close)-min(close))//10))
        plt.plot(np.exp(stock_price_log), 'green', label='Train data')
        plt.plot(np.exp(test_data), 'blue', label='Test data')
        plt.legend()
        plt.show()

        model_autoARIMA = auto_arima(train_data, start_p=0, start_q=0, test='adf', max_p=3, max_q=3, m=1, d=None, seasonal=False, start_P=0, D=0, trace=True, error_action='ignore', suppress_warnings=True, stepwise=True)


        model = ARIMA(train_data, order=(0,1,2)) # This is where we put the order of machine learning model
        fitted = model.fit(disp=-1)


        fc, se, conf = fitted.forecast(len(close)//10+1, alpha=0.05)  # 95% confidence interval - This is where we change the other forecast model.
        fc_series = pd.Series(fc, index=test_data.index)
        lower_series = pd.Series(conf[:, 0], index=test_data.index)
        upper_series = pd.Series(conf[:, 1], index=test_data.index)
        plt.figure(figsize=(12,8), dpi=100)
        plt.plot(np.exp(train_data), label='Training')
        plt.plot(np.exp(test_data), color = 'blue', label='Actual Stock Price (USD)')
        plt.plot(np.exp(fc_series), color = 'orange',label='Predicted Stock Price (USD)')
        plt.yticks(np.arange(min(close), max(close), (max(close)-min(close))//10))
        # plt.fill_between(lower_series.index, lower_series, upper_series, color='k', alpha=.10)
        plt.title(company + ' Stock Price Prediction')
        plt.xlabel('Time')
        plt.ylabel('Actual Stock Price')
        plt.legend(loc='upper left', fontsize=8)
        plt.show()
