import discord
from info import *

# get the tones dict, the token str, and the question string
tones, token = gettones(), gettoken()
question = getquestion(tones)

# start the bot
bot = discord.Client()

# on ready
@bot.event
async def on_ready():
    print(f'<{bot.user}> is ready.')
    return

# event reader
@bot.event
async def on_message(message: discord.Message):    
    if message.author == bot.user:
        return
    
    if message.content.startswith('t?all'):
        if message.author.dm_channel is None:
            dm = await message.author.dm_channel()
            await dm.send(question)
        else:
            await message.author.dm_channel.send(question)
        return

    for tone in tones.keys():
        if tone in message.content.split(' '):
            await message.reply(f'``{tones[tone]}``', mention_author=False)
            return

# loop
bot.run(token)
