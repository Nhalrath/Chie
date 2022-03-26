import chie_utils
import discord
import logging
from discord.ext import commands

class KickCommand(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command()
	@commands.has_permissions(kick_members = True)
	async def kick(self, ctx, member:discord.Member, *, reason=None):
		try:
			await member.kick(reason=reason)
			chie_utils.log_event(__name__, logging.INFO, f"{ctx.author} kicked {member} for '{reason}' in {ctx.guild}")
			await ctx.send(f"{member} has been kicked. Reason: `{reason}`")
		except TypeError:
			await ctx.send("Invalid user.")

def setup(client):
	client.add_cog(KickCommand(client))
