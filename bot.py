import discord
import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)
TOKEN = os.getenv("TOKEN1")


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):

    base = 'https://rest.coinapi.io/v1/exchangerate'
    endpoint = '/' + message.content + '/' + 'USD'
    url = base + endpoint
    headers = {'X-CoinAPI-Key' : '72A67B2F-90EE-4717-A8A9-E15AA0EDEE52'}
    response = requests.get(url, headers=headers)
    rate = json.loads(response.text)['rate']
    await message.channel.send("$" + str(rate))

client.run(TOKEN)