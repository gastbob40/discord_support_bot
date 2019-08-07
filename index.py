import yaml
import discord
from src.eventsHandler.eventsHandler import EventsHandler

# Get configuration
with open('run/config/config.yml', 'r') as file:
    config = yaml.safe_load(file)

client = discord.Client()


@client.event
async def on_ready():
    EventsHandler.on_ready(client)


@client.event
async def on_message(message: discord.Message):
    await EventsHandler.on_message(client, message)


client.run(config['token'])
