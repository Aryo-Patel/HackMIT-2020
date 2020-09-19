from bs4 import BeautifulSoup
import urllib.request

class stock_info:
    def __init__(self, ticker_symbol):
        self.val = ticker_symbol
    
    def get_info(self):
        url = 'https://finance.yahoo.com/quote/' + self.val  + '?p=' + self.val
        
        headers ={'User-Agent': 'Chrome/47.0.2526.80 Safari/537.36 Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko)'}
        req = urllib.request.Request(url, headers=headers)
        
        resp = urllib.request.urlopen(req)
        
        html = resp.read()
        
        soup = BeautifulSoup(html, 'html.parser')
        
        tagged_values= soup.find_all("td", {'class': 'Ta(end) Fw(600) Lh(14px)'})
        recommendation_value = (soup.find("div", {'class': "Fw(b) Fl(end)--m Fz(s) C($primaryColor"})).get_text()
        
        values = []
        titles = ["Previous_Close", "Open", "Bid", "Ask", "Day's Range", "52 Week Range", "Volume", "Average Volume", "Market Cap", "Beta 3yr Monthly", "P/E Ratio (TTM)", "EPS (TTM)", "Earnings Date", "Forward Dividend & Yield", "Ex-Dividend Date", "1 yr Target Estimate"]
        value_dict = {}
        for tv in tagged_values:
            values.append(tv.get_text())
        for i in range(len(values)):
            value_dict[titles[i]]= values[i]
        value_dict["Recommendation"] = recommendation_value
        return value_dict
