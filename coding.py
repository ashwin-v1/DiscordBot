import discord
import requests
import json


BASE_URL = 'https://pro-api.coinmarketcap.com'
endpoint = '/v2/cryptocurrency/quotes/latest'
url = BASE_URL + endpoint

TOKEN = 'MTA1OTk4ODYzMDQ3MjQ5MTA2OA.GoDwSc.k9BGDwnY0i3BjUFV3NhtTOkouA4WlAEwECGzek'
headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': '002e8dee-6bdc-400c-8735-9011914b4749',
        }


params = {
    'id': '1',
   
}

session = requests.Session()
session.headers.update(headers)
response = session.get(url, params=params)


info = json.loads(response.text)['data']['1']['quote']['USD']['price']
print(info)

intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('btc'):
        await message.channel.send("$" + str(info))

client.run(TOKEN)



