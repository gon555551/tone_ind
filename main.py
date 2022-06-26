import discord, os, dotenv
from func import *

# start the bot
bot = discord.Client()

# get the handler, load .env
handler = EventHandler(get_tones())
dotenv.load_dotenv()

# on ready
@bot.event
async def on_ready():
    print(f"<{bot.user}> is ready.")
    return


# on message
@bot.event
async def on_message(message: discord.Message):
    if message.author == bot.user:
        return

    match message.content.split(" ")[0]:
        case "t?all":
            if message.author.dm_channel is None:
                await message.author.create_dm()
            await message.author.dm_channel.send(handler.question)
        case "t?tone":
            await message.channel.send(handler.what_tone(message.content))
        case "t?ind":
            await message.channel.send(handler.mean_ind(message.content))
        case _:
            line = handler.tone_used(message.content)
            if line != "":
                await message.reply(line, mention_author=False)


# loop
bot.run(os.environ["TOKEN"])
