
import discord
"""
to add the bot: https://discord.com/api/oauth2/authorize?client_id=922575933515395092&permissions=19520&scope=bot
"""
if __name__ == '__main__':
    from dotenv import load_dotenv
    load_dotenv()
    from os import environ
    a = environ["DISCORD_TOKEN"]
    print(a)