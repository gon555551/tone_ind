import interactions
from info import tones, token

tones, token = tones(), token()

bot = interactions.Client(token=token)



bot.start()
