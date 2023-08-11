import discord

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Bot online como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user: 
        return
    
    if message.content.startswith('!hello'):
        await message.channel.send('Olá, mundo!')

TOKEN = 'MTEzMTYxNDE4ODA4NzgyNDQ4NA.Gz-kpX.OtTAJf7q-VHebXywM00R8g1Wks2BPoEiV_5Nuw'
client.run(TOKEN)
