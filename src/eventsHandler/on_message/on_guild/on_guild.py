import asyncio
from typing import List
import discord
import yaml

from src.models.models import Channel, session


async def on_guild(client: discord.Client, message: discord.Message):
    with open('run/config/config.yml', 'r') as file:
        config = yaml.safe_load(file)

    if message.channel.category.id != config['category_id']:
        return

    link: Channel = session.query(Channel).filter_by(channel_id=message.channel.id).first()

    if not link:
        await message.channel.send("❌ | Aucune discussion n'est en cours dans ce salon.")
        return

    if message.content == config['prefix'] + "close":
        current_message: discord.Message = await message.channel.send \
            (f"{message.author.mention} Vous avez décidé de fermer cette discussion.\n"
             f"Confirmer vous ce choix ?")

        await current_message.add_reaction('✅')
        await current_message.add_reaction('❌')

        def check(reaction, user):
            return user == message.author and (str(reaction.emoji) == '✅' or str(reaction.emoji) == '❌')

        try:
            reaction, user = await client.wait_for('reaction_add', timeout=20.0, check=check)
        except asyncio.TimeoutError:
            await message.channel.send(
                f"Vous avez __refusé__ l'arret de la discussion.")
        else:
            if str(reaction.emoji) == '❌':
                await message.channel.send(
                    f"Vous avez __refusé__ l'arret de la discussion.")
                return

            await message.channel.delete()
            await client.get_user(link.author_id).send("Le staff a décidé d'arrêter cette discussion.")

            session.delete(link)
            session.commit()

    else:
        if message.content:
            await client.get_user(link.author_id).send(f"{message.content}")

        for attachment in message.attachments:
            await client.get_user(link.author_id).send(attachment.proxy_url)

        await message.add_reaction('📨')