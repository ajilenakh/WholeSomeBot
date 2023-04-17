import wavelinkcord as wavelink
import nextcord
from nextcord.ext import commands


class music_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(guild_ids=[1062474098418139256])
    async def play(self, interaction: nextcord.Interaction, search: str):
        query = await wavelink.YouTubeTrack.search(search, return_first=True)
        destination = interaction.user.voice.channel

        if not interaction.guild.voice_client:
            vc: wavelink.Player = await destination.connect(cls=wavelink.Player)
        else:
            vc: wavelink.Player = interaction.guild.voice_client

        if vc.queue.is_empty and not vc.is_playing():
            await vc.play(query)
            await interaction.response.send_message(f"Now Playing {vc.current.title}")
        else:
            await vc.queue.put_wait(query)
            await interaction.response.send_message(f"Song was added to the queue")

    @nextcord.slash_command(guild_ids=[1062474098418139256])
    async def skip(self, interaction: nextcord.Interaction):
        vc: wavelink.Player = interaction.guild.voice_client
        await vc.stop()
        await interaction.response.send_message(f"Song was skipped!!")

    @nextcord.slash_command(guild_ids=[1062474098418139256])
    async def pause(self, interaction: nextcord.Interaction):
        vc: wavelink.Player = interaction.guild.voice_client
        if vc.is_playing():
            await vc.pause()
            await interaction.response.send_message(f"Song was paused.")
        else:
            await interaction.response.send_message(f"Song is already paused!")

    @nextcord.slash_command(guild_ids=[1062474098418139256])
    async def resume(self, interaction: nextcord.Interaction):
        vc: wavelink.Player = interaction.guild.voice_client
        if vc.is_paused():
            await vc.resume()
            await interaction.response.send_message(f"Song is resumed.")
        else:
            await interaction.response.send_message(f"The song is already playing!")

    @nextcord.slash_command(guild_ids=[1062474098418139256])
    async def disconnect(self, interaction: nextcord.Interaction):
        vc: wavelink.Player = interaction.guild.voice_client
        await vc.disconnect()
        await interaction.response.send_message(f"I am disconnecting :D")

    @nextcord.slash_command(guild_ids=[1062474098418139256])
    async def queue(self, interaction: nextcord.Interaction):
        vc: wavelink.Player = interaction.guild.voice_client
        if not vc.queue.is_empty:
            song_counter = 0
            songs = []
            queue = vc.queue.copy()
            embed = nextcord.Embed(title="Queue")
            for song in queue:
                song_counter += 1
                songs.append(song)
                embed.add_field(name=f"[{song_counter}] Duration {song.duration}", value=f"{song.title}", inline=False)
            await interaction.response.send_message(embed=embed)
        else:
            await interaction.response.send_message("The queue is empty!")

def setup(bot):
    bot.add_cog(music_cog(bot))