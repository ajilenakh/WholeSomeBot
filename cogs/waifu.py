import requests
import os
import dotenv
from dotenv import load_dotenv
import nextcord
from nextcord.ext import commands

load_dotenv()

def api_request(msg, author, userName):
    url = "https://waifu.p.rapidapi.com/path"

    payload = {
        "user_id": str(author),
        "message": msg,
        "from_name": str(userName),
        "to_name": "Girl",
        "situation": f"Girl loves {userName}.",
        "translate_from": "auto",
        "translate_to": "eng"
    }

    headers = {
        "X-RapidAPI-Key": os.getenv("waifu_key"),
        "X-RapidAPI-Host": "waifu.p.rapidapi.com"
    }

    try:
        response = requests.post(url, headers=headers, params=payload)
        response.raise_for_status()  # Raise an exception if the request was not successful

        return response.json()
    except requests.exceptions.RequestException as e:
        # Handle any request-related exceptions here
        print(f"Error: {e}")
        return {"error": "Request failed"}

class waifu_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(guild_ids=[1062474098418139256])
    async def waifu(self, interaction: nextcord.Interaction, msg:str):
        userName = str(interaction.user)
        waifu_response = api_request(msg, interaction.user.id, userName)
        print("Waifu API Response:", waifu_response) 
        await interaction.response.send_message(f"{userName}: {msg}")
        await interaction.followup.send(f"Waifu: {waifu_response}")
        
def setup(bot):
    bot.add_cog(waifu_cog(bot))
