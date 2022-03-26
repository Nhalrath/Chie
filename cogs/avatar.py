import discord
from discord.ext import commands

class AvatarCommand(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command(aliases = ["av"])
	async def avatar(self, ctx, mention:discord.Member=None):
		def create_embed(user):
			return discord.Embed(
				title = f"{user.name}'s Avatar",
				color = 0xff0000
			).set_image(
				url = user.avatar_url
			).set_footer(
				text = ctx.author,
				icon_url = ctx.author.avatar_url
			)

		if mention == None:
			await ctx.send(embed = create_embed(ctx.author))
		else:
			try:
				await ctx.send(embed = create_embed(mention))
			except TypeError:
				await ctx.send("Invalid user.")

def setup(client):
	client.add_cog(AvatarCommand(client))
