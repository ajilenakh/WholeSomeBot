import nextcord
from nextcord.ext import commands

class moderation(commands.Cog):
    def __init__(self,bot):
        self.bot= bot
        
    @nextcord.slash_command(guild_ids=[1062474098418139256])
    async def ban(self, interaction: nextcord.integrations, member: None, reason: None):
        query = await member
        query = await reason
        
    def setup(bot):
        bot.add_cog(moderation(bot))