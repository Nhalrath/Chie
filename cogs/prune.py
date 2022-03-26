import chie_utils
import logging
from discord.ext import commands

class PruneCommand(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command(aliases = ['clrmsg', 'purge'])
	@commands.has_permissions(manage_messages = True)
	async def prune(self, ctx, *, amount=1):
		if amount > 100:
			await ctx.send("Sorry, but I can't handle that amount `max: 100`")
			chie_utils.log_event(__name__, logging.INFO, f"{ctx.author} tried to prune {amount} messages")
		else:
			amount += 1
			await ctx.channel.purge(limit=amount)

def setup(client):
	client.add_cog(PruneCommand(client))
