import discord # imports discord module used to connect to the Discord API
from discord.ext import commands # imports commands from Discord module
from stockinfo import getStockInfo,checkStockValid,getStockPrice # imports custom functions from 'stockinfo.py'

client = discord.Client() # connnects to Discord

botToken = "BotTokenGoesHere" # --Enter your bot token--

commands = ["/SG - brings up welcome text.","/SG help - brings up this menu.","/SG [Stock Symbol] info - returns info about given stock.","/SG [Stock Symbol] price - returns current price of given stock symbol."] # array that hold the commands to be displayed in the help menu

@client.event
async def on_ready(): # code that runs once connected to Discord
    print('We have logged in as {0.user}'.format(client)) # message to print once a connection has been made

@client.event
async def on_message(message):# code that runs once a message is received

    if message.author == client.user:# makes sure that the bot ignores it's own messages
        return

    if message.content.startswith('/SG'): #identifies the messages that start with '/SG' (Stock Genie)
        helpText = "" #initialises the helpText variable that holds the help menu as a string
        print(f"{message.author} ({message.author.id}) says \"{message.content}\"") # prints the message content and the user who posted it, aswell as their Discord ID

        if message.content==("/SG"): # identifies if they used the '/SG' command
            await message.channel.send(f'Hello! <@{message.author.id}>\nMy Name is Stock Genie!\nI am a Discord bot that can get you stock information.\ntry \"/SG help\" for available commands.') # sends Discord message adressing the user who entered the command

        elif message.content == ("/SG help"): # identifies if the user used the '/SG help' command
            for x in range(len(commands)): # constructs the help menu from the array
                helpText += commands[x]
                helpText += "\n"
            await message.channel.send(f'{helpText}') # sends the help menu

        elif message.content[len(message.content)-4] == ("i") and message.content[len(message.content)-3] == ("n") and message.content[len(message.content)-2] == ("f") and message.content[len(message.content)-1] == ("o") and len(message.content)>9: # identifies if the user used the '/SG <Stock Symbol> info' command
            stockSymbol = message.content.replace("/SG ", "").replace(" info", "").upper() # finds the stock symbol from the command and makes it uppercase
            if(checkStockValid(stockSymbol)): # checks the stock symbol is valid
                info = getStockInfo(stockSymbol) # gets the stock symbol info
                await message.channel.send(info) # sends the stock info
            else:
                await message.channel.send(f'Invalid Stock Symbol\nTry: /SG help') # sends an error explaining it was an invalid stock symbol

        elif message.content[len(message.content) - 5] == ("p") and message.content[len(message.content) - 4] == ("r") and message.content[len(message.content) - 3] == ("i") and message.content[len(message.content) - 2] == ("c") and message.content[len(message.content) - 1] == ("e") and len(message.content)>10: # identifies if the user used the '/SG <Stock Symbol> price' command
            stockSymbol = message.content.replace("/SG ", "").replace(" price", "").upper() # finds the stock symbol from the command and makes it uppercase
            if (checkStockValid(stockSymbol)): # checks the stock symbol is valid
                priceInfo = getStockPrice(stockSymbol) # gets the stock symbol price
                await message.channel.send(priceInfo) # sends the stock symbol price
            else:
                await message.channel.send(f'Invalid Stock Symbol\nTry: /SG help') # sends an error explaining it was an invalid stock symbol

        else:
            await message.channel.send(f'Invalid Command') # sends an error explaining it was an invalid command






client.run(botToken) # connects to your Discord bot