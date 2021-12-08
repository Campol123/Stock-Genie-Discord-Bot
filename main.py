import discord
import os
from discord.ext import commands
from stockinfo import getStockInfo,checkStockValid,getStockPrice

client = discord.Client()
commands = ["/SG - brings up welcome text.","/SG help - brings up this menu.","/SG [Stock Symbol] info - returns info about given stock.","/SG [Stock Symbol] price - returns current price of given stock symbol."]
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('/SG'):
        helpText = ""
        print(f"{message.author} says \"{message.content}\"")
        if message.content==("/SG"):
            await message.channel.send(f'Hello! <@{message.author.id}>\nMy Name is Stock Genie!\nI am a Discord bot that can get you stock information.\ntry \"/SG help\" for available commands.')

        elif message.content==("/SG you smell"):
            await message.channel.send(f'fuck right off <@{message.author.id}>')

        elif message.content == ("/SG help"):
            for x in range(len(commands)):
                helpText += commands[x]
                helpText += "\n"

            await message.channel.send(f'{helpText}')


        elif message.content[len(message.content)-4] == ("i") and message.content[len(message.content)-3] == ("n") and message.content[len(message.content)-2] == ("f") and message.content[len(message.content)-1] == ("o") and len(message.content)>9:

            stockSymbol = message.content.replace("/SG ", "").replace(" info", "")
            if(checkStockValid(stockSymbol)):
                info = getStockInfo(stockSymbol)
                await message.channel.send(info)
            else:
                await message.channel.send(f'Invalid Stock Symbol\nTry: /SG help')

        elif message.content[len(message.content) - 5] == ("p") and message.content[len(message.content) - 4] == ("r") and message.content[len(message.content) - 3] == ("i") and message.content[len(message.content) - 2] == ("c") and message.content[len(message.content) - 1] == ("e") and len(message.content)>10:
            stockSymbol = message.content.replace("/SG ", "").replace(" price", "")
            if (checkStockValid(stockSymbol)):
                priceInfo = getStockPrice(stockSymbol)
                await message.channel.send(priceInfo)
            else:
                await message.channel.send(f'Invalid Stock Symbol\nTry: /SG help')

        else:
            await message.channel.send(f'Invalid Command')






client.run("OTE3NzY0NzMwNzI1MjIwMzUy.Ya9dAw.EKBAj6FnKPozbMtLRfF0TfcqB1Q")