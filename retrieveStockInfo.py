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
        
        tagged_values = soup.find_all("td", {'class': 'Ta(end) Fw(600) Lh(14px)'})
        recommendation_value = (soup.find("div", {'class': "Fw(b) Fl(end)--m Fz(s) C($primaryColor"})).get_text()
        price = soup.find("span", {'class': "Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"}).get_text()
        change = soup.find("span", {'class': 'Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($negativeColor)'})
        if change == None:
            change = soup.find("span", {'class': 'Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($positiveColor)'})
        
        change = (change.get_text()).split()
        values = []
        titles = ["Previous_Close", "Open", "Bid", "Ask", "Day's Range", "52 Week Range", "Volume", "Average Volume", "Market Cap", "Beta 3yr Monthly", "P/E Ratio (TTM)", "EPS (TTM)", "Earnings Date", "Forward Dividend & Yield", "Ex-Dividend Date", "1 yr Target Estimate"]
        value_dict = {}
        value_dict["Current Price"] = price
        value_dict["Change"] = change[0]
        value_dict["Percent Change"] = change[1][1:len(change[1])-1]
        for tv in tagged_values:
            values.append(tv.get_text())
        for i in range(len(values)):
            value_dict[titles[i]]= values[i]
        value_dict["Recommendation"] = recommendation_value  
        return value_dict
    
    def get_info_2(self):
        url = 'https://www.bloomberg.com/quote/' + self.val + ':US' 
        
        headers ={'User-Agent': 'Chrome/47.0.2526.80 Safari/537.36 Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko)'}
        req = urllib.request.Request(url, headers=headers)
        
        resp = urllib.request.urlopen(req)
        
        html = resp.read()
        
        soup = BeautifulSoup(html, 'html.parser')
        
        tagged_values = soup.find_all("div", {'class': 'value__b93f12ea'})
        tagged_values_2 = soup.find_all("span", {'class': 'fieldValue__2d582aa7'})
        tagged_titles = soup.find_all("header", {'class': 'title__49417cb9'})
        tagged_titles_2 = soup.find_all("span", {'class': 'fieldLabel__9f45bef7'})
        price = soup.find("span", {'class': 'priceText__1853e8a5'}).get_text()
        change = soup.find("span", {'class': 'changeAbsolute__395487f7 negative__53babed0 animatedBackground__bc43aa59'}).get_text()
        percent_change = soup.find("span", {'class': 'changePercent__2d7dc0d2 negative__53babed0 animatedBackground__bc43aa59'}).get_text()
    
        value_dict = {}
        values = []
        titles = []
        value_dict["Current Price"] = price
        value_dict["Change"] = change
        value_dict["Percent Change"] = percent_change
        for tv in tagged_values:
            values.append(tv.get_text())
        for tv in tagged_values_2:
            values.append(tv.get_text())

        for tt in tagged_titles:
            titles.append(tt.get_text())
        for tt in tagged_titles_2:
            titles.append(tt.get_text())

        for i in range(len(values)):
            value_dict[titles[i]]= values[i]
        if 'Address' in value_dict:
            value_dict.pop("Address")
        if 'Phone' in value_dict:
            value_dict.pop("Phone")
        return value_dict
    
    def get_Index_info(self):
        url = 'https://www.bloomberg.com/quote/' + self.val + ':IND' 
        
        headers ={'User-Agent': 'Chrome/47.0.2526.80 Safari/537.36 Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko)'}
        req = urllib.request.Request(url, headers=headers)
        
        resp = urllib.request.urlopen(req)
        
        html = resp.read()
        
        soup = BeautifulSoup(html, 'html.parser')
        
        tagged_values = soup.find_all("div", {'class': 'value__b93f12ea'})
        tagged_values_2 = soup.find_all("span", {'class': 'fieldValue__2d582aa7'})
        tagged_titles = soup.find_all("header", {'class': 'title__49417cb9'})
        tagged_titles_2 = soup.find_all("span", {'class': 'fieldLabel__9f45bef7'})
        price = soup.find("span", {'class': 'priceText__1853e8a5'}).get_text()
        change = soup.find("span", {'class': 'changeAbsolute__395487f7 negative__53babed0 animatedBackground__bc43aa59'}).get_text()
        percent_change = soup.find("span", {'class': 'changePercent__2d7dc0d2 negative__53babed0 animatedBackground__bc43aa59'}).get_text()
    
        value_dict = {}
        values = []
        titles = []
        value_dict["Current Price"] = price
        value_dict["Change"] = change
        value_dict["Percent Change"] = percent_change
        for tv in tagged_values:
            values.append(tv.get_text())
        for tv in tagged_values_2:
            values.append(tv.get_text())

        for tt in tagged_titles:
            titles.append(tt.get_text())
        for tt in tagged_titles_2:
            titles.append(tt.get_text())

        for i in range(len(values)):
            value_dict[titles[i]]= values[i]
        return value_dict
