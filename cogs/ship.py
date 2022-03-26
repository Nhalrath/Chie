import discord
import io
import random
import requests

from discord.ext import commands
from PIL import Image, ImageDraw

class ShipCommand(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	def create_card(self, member_a:discord.Member, member_b:discord.Member):
		IMG_HEIGHT = 280
		IMG_WIDTH = 500

		mod = random.randrange(0, 100)

		member_a_avatar = Image.open(io.BytesIO(requests.get(
			member_a.avatar_url_as(format = "png", size = 128)).content))
		member_b_avatar = Image.open(io.BytesIO(requests.get(
			member_b.avatar_url_as(format = "png", size = 128)).content))
		
		card = Image.new(mode = "RGB", size = (IMG_WIDTH, IMG_HEIGHT), color = (255, 192, 203))
		i_ctx = ImageDraw.Draw(card)

		card.paste(member_a_avatar, (30, 58))
		card.paste(member_b_avatar, ((IMG_WIDTH - member_b_avatar.width - 30), 58))

		i_ctx.text(
			xy = (40, 25),
			text = member_a.display_name,
			fill = (0, 15, 50)
		)

		i_ctx.text(
			xy = ((IMG_WIDTH - (round(28 / 2) * len(member_b.display_name)) - 40), 25),
			text = member_b.display_name,
			fill = (0, 15, 50)
		)

		i_ctx.text(
			xy = ((IMG_WIDTH / 2) - (round(28 / 2)), IMG_HEIGHT - 50 - 38),
			text = f"{mod}%",
			fill = (0, 15, 50)
		)

		i_ctx.rectangle(
			[(50, IMG_HEIGHT - 20),
			(IMG_WIDTH - 50, IMG_HEIGHT - 50)], fill = (40, 40, 60))
		i_ctx.rectangle(
			[(50, IMG_HEIGHT - 20),
			(IMG_WIDTH - 50 - (((100 - mod) / 100) * 400), IMG_HEIGHT - 50)], fill = (150, 255, 150))

		# Would be better if I could save this to memory instead of disk, but I don't know how.
		card.save("card.png", "PNG")

	@commands.command()
	async def ship(self, ctx, member_a:discord.Member=None, member_b:discord.Member=None):
		try:
			if member_a and member_b:
				self.create_card(member_a, member_b)
			elif member_a and not member_b:
				self.create_card(ctx.author, member_a)
			else:
				await ctx.send("Who are you shipping yourself to? Mention a member, please.")
				return

			await ctx.send(file = discord.File("card.png"))
		except commands.errors.MemberNotFound:
			await ctx.send("Please mention a member")

def setup(bot):
	bot.add_cog(ShipCommand(bot))