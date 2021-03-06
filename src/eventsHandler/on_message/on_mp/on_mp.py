import textwrap
from datetime import datetime

import discord
import yaml

from src.models.models import session, Channel


async def on_mp(client: discord.Client, message: discord.Message):
    with open('run/config/config.yml', 'r') as file:
        config = yaml.safe_load(file)

    author: discord.User = message.author
    link: Channel = session.query(Channel).filter_by(author_id=author.id).first()

    if not link:
        # Pas encore connecté
        now = datetime.now()
        topic = f"Username : {author.name}#{author.discriminator}\n" \
                f"ID : {author.id}\n" \
                f"Conversation commencé le : {now.day}/{now.month}/{now.year} à {now.hour}:{now.minute}"

        channel = await client.get_guild(config['guild_id']).create_text_channel(
            author.name[:10],
            category=client.get_guild(config['guild_id']).get_channel(config['category_id']),
            topic=topic
        )

        link = Channel(author.id, channel.id)
        session.add(link)
        session.commit()

        await message.channel.send("Merci pour votre message! "
                                   "Notre équipe de modérateurs vous répondra dans les plus brefs délais.\n"
                                   "Tous les messages que vous posterez ici (y compris votre précédent message), "
                                   "sera retransmis au staff.")

        await client.get_channel(link.channel_id).send(f"**Une discussion vient de commencer avec "
                                                       f"{author.name}#{author.discriminator} | {author.id}.**")

    if message.content:
        await client.get_channel(link.channel_id).send(message.content)

    for attachment in message.attachments:
        await client.get_channel(link.channel_id).send(attachment.proxy_url)

    await message.add_reaction('📨')
