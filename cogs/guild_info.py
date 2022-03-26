import discord
from discord.ext import commands

class GuildInfoCommand(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command(aliases = ["serverinfo"])
	async def guildinfo(self, ctx):
		card = discord.Embed(
			title = f"{ctx.guild.name}'s Info",
			color = 0xff0000
		).set_thumbnail(
			url = ctx.guild.icon_url
		).add_field(
			name = "ID",
			value = ctx.guild.id,
			inline = False
		).add_field(
			name = "Date Created",
			value = ctx.guild.created_at.strftime("%B %d, %Y at %H:%m"),
			inline = False
		).add_field(
			name = "Owner",
			value = ctx.guild.owner,
			inline = False
		).add_field(
			name = "Members",
			value = ctx.guild.member_count,
			inline = True
		).add_field(
			name = "Channels",
			value = len(ctx.guild.channels),
			inline = True
		).add_field(
			name = "Region",
			value = ctx.guild.region,
			inline = True
		).set_footer(
			text = ctx.author,
			icon_url = ctx.author.avatar_url
		)

		await ctx.send(embed = card)

def setup(client):
	client.add_cog(GuildInfoCommand(client))
