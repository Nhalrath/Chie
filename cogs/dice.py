import random
from discord.ext import commands

class DiceCommand(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command(aliases = ["roll"])
	async def dice(self, ctx, face:int=6):
		try:
			await ctx.send(f":game_die: {random.randint(1, face)} (1-{face})")
		except TypeError:
			await ctx.send(f"{face} is not an number.")

def setup(client):
	client.add_cog(DiceCommand(client))
