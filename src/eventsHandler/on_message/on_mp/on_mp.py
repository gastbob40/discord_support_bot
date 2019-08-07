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
        if message.content != "start":
            await message.channel.send("❌ | Aucune discussion n'est en cours.\n"
                                       "Merci de marquer `start` pour commencer une discussion avec le staff.")
            return

        else:
            now = datetime.now()
            topic = f"Username : {author.name}#{author.discriminator}\n" \
                    f"ID : {author.id}\n" \
                    f"Conversation commencé le : {now.day}/{now.month}/{now.year} à {now.hour}:{now.minute}"

            channel = await client.get_guild(config['guild_id']).create_text_channel(
                textwrap.shorten(author.name, width=10),
                category=client.get_guild(config['guild_id']).get_channel(config['category_id']),
                topic=topic
            )

            link = Channel(author.id, channel.id)
            session.add(link)
            session.commit()

            await message.channel.send("✅ | Une discussion vient de commencer.\n"
                                       "Tout ce que vous posterez ici sera retransmis au staff.")
            await client.get_channel(link.channel_id).send(f"**Une discussion vient de commencer avec "
                                                           f"{author.name}#{author.discriminator} | {author.id}.**")

    else:
        if message.content:
            await client.get_channel(link.channel_id).send(message.content)

        for attachment in message.attachments:
            embed = discord.Embed()
            embed.set_image(url=attachment.proxy_url)
            await client.get_channel(link.channel_id).send(embed=embed)

        await message.add_reaction('📨')
