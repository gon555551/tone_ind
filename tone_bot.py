import discord
from info import tones, token

# get the tones dict and the token str
tones, token = tones(), token()

# start the bot
bot = discord.Client()

# event reader
@bot.event
async def on_message(message: discord.Message):
    for tone in tones.keys():
        if tone in message.content.split(' '):
            
            # @ the user and send the meaning
            await message.channel.send(f'{message.author.mention}: ``{tones[tone]}``')

# loop
bot.run(token)
