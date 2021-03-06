#   Copyright 2020-2021 Nhalrath
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import discord
import json
import random
import requests
from chieUtils import event_logger as logger
from discord.ext import commands

class SafebooruCommand(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.imageboard = "https://safebooru.donmai.us"

    @commands.command()
    async def safebooru(self, ctx, tag = None):
        def embedBuilder(image, tag):
            embed = discord.Embed(
                title = "Safebooru",
                color = 0x008000,
            )
            embed.add_field(
                name = "Tags",
                value = tag,
                inline = False
            )
            embed.set_image(
                url = image
            )
            embed.set_footer(
                text = ctx.author,
                icon_url = ctx.author.avatar_url
            )

            return embed

        if requests.get(self.imageboard).status_code == 200:
            if tag == None:
                request = requests.get("%s/posts/random.json" % (self.imageboard))
                image = request.json()['file_url']
                tags = "`%s`" % (request.json()['tag_string'].replace(" ", "`, `"))
                embed = embedBuilder(image, tags)

                await ctx.send(embed = embed)
            else:
                request = requests.get("%s/posts/random.json?tags=%s" % (self.imageboard, tag))
                image = request.json()['file_url']
                tags = "`%s`" % (request.json()['tag_string'].replace(" ", "`, `"))
                embed = embedBuilder(image, tags)

                await ctx.send(embed = embed)
        else:
            await ctx.send("There seems to be an error within the **Safebooru** site.")
            logger.INFO(__name__, "There's an error within the Safebooru site.")

def setup(client):
    client.add_cog(SafebooruCommand(client))
