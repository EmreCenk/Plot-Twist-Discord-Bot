


"""
to add the bot: https://discord.com/api/oauth2/authorize?client_id=922575933515395092&permissions=19520&scope=bot
"""

import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')


if __name__ == '__main__':
    from dotenv import load_dotenv
    load_dotenv()
    from os import environ
    token = environ["DISCORD_TOKEN"]
    client = MyClient()
    client.run(token)