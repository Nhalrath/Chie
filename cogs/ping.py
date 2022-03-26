import time
from discord.ext import commands

class PingCommand(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command()
	async def ping(self, ctx):
		ws = round(self.client.latency * 1000)
		start = time.time()

		msg = await ctx.send("Pinging...")
		end = time.time()

		await msg.edit(content = f"**Ping:** {round((end - start) * 1000)}ms | **Websocket:** {ws}ms")

def setup(client):
	client.add_cog(PingCommand(client))
