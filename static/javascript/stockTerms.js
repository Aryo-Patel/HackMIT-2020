let terms = {"Investor": "Person purchasing the stock",
"Shareholder": "Person selling the stock",
"Current Price": "The most recent selling price of an asset",
"Previous Close": "The last price of the stock from when the market closed on the previous trading day",
"Open": "The starting price of trading for this trading day",
"Change": "How many points the stock rose/fell during the trading day. This value is calculated by taking the current value and subtracting the previous day's closing value.",
"Percent Change": "How much the stock rose/fell during the trading day compared to its value given as a percentage",
"Bid": "The highest price an investor is willing to pay for a share",
"Ask": "The lowest price at which a shareholder is willing to sell their shares",
"Day's Range": "The difference between the highest and lowest price traded during the trading day",
"52 Week Range": "The difference between the highest and lowest price traded during the past 52 weeks",
"Volume": "The amount of an asset or security that changes hands over a specific period of time",
"Average Volume": "The total volume in the specified period divided by the number of bars. When the average volume changes dramitcally it signifies a substantial shift in how people value or view the asset.",
"Market Cap": "The total value of all a company's shares of stock. Large Cap companies have a market cap of $10 B or more and are often considered more conservative investments since the company is more reliable and experiences less aggressive growth. Mid Cap companies have a market cap between $2 B and $10 B and are usually experiencing or expected to experience rapid growth. Small Cap companies have a market cap between $300 M and $2 B and are new vulnerable companies that can be risky.",
"Beta 3 Year Monthly": "A measure of the stock's volatility. The S&P 500 has a beta of 1. Companies with a beta higher than 1 are said to be riskier, but offer a greater potential return. Companies with a beta lower than 1 are less risky, but offer lower returns.",
"P/E Ratio": "The ratio of the Company's stock price to its earnings per share. This ratio is used to value the company and find out if its overvalued or undervalued by comparing it to other stocks in the industry group",
"Earnings Per Share": "The portion of a company's profit that that is allocated to every share of the stock. This number gauges a company's profitability. The higher this number is the more profitable the stock of the company is.",
"Earnings Date": "The date of the next release of the company's financial report",
"Forward Dividend Yield": "An estimation of the year's dividend expressed as a percentage of the current stock price",
"Ex-Dividend Date": "Set 1 day before the record date and determines who earns the dividend the seller or the buyer. If you were to make a purchase on or after this date the seller earns the dividend",
"1 Year Target Estimate": "Reflects what analysts think the stock will be worth after a certain period of time. This number can change overtime as new information becomes available."
}

let stockTerms = document.querySelectorAll('.info');
stockTerms = Array.from(stockTerms);
let userX;
let userY;
let explanation;
let yOffset = window.pageYOffset;
document.addEventListener('mousemove', event =>{
    userX = event.clientX;
    userY = event.clientY;
    yOffset = window.pageYOffset
    console.log(userX);
})
stockTerms.forEach(term => {
    term.addEventListener('mouseover', e =>{
        let textContent = e.target.innerHTML;
        let referencePhrase = textContent.split(':')[0]
        console.log(e.target.getBoundingClientRect())
        let rect = e.target.getBoundingClientRect();
        
        explanation = document.createElement('div');
        explanation.classList.add('blurb');
        explanation.style.width = e.target.width;
        explanation.style.left = rect.left+ 'px';
        explanation.style.top = rect.top - 50 + yOffset + 'px';
        let paragraphAdd = document.createElement('p');
        paragraphAdd.classList.add('blurb-text');
        paragraphAdd.textContent = terms[referencePhrase];
        explanation.appendChild(paragraphAdd);

        document.getElementById('stock-info-table').appendChild(explanation);
    });
    term.addEventListener('mouseout', e => {
        let table = document.getElementById('stock-info-table');
        table.removeChild(explanation);
    })
});

function createBlurb(){
    let blurb = document.createElement('div');
    blurb.classList.add('blurb');
}
