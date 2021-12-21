


"""
to add the bot: https://discord.com/api/oauth2/authorize?client_id=922575933515395092&permissions=19520&scope=bot
"""

import discord
from utils import message_checker
import asyncio

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.author == self.user:
            return

        checker = message_checker()
        response = checker.valid_message(message.content)
        if not response.validity:
            return

        # print(f'Message from {message.author}: {message.content}')
        text_to_send = f"...or is {response.adjective}?"
        sent_message = await message.reply(text_to_send)
        await asyncio.sleep(2)
        await sent_message.edit(content = text_to_send + f"{response.is_alternative} {response.noun} {response.adjective}?")


if __name__ == '__main__':
    from dotenv import load_dotenv
    load_dotenv()
    from os import environ
    token = environ["DISCORD_TOKEN"]
    client = MyClient()
    client.run(token)