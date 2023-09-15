import nextcord
from nextcord.ext import commands
import os
import wavelinkcord as wavelink
from dotenv import load_dotenv

load_dotenv()

bot = commands.Bot(command_prefix='!',intents = nextcord.Intents.all())
'''
async def on_node():
    node: wavelink.Node = wavelink.Node(uri="http://lavalink.clxud.pro:2333", password="youshallnotpass")
    await wavelink.NodePool.connect(client=bot, nodes=[node])
    wavelink.Player.autoplay = True
'''
for f in os.listdir('WholeSomeBot\cogs'):
    if f.endswith('.py'):
        bot.load_extension(f'cogs.{f[:-3]}')

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
#    bot.loop.create_task(on_node())

bot.run(os.getenv('TOKEN'))