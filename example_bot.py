import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == ('ping'):
        await message.channel.send('pong')

client.run('OTAzMDE3MDE3NzEwMzQ2MjQw.YXm2Ig.XZx9KWGpR2pS83gFfkKGBLnGmL4')
