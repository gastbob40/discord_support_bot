# Discord Support Bot

![Discord](https://img.shields.io/badge/Discord-project-brightgreen)
![python](https://img.shields.io/badge/Language-Python-blueviolet)

This github contains the code to quickly set up a support bot. When a person sends an mp to this bot, this message is forwarded to a discord server, and this by creating a lounge in a category. It will then be possible to answer the person by writing in this room. This bot also retransmits all the files transmitted on both sides.

## Getting Started

These instructions will get you a copy of the project up and running on your machine for testing purposes and production.

### Prerequisites

- [Python 3](https://www.python.org/)
- [A discord bot](https://discordapp.com/developers/applications/)

### Installing

- Download the project from github

```
$ git clone https://github.com/gastbob40/discord_support_bot
```

- Go in the created folder, create an virtual environment and run it

```
$ cd discord_support_bot
$ python3 -m venv venv
$ source venv/Scripts/activate
```

- Install the bot dependencies

```
$ pip install -r requirements.txt
```

### Setup the bot

#### Discord Configuration

You must use a discord server for using this bot. You must also create a category in this server.

#### File Configuration

You can see that the run folder contains another folder, the config folder.

You can see an configuration example, as this:

```
prefix: '?'
token: ~

guild_id: ~
category_id: ~
```

- The `prefix` is the prefix for trigger the bot (for close channels).

- The `token` is the token of your bot. You can get [here](https://discordapp.com/developers/applications/)

- The `guild_id` is the id of the guild where the bot will send messages. You must activate the `Developer Mode` option in your discord. After, right click of the guild icon to get its id.

- The `category_id` is the id of the category where the bot will create channels. You can get it by right clicking on a category.

#### Run the Bot

You will have just to start the bot, by tapping:

```
python index.py
```

## Bot's Commands.

This bot doesn't have much command. You can just type `[prefix]close` in a channel to close it.

# Credits

Discord Support Bot was developed by gastbob40.