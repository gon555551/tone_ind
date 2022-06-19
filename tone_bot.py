import discord
from info import gettones, gettoken, getquestion

# get the tones dict, the token str, and the question string
tones, token = gettones(), gettoken()
question = getquestion(tones)

# start the bot
bot = discord.Client()

# event reader
@bot.event
async def on_message(message: discord.Message):
    
    # always ignore own messages
    if message.author == bot.user:
            return
        
    # explain
    try:
        if message.content.index('/?') == 0:
            await message.channel.send(question)
    except ValueError:
        pass
    
    # if tone indicator is used
    for tone in tones.keys():
        if tone in message.content.split(' '):
            
            # @ the user and send the meaning
            await message.channel.send(f'{message.author.mention}: ``{tones[tone]}``')
            return

# loop
bot.run(token)
