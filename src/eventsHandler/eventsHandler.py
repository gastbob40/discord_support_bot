import discord
import yaml
from src.eventsHandler.on_ready.on_ready import OnReady
from src.eventsHandler.on_message.on_message import OnMessage


class EventsHandler:
    @staticmethod
    def on_ready(client: discord.Client):
        OnReady.login_information(client)

    @staticmethod
    async def on_message(client: discord.Client, message: discord.Message):
        await OnMessage.run(client, message)



