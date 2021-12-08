import yfinance as yf

def getStockInfo(stockSymbol):
    infoParts = ["longName","zip","financialCurrency","currentPrice","regularMarketPrice","currency","grossProfits","country","enterpriseValue","website","CoinMarketCap"]
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
    infop2 = "regularMarketPrice"
    infop3 = "currency"
    if infop in info:
        return f"Current price of {stockSymbol}: {info[infop]} {info[infop3].upper()}"
    elif infop2 in info:
        return f"Current price of {stockSymbol}: {info[infop2]} {info[infop3].upper()}"
    else:
        return f"Sorry, our API does not contain the current price of {stockSymbol}."

def checkStockValid(stockSymbol):
    stock = yf.Ticker(stockSymbol)
    info = stock.info
    if(info["regularMarketPrice"]==None):
        return False
    else:
        return True


#print(getStockPrice("BTC-GBP"))
#print(getStockPrice("TSCO.L"))
#print(getStockPrice("AMZN"))
#print(getStockPrice("vow3.De"))
#print(getStockInfo("AMZN"))
