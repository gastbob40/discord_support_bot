from typing import List
import discord
import yaml


async def change_prefix(client: discord.Client, message: discord.Message, args: List[str]):
    with open('run/config/config.yml', 'r') as file:
        config = yaml.safe_load(file)

    if not message.author.guild_permissions.administrator:
        await message.channel.send(f":x: Vous n'avez pas les permissions pour changer le préfix.")
        return

    if len(args) != 1:
        await message.channel.send \
            (f":x: Erreur dans la commande.\nRappel : `{config['prefix']}prefix <nouveau prefix>`")
        return

    await message.channel.send(f"⚙ Le préfix **{config['prefix']}** a été changé par **{args[0]}**.")
    config['prefix'] = args[0]

    with open('run/config/config.yml', 'w', encoding='utf8') as outfile:
        yaml.dump(config, outfile, default_flow_style=False, allow_unicode=True)
