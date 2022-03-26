import discord
import requests

from discord.ext import commands

class UrbanCommand(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command()
	async def urban(self, ctx, term, index:int=None):
		data = requests.get(f"https://api.urbandictionary.com/v0/define?term={term}").json().get("list")

		if term is None:
			await ctx.send("Please specify a term.")
			return

		if index == None:
			count = 1

			card = discord.Embed(
				title = "Results",
				color = 0xffa500
			)

			for entry in data:
				card.add_field(
					name = f"[{count}] {entry['word']}",
					value = f"*{entry['definition'][0:50]}...*",
					inline = False
				)

				count += 1
		else:
			card = discord.Embed(
				title = f"{data[index-1]['word']}",
				color = 0xffa500
			).add_field(
				name = "Definition",
				value = f"*{data[index-1]['definition']}*",
				inline = False
			)

		await ctx.send(embed = card)

def setup(client):
	client.add_cog(UrbanCommand(client))
