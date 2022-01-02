


"""
to add the bot: https://discord.com/api/oauth2/authorize?client_id=922575933515395092&permissions=19520&scope=bot
"""

import discord
from utils import message_checker, random_string
import asyncio
bad_bot_id = 926600995042103397
BYPASS_MESSAGE = f"Did you think I would @ everyoneBypassing <@{bad_bot_id}>...\n\n"
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print(message.author.id, type(message.author.id))
        # if message.author.id == bad_bot_id:
        #     await message.reply(BYPASS_MESSAGE + "\n\n\nlmao look at this idiot fail")
        #     return
        if message.author.bot:
            return

        checker = message_checker()
        some_response = checker.valid_message(message.content)
        if some_response.validity == False: return

        if "@everyone" in message.content:
            sent_message = await message.reply("Did you think I would @ everyone? I'm not that dumb")
            return

        #replacing apostorphees:
        some_response.subject = some_response.subject.replace("'m", "am").replace("'re", "are").replace("'s", "is")
        some_response.is_alternative = some_response.is_alternative.replace("'m", "am").replace("'re", "are").replace("'s", "is")
        some_response.adjective = some_response.adjective.replace("'m", "am").replace("'re", "are").replace("'s", "is")

        # Bypassing the opression of https://github.com/Luke-zhang-04/toB-drocsiD-tsiwT-tolP:
        text_to_send = BYPASS_MESSAGE
        # sent_message = await message.reply(text_to_send)
        # await asyncio.sleep()


        text_to_send += f"...{some_response.is_alternative} {some_response.subject} {some_response.adjective}?"
        # sent_message = await message.reply(text_to_send)

        sleeptime = 1.4
        text_to_send += f"\nThe truth was right in front of you the whole time..."
        text_to_send += f"\n{some_response.subject} {some_response.is_alternative} {checker.negate(some_response.adjective)}"
        text_to_send += "\nNote: plz give <@569431484486909964> some ideas for this not to suck"
        sent_message = await message.reply(text_to_send)

        # await asyncio.sleep(sleeptime)
        # await sent_message.edit(content = text_to_send)
        #
        # try:
        #     text_to_send += f"\n{some_response.subject} {some_response.is_alternative} {checker.negate(some_response.adjective)}"
        #     await asyncio.sleep(sleeptime)
        #     await sent_message.edit(content = text_to_send)
        # except: pass #message was removed by Worst Bot
        #
        # try:
        #     text_to_send += "\nNote: plz give <@569431484486909964> some ideas for this not to suck"
        #     await asyncio.sleep(sleeptime)
        #     await sent_message.edit(content = text_to_send)
        # except: pass #message was removed by worst bot



#heroku maintenance:on
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