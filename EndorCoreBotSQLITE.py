#################################
# Import Modules ##############################################################################################################################
#################################
import json
import logging
import os
import random
from datetime import datetime
import discord
from discord.ext import commands, tasks
import Moudles.asqlite as asqlite

with open(r"config.json") as f:
    data = json.load(f)
    
    

#################################
# def thingy ##############################################################################################################################
#################################
def check_if_it_is_me(ctx):
    return ctx.message.author.id == 668304274580701202 


#@tasks.loop(hours=24)
async def Mood_roller_coster_time():
    rand_roller_mood_time = random.randrange(1,100000)
    client.mood_time = 0
    return rand_roller_mood_time 



#################################
# client (EndorCore Bot) ##############################################################################################################################
#################################
intents = discord.Intents.default()  
intents.members = True 
intents.presences = True 
intents.messages = True 
client = commands.Bot(command_prefix ='>', intents=intents)
client.mood = None
client.mood_time = 0
client.revenge_mode = False 
client.revenge_user = None 
client.revenge_del = False 
client.launch_time = datetime.utcnow()
client.del_time = 0 
client.restart = False 
client.db = None 
client.remove_command('help') 
token = data["TOKEN"]


async def initionalize():
    await client.wait_until_ready()
    client.db = await asqlite.connect("Databases/servers.db")
        
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='Moudles/discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
        
@client.command()
@commands.check(check_if_it_is_me)
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.message.channel.send(f"Loaded {extension}")

@client.command()
@commands.check(check_if_it_is_me)
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.message.channel.send(f"unloaded {extension}")
    
@client.command()
@commands.check(check_if_it_is_me)
async def reload(ctx, extension):
    client.reload_extension(f'cogs.{extension}')
    await ctx.message.channel.send(f"Reloaded {extension}")
    

#################################
# Run EndorCore on Servers ##############################################################################################################################
#################################
client.loop.create_task(initionalize())
client.run(token)








