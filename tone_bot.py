import discord
from info import tones, token

tones, token = tones(), token()

bot = discord.Client()

@bot.event
async def on_message(message: discord.Message):
    for tone in tones.keys():
        if tone in message.content.split(' '):
            await message.channel.send(f'{message.author.mention}: ``{tones[tone]}``')

bot.run(token)
