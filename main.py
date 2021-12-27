


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
        text_to_send = f"...{response.is_alternative} {response.subject} {response.adjective}?"
        sent_message = await message.reply(text_to_send)

        sleeptime = 1.4
        text_to_send +=  f"\nThe truth was right in front of you the whole time..."
        await asyncio.sleep(sleeptime)
        await sent_message.edit(content = text_to_send)

        text_to_send += f"\n{response.subject} {response.is_alternative} not {response.adjective}"
        await asyncio.sleep(sleeptime)
        await sent_message.edit(content = text_to_send)

        text_to_send += "\nNote: plz give <@569431484486909964> some ideas for this not to suck"
        await asyncio.sleep(sleeptime)
        await sent_message.edit(content = text_to_send)




if __name__ == '__main__':
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        pass #this is fine. it just means we're in production instead of testing.
    from os import environ
    token = environ["DISCORD_TOKEN"]

    client = MyClient()
    client.run(token)