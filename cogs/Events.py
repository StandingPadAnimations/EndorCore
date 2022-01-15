import discord 
from discord.ext import commands
import Moudles.asqlite as asqlite 


class Events(commands.Cog):
    
    def __init__(self, client):
        
        self.client = client 
        
        
    @commands.Cog.listener()
    async def on_connect(self):
        print("EndorCore is connected to Discord")
        
    @commands.Cog.listener()
    async def on_ready(self):
        print("EndorCore is running")
        

    async def initionalize(self):
        await self.client.wait_until_ready()
        self.client.db = await asqlite.connect("servers.db")
        
        
    @commands.Cog.listener() 
    async def on_disconnect(self):
        await self.client.db.close()
        print("Disconected")
        
    
        
    @commands.Cog.listener()
    async def on_resumed(self):
        self.client.db = await asqlite.connect("servers.db")
        print('Reconnected')

    @commands.Cog.listener()
    async def on_message_delete(self, msg):
        
        
        cursor = await self.client.db.cursor()
        await cursor.execute(f"SELECT ENABLE_OR_DISABLE_ON_MSG_DELETE FROM Servers WHERE Guild_ID = {msg.guild.id}")
        result = await cursor.fetchone()
        
        
        if result["ENABLE_OR_DISABLE_ON_MSG_DELETE"] == 0:
            return   
        
        if result["ENABLE_OR_DISABLE_ON_MSG_DELETE"] == 1:
            myembed = discord.Embed(title= "Deleted Message")
            myembed.add_field(name= f'{msg.author} deleted a message(if you want to disable this, just do >disable-del)', value= f'{msg.content}')
            await msg.channel.send(embed=myembed) 
            
            

        if msg.author.id == msg.author.bot:
            pass 
        
        
        

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        
        
        cursor = await self.client.db.cursor()
            
        sql = f"INSERT INTO Servers(Guild_ID) VALUES({guild.id})"
            
            
        await cursor.execute(sql)
        await self.client.db.commit()
        await cursor.close()
        
        endorcore = discord.utils.get(guild.roles, name= "EndorCore")
        await endorcore.edit(position=1)
        
        
    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        
        
        cursor = await self.client.db.cursor()
            
        sql = f"DELETE FROM Servers WHERE Guild_ID = {guild.id}"
            
            
        await cursor.execute(sql)
        await self.client.db.commit()
        await cursor.close()
        


        
def setup(client):
    client.add_cog(Events(client))