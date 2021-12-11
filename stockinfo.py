import yfinance as yf # imports the stock information API

def getStockInfo(stockSymbol): # defines the function to get stock info
    infoParts = ["longName","zip","financialCurrency","currentPrice","regularMarketPrice","currency","grossProfits","country","enterpriseValue","website","CoinMarketCap"]  # an array that contains the keys of the stock symbol info dictionary returned by the API
    stock = yf.Ticker(stockSymbol)
    info = stock.info # gets stock info
    curatedInfo = f"Info about Stock: {stockSymbol}:"
    #print(info)
    for x in range(len(infoParts)):
        if infoParts[x] in info:
            curatedInfo+="\n" + str(infoParts[x]) + ": " + str(info[infoParts[x]]) # assembles info text to be sent on Discord

    return curatedInfo

def getStockPrice(stockSymbol): # defines the function to get stock price
    stock = yf.Ticker(stockSymbol)
    info = stock.info
    infop = "currentPrice"
    infop2 = "regularMarketPrice"
    infop3 = "currency"
    if infop in info:
        return f"Current price of {stockSymbol}: {info[infop]} {info[infop3].upper()}" # assembles price text to be sent on Discord
    elif infop2 in info:
        return f"Current price of {stockSymbol}: {info[infop2]} {info[infop3].upper()}" # assembles price text to be sent on Discord
    else:
        return f"Sorry, our API does not contain the current price of {stockSymbol}." # returns an error stating the API does not have price information on a valid stock symbol

def checkStockValid(stockSymbol): # defines the function to check a stock symbol is valid
    stock = yf.Ticker(stockSymbol)
    info = stock.info
    if(info["regularMarketPrice"]==None): # checks if stock symbol has a regular market price to determine it's validity
        return False
    else:
        return True



