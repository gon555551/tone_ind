import discord
from info import tones, token

# get the tones dict and the token str
tones, token = tones(), token()

# start the bot
bot = discord.Client()

# event reader
@bot.event
async def on_message(message: discord.Message):
    
    # always ignore own messages
    if message.author == bot.user:
            return
        
    # explain
    if message.content.index('/?') == 0:
        line = f'''Hello {message.author.mention}! Your message started with ``/?``,  so I'll explain how I work...

Simply use a tone indicator, like ``/srs``, anywhere in your message (as long as it's separated from other words with a space), and I'll send a message in the same channel saying what it means.

Currently, these are the tone indicators I recognize:

'''
        for key, value in tones.items():
            line += f'``{key}`` -> ``{value}``\n'
        
        line += '\nUse ``./tone`` if you don\'t want me to explain it! /srs'
        
        await message.channel.send(line)
    
    # if tone indicator is used
    for tone in tones.keys():
        if tone in message.content.split(' '):
            
            # @ the user and send the meaning
            await message.channel.send(f'{message.author.mention}: ``{tones[tone]}``')
            return

# loop
bot.run(token)
