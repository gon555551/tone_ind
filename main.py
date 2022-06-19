import discord
from func import *

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

# on message
@bot.event
async def on_message(message: discord.Message):    
    if message.author == bot.user:
        pass
    
    elif message.content.startswith('t?all'):
        if message.author.dm_channel is None:
            await message.author.create_dm()
        await message.author.dm_channel.send(question)

    elif message.content.startswith('t?what'):
        await message.channel.send(whattone(message.content, tones))
    
    elif message.content.startswith('t?mean'):
        await message.channel.send(meanind(message.content, tones))
    
    else:
        line = toneused(message.content, tones)
        if line != '':
            await message.reply(line, mention_author=False)

# loop
bot.run(token)
