import discord
import yaml

from src.eventsHandler.on_message.on_guild.on_guild import on_guild
from src.eventsHandler.on_message.on_mp.on_mp import on_mp


class OnMessage:
    @staticmethod
    async def run(client: discord.Client, message: discord.Message):
        with open('run/config/config.yml', 'r') as file:
            config = yaml.safe_load(file)

        if message.author.bot:
            return

        if not message.guild:
            # dm
            await on_mp(client, message)
        else:
            # In guild
            await on_guild(client, message)
