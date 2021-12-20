


"""
to add the bot: https://discord.com/api/oauth2/authorize?client_id=922575933515395092&permissions=19520&scope=bot
"""

import discord
from utils import valid_message
import asyncio

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.author == self.user:
            return
        is_message_valid = valid_message(message.content)
        if not is_message_valid[0]:
            return

        # print(f'Message from {message.author}: {message.content}')
        text_to_send = "...or is it?"
        sent_message = await message.reply(text_to_send)
        await asyncio.sleep(1)
        await sent_message.edit(content = text_to_send + f"\nperhaps the world isn't {is_message_valid[1]}")


if __name__ == '__main__':
    from dotenv import load_dotenv
    load_dotenv()
    from os import environ
    token = environ["DISCORD_TOKEN"]
    client = MyClient()
    client.run(token)