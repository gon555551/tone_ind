# TONE INDICATOR DISCORD BOT

Scripts for a code indicator bot using [discord-py](https://github.com/Rapptz/discord.py) and [masterlist](https://toneindicators.carrd.co/#masterlist).

Simply use a tone indicator, like ``/srs``, anywhere in your message (as long as it's separated from other words with a space), and a message will be sent in the same channel explaining what it means. The message will be a reply without mentioning the user.
Only reads the first tone indicator used.

Available commands\*:
- ``t?all``: get a DM with the use-explanation
- ``t?what TONE``: displays the indicator for the specified tone
- ``t?mean IND``: displays the tone of the specified indicator

\*doesn't actually implement ``commands.Command()``, only message parsing.
