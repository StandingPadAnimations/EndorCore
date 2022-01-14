import discord 
from discord.ext import commands


class Rant(commands.Cog):
    
    def __init__(self, client):
        
        self.client = client 
        
        self.inputs = ['hello']
        self.outputs = []
        
        self.dm_enable = 1
        
    @commands.Cog.listener('on_message')
    async def rant(self, msg):
        if isinstance(msg.channel, discord.DMChannel):
            if msg.author.bot:
                return
            
            elif msg.author.id == 668304274580701202:
                return 
            
            else:
                if self.dm_enable == 1:
                    user = await self.client.fetch_user(668304274580701202)
                    await user.send(f'{msg.author.id}: {msg.content}')
                    
                else:
                    return 
            
    @commands.command(name='dm')
    async def dm(self, ctx, user_id : int, *, msg):
        user = await self.client.fetch_user(user_id)
        await user.send(msg)
        self.dm_enable = 1 
        
    @commands.command(name='off')
    async def dm_off(self, ctx, user_id : int, *, msg):
        user = await self.client.fetch_user(user_id)
        await user.send(msg)
        self.dm_enable = 0

def setup(client):
    client.add_cog(Rant(client))