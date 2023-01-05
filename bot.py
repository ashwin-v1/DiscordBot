import discord
import requests
import json


intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)
TOKEN = 'MTA1OTk4ODYzMDQ3MjQ5MTA2OA.GoDwSc.k9BGDwnY0i3BjUFV3NhtTOkouA4WlAEwECGzek'


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    '''if message.author == client.user:
        return
    
    if message.content.startswith(x):
        x = input('Enter Symbol')'''
        
    base = 'https://rest.coinapi.io/v1/exchangerate'
    endpoint = '/' + message.content + '/' + 'USD'
    url = base + endpoint
    headers = {'X-CoinAPI-Key' : '72A67B2F-90EE-4717-A8A9-E15AA0EDEE52'}
    response = requests.get(url, headers=headers)
    rate = json.loads(response.text)['rate']
    await message.channel.send("$" + str(rate))

client.run(TOKEN)

