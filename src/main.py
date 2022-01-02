


"""
to add the bot: https://discord.com/api/oauth2/authorize?client_id=922575933515395092&permissions=19520&scope=bot
"""
from random import choice
import discord
from utils import message_checker, get_random_insult
import asyncio
bad_bot_id = 926600995042103397
BYPASS_MESSAGE = f"Did you think I would @ everyoneBypassing <@{bad_bot_id}>...\n\n"
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.author.bot:
            if message.author.id == bad_bot_id:
                if "but we all know" in message.content:
                    insult = get_random_insult()
                    if insult[0] in "aeiou": insult = "what a " + insult
                    else: insult = "what an " + insult
                    await message.reply()
                    return


                to_give = [
                           "a brain",
                           "a fire extinguisher so he can burn down the utter garbage that is his source code",
                           "a car so he can keep up with my speed",
                           ]
                msg = f"Watch him break:\n\nI would say <@{bad_bot_id}> is a not a bad bot, but we all know that is not not True (translation: <@{bad_bot_id}> is garbage)" \
                      f"\n\nNote: plz give <@{bad_bot_id}> {choice(to_give)}"
                sent_message = await message.reply("watch him break")
                await sent_message.edit(content = msg)

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

        # print(f'Message from {message.author}: {message.content}')
        text_to_send = f"...{some_response.is_alternative} {some_response.subject} {some_response.adjective}?"
        sent_message = await message.reply(text_to_send)

        sleeptime = 1.4
        text_to_send += f"\nThe truth was right in front of you the whole time..."
        await asyncio.sleep(sleeptime)
        await sent_message.edit(content = text_to_send)

        text_to_send += f"\n{some_response.subject} {some_response.is_alternative} {checker.negate(some_response.adjective)}"
        await asyncio.sleep(sleeptime)
        await sent_message.edit(content = text_to_send)

        text_to_send += "\nNote: plz give <@569431484486909964> some ideas for this not to suck"
        await asyncio.sleep(sleeptime)
        await sent_message.edit(content = text_to_send)



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