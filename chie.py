#!/bin/python3

import os
import chie_utils
import discord
import json
import logging

from discord.ext import commands

# Config
try:
	with open("./config.json", 'r') as f:
		config = json.load(f)

		USE_SYS_ENV = True if config["USE_SYS_ENV"] else False

		TOKEN			= os.environ["TOKEN"]			if USE_SYS_ENV else config["TOKEN"]
		COMMAND_PREFIX	= os.environ["COMMAND_PREFIX"]	if USE_SYS_ENV else config["COMMAND_PREFIX"]
except KeyError:
	chie_utils.log_event(__name__, logging.ERROR, "Missing 'config.json' or invalid config values")

client = commands.Bot(COMMAND_PREFIX, intents=discord.Intents.all())

client.remove_command("help")

# Load cogs and commands
for cog in os.listdir("./cogs"):
	if cog.endswith(".py"):
		try:
			client.load_extension(f"cogs.{cog[:-3]}")
			chie_utils.log_event(__name__, logging.INFO, f"Loaded cog '{cog[:-3]}'")
		except Exception as e:
			chie_utils.log_event(__name__, logging.ERROR, f"Failed to load cog '{cog}'\n{e}")

@client.event
async def on_ready():
	chie_utils.log_event(__name__, logging.INFO, f"{client.user} is online!")
	await client.change_presence(activity = discord.Activity(type = discord.ActivityType.watching, name = 'over you.'))

client.run(TOKEN)
