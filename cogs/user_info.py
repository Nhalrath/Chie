import discord
from discord.ext import commands

class UserInfoCommand(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command(aliases = ["profile"])
	async def userinfo(self, ctx, mention:discord.Member=None):
		def embedBuilder(user):
			embed = discord.Embed(
				title = f"{user.name}'s Profile",
				color = 0xff0000
			).set_thumbnail(
				url = user.avatar_url
			).add_field(
				name = "ID",
				value = user.id,
				inline = False
			).add_field(
				name = "Date Created",
				value = user.created_at.strftime("%B %d, %Y at %H:%m"),
				inline = False
			).set_footer(
				text = ctx.author,
				icon_url = ctx.author.avatar_url
			)

			return embed
		
		if mention == None:
			embed = embedBuilder(ctx.author)
		else:
			embed = embedBuilder(mention)

		await ctx.send(embed = embed)

def setup(client):
	client.add_cog(UserInfoCommand(client))
