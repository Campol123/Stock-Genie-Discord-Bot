import yfinance as yf

def getStockInfo(stockSymbol):
    infoParts = ["longName","zip","financialCurrency","currentPrice","grossProfits","country","enterpriseValue","website"]
    stock = yf.Ticker(stockSymbol)
    info = stock.info
    curatedInfo = f"Info about Stock: {stockSymbol}:"
    #print(info)
    for x in range(len(infoParts)):
        if infoParts[x] in info:
            curatedInfo+="\n" + str(infoParts[x]) + ": " + str(info[infoParts[x]])

    return curatedInfo

def getStockPrice(stockSymbol):
    stock = yf.Ticker(stockSymbol)
    info = stock.info
    infop = "currentPrice"
    if infop in info:
        return f"Current price of {stockSymbol}: ${info[infop]}"
    else:
        return f"Sorry, our API does not contain the current price of {stockSymbol}."

def checkStockValid(stockSymbol):
    stock = yf.Ticker(stockSymbol)
    info = stock.info
    if(info["regularMarketPrice"]==None):
        return False
    else:
        return True


#print(getStockPrice("AMZN"))
#print(getStockPrice("VOO"))
