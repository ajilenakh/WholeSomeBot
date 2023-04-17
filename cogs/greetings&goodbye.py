import nextcord
from run import bot
from nextcord.ext import commands

class greetings_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.get_channel(1094324167869993081)
        if channel is not None:
            await channel.send(f'Welcome {member.mention}. :grin:')
    
    @commands.Cog.listener()        
    async def on_member_remove(self, member):
        guild = bot.get_guild(1062474098418139256)
        channel = guild.get_channel(1094328313427808286)
        if channel is not None:
            await channel.send(f'{member.mention} Just left the server. :cry:')

    @commands.command()
    async def hello(self, ctx, *, member: nextcord.Member = None):
        '''hello command'''
        member = member or ctx.author

        if self._last_member is None or self._last_member.id != member.id:
            await ctx.send(f"Hello there {member.mention}! Welcome to our virtual space :D.")
        else:
            await ctx.send("Hey there! Nice to see you again! Hope you're doing well!")
        self._last_member = member    

def setup(bot):
    bot.add_cog(greetings_cog(bot))
