from discord.ext import commands

class ErrorListener(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_command_error(self, ctx, error):
		if isinstance(error, commands.CommandNotFound):
			return

def setup(client):
	client.add_cog(ErrorListener(client))
