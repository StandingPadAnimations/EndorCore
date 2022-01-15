import logging
import os
from discord.commands import slash_command, permissions
from Moudles.EndorCoreClient import EndorCore

client = EndorCore()

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='Logs/discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
        
@slash_command(name='load')
@permissions.permission(user_id=client.dev, permission=True)
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.message.channel.send(f"Loaded {extension}")

@slash_command(name='unload')
@permissions.permission(user_id=client.dev, permission=True)
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.message.channel.send(f"unloaded {extension}")

@slash_command(name='reload')
@permissions.permission(user_id=client.dev, permission=True)
async def reload(ctx, extension):
    client.reload_extension(f'cogs.{extension}')
    await ctx.message.channel.send(f"Reloaded {extension}")


client.run(client.token)








