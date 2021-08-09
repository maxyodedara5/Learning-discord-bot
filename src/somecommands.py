from logging import NOTSET
import discord
import time
from discord import channel
from discord import colour
from discord.ext import commands


class SomeCommands(commands.Cog):
    """Some simple commands"""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.last_msg = None


    @commands.command(name="ping")
    async def ping(self, ctx: commands.Context):
        """Get the bot's current websocket latency."""
        start_time = time.time()
        message = await ctx.send("Testing ping...")
        end_time = time.time()

        await message.edit(content=f"Pong Nw! {round(self.bot.latency * 1000)}ms\n API: {round((end_time-start_time)* 1000)}ms ") 

    @commands.command(name="setstatus")
    async def setstatus(self, ctx:commands.Context, *, text:str):
        """Set the status for bot"""
        await self.bot.change_presence(activity=discord.Game(name=text))

    @commands.Cog.listener()
    async def on_member_join(self, member:discord.Member):
        channel = self.bot.get_channel(578085964333973536)

        if not channel:
            return

        await channel.send(f"Greetings, {member}!")


    @commands.Cog.listener()
    async def on_message_delete(self, message: discord.Message):
        """Storing the last message """
        self.last_msg = message

    @commands.command(name="snipe")
    async def snipe(self, ctx:commands.Context):
        """Command for sniping the deleted messages"""
        if not self.last_msg:
            await ctx.send("There is no message to snipe")
            return

        author = self.last_msg.author
        content = self.last_msg.content

        embed = discord.Embed(title=f"Message from {author}", description = content)
        await ctx.send(embed=embed)
        

    @commands.command(name="fancyembed")
    async def fancyembed(self, ctx:commands.Context):
        """Creates a fancy embed"""
        embed = discord.Embed(title=f"Fancy Embed bruh!", description = "This be a fancy embed man" , colour = 0x14C821)
        embed.set_author(name = "Maxy" , icon_url= "https://avatars.githubusercontent.com/u/17339687?v=4")
        embed.add_field(name="This be Field", value="This be the value for the said field")

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(SomeCommands(bot))