import chie_utils
import discord
import logging
from discord.ext import commands

class BanCommand(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command()
	@commands.has_permissions(ban_members = True)
	async def ban(self, ctx, member:discord.Member, *, reason=None):
		try:
			await member.ban(reason=reason)
			chie_utils.log_event(__name__, logging.INFO, f"{ctx.author} banned {member} for '{reason}' in {ctx.guild}")
			await ctx.send(f"{member} has been banned. Reason: `{reason}`")
		except TypeError:
			await ctx.send("Invalid user.")

def setup(client):
	client.add_cog(BanCommand(client))
