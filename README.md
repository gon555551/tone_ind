# TONE INDICATOR DISCORD BOT

Scripts for a code indicator bot using discord-py and [masterlist](https://toneindicators.carrd.co/#masterlist).

Send ``t?all`` to get a DM explaining how to use the bot.

Simply use a tone indicator, like ``/srs``, anywhere in your message (as long as it's separated from other words with a space), and a message will be sent in the same channel explaining what it means.
Only reads the first one used.

Available commands\*:
- ``t?all``: get a DM with the use-explanation
- ``t?what TONE``: displays tone indicator for specified tone
- 


\* doesn't actually implement ``commands.Command()``, only message parsing.
