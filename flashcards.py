import random


terms = {"Investor": "Person purchasing the stock",
         "Shareholder": "Person selling the stock",
         "Previous Close": "The last price of the stock from when the market closed on the previous trading day",
         "Open": "The starting price of trading for this trading day",
         "Change": "How many points the stock rose/fell during the trading day",
         "Percent Change": "How much the stock rose/fell during the trading day compared to its value given as a percentage",
         "Bid": "The highest price an investor is willing to pay for a share",
         "Ask": "The lowest price at which a shareholder is willing to sell their shares",
         "Day's Range": "The difference between the highest and lowest price traded during the trading day",
         "52 Week Range": "The difference between the highest and lowest price traded during the past 52 weeks",
         "Volume": "The amount of an asset or security that changes hands over a specific period of time",
         "Average Volume": "The totol volume in the specified period divided by the number of bars",
         "Market Capitalization": "The total value of all a company's shares of stock",
         "Beta": "A measure of the stock's volatility",
         "P/E ratio": "The ratio of the Company's stock price to its earnings per share. This ratio is used to value the company and find out if its overvalued or undervalued",
         "Earnings Per Share": "The portion of a company's profit that that is allocated to every share of the stock",
         "Earnings Date": "The date of the next release of the company's financial report",
         "Forward Dividend and Yield": "An estimation of the year's dividend expressed as a percentage of the current stock price",
         "Ex-Dividend Date": "Set 1 day before the record date and determines who earns the dividend the seller or the buyer",
         "Target Estimate": "Reflects what analysts think the stock will be worth after a certain period of time"
         }

menu = None
while menu != 4:
    print("""

    Learn the Terminology!

    1 - List Terms
    2 - Learn the Definitions
    3 - Look up the definition to a specific term
    4 - Quiz Yourself
    5 - Exit

    """)
    
    menu = input("\t\t\tEnter Menu option: ")
    if menu == "1":
        print("\n")
        for term in terms:
            print("\t\t\t", term)
        input("\n\tPress 'Enter' to return to Main Menu.\n")
        
    elif menu == "2":
        print("\n\t\t\tType 'Exit' to return to Menu")
        print("\n\t\t\tPress Enter for another term\n\n")
        exit = None
        while exit != "EXIT":
            term, definition = random.choice(list(terms.items()))
            print(term + ":", definition)
            exit = input("").upper() 
    
    elif menu == "3":
        print("\n\t\t\tType 'Exit' to return to Menu")
        term = input("\n\t\t\tWhat term would you like to look-up?\n\n")
        while term != "EXIT":
            print(terms[term.capitalize()])
            exit = input("").upper()
    
    elif menu == "4":
        print("\n\t\t\tType 'Exit' to return to Menu\n")
        def generate_pairing():
            term, definition = random.choice(list(terms.items()))
            print(definition)
            return term.upper()
        term = generate_pairing()
        guess = ""
        while guess != "EXIT":
            guess = input("What is the Term?")
            print("\n")
            if guess.upper() == term:
                print("Correct!")
                if input("Next Definition?(y/n)") == "y":
                    print("\n")
                    term = generate_pairing()
                else:
                    guess = "EXIT"
            else:
                print("Sorry that is incorrect. Try again")
                    
        