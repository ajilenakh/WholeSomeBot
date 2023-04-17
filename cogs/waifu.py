import requests
import os
import dotenv
from dotenv import load_dotenv
import nextcord
from nextcord.ext import commands

load_dotenv()

def input(msg, author):
    url = "https://waifu.p.rapidapi.com/path"

    querystring = {"user_id":f"{author}","message":f"{msg}","from_name":f"{userName[:-5]}","to_name":"Waifu","situation":"Waifu loves "+f"{userName[:-5]}"+" .","translate_from":"auto","translate_to":"auto"}

    payload = {}
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": os.getenv("waifu_key"),
        "X-RapidAPI-Host": "waifu.p.rapidapi.com"
    }

    response = requests.request("POST", url, json=payload, headers=headers, params=querystring)

    return(response.text)

class waifu_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @nextcord.slash_command(guild_ids=[1062474098418139256])
    async def waifu(self, interaction: nextcord.Interaction, msg:str):
        global userName
        author = interaction.user
        userName= (f"{author}")
        await interaction.response.send_message(f"{userName[:-5]}: {msg}")
        await interaction.followup.send("Waifu: " + input(msg, author))
        
def setup(bot):
    bot.add_cog(waifu_cog(bot))
