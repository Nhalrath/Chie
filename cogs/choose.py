import random
from discord.ext import commands

class ChooseCommand(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command(aliases = ["pick"])
	async def choose(self, ctx, *, choice=None):
		if choice is None:
			await ctx.send("Please provide a choice.")
		else:
			choices = choice.replace(" ","").split(",")
			await ctx.send(f"I choose **{random.choice(choices)}**!")

def setup(client):
	client.add_cog(ChooseCommand(client))
