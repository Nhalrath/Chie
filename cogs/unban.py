import chie_utils
import discord
import logging
from discord.ext import commands

class UnbanCommand(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command()
	@commands.has_permissions(ban_members = True)
	async def unban(self, ctx, member:discord.Member):
		try:
			await member.unban()
			chie_utils.log_event(__name__, logging.INFO, f"{ctx.author} unbanned {member} in {ctx.guild}")
			await ctx.send(f"{member} has been unbanned.")
		except TypeError:
			await ctx.send("Invalid user.")

def setup(client):
	client.add_cog(UnbanCommand(client))