import discord 
from discord.ext import commands


class Config(commands.Cog):
    
    def __init__(self, client):
        
        self.client = client
        
    async def cog_check(self, ctx):
        cursor = await self.client.db.cursor()
        await cursor.execute("SELECT REASON FROM Blacklist WHERE User_ID = ?", (ctx.author.id,))
        result = await cursor.fetchone()
        if result is None:
            return ctx.author.id 
        
    @commands.command(name= 'disable-del')
    @commands.has_permissions(administrator=True)
    async def disable(self, ctx):
        
        
        cursor = await self.client.db.cursor()
        
    
        await cursor.execute("UPDATE Servers SET ENABLE_OR_DISABLE_ON_MSG_DELETE = ? WHERE Guild_ID = ?", (0, ctx.guild.id))
        await self.client.db.commit()
        

        await ctx.send("Message Delete event thingy disable")
        
        
    @commands.command(name= 'enable-del')
    @commands.has_permissions(manage_messages=True)
    async def enable(self, ctx):
        
        
        cursor = await self.client.db.cursor()
        
    
        await cursor.execute("UPDATE Servers SET ENABLE_OR_DISABLE_ON_MSG_DELETE = ? WHERE Guild_ID = ?", (1, ctx.guild.id))
        await self.client.db.commit()
        

        
        await ctx.send("Message Delete event thingy enabled")
        
    @commands.command(name= 'enable-anime')
    @commands.has_permissions(administrator=True)
    async def enable_anime(self, ctx):
        
        
        cursor = await self.client.db.cursor()
        
    
        await cursor.execute("UPDATE Servers SET USE_ANIME_GIFS = ? WHERE Guild_ID = ?", (1, ctx.guild.id))
        await self.client.db.commit()
        

            
        await ctx.send("Anime mode enabled")
        
    @commands.command(name= 'disable-anime')
    @commands.has_permissions(administrator=True)
    async def disable_anime(self, ctx):
        
        
        cursor = await self.client.db.cursor()
        
    
        await cursor.execute("UPDATE Servers SET USE_ANIME_GIFS = ? WHERE Guild_ID = ?", (0, ctx.guild.id))
        await self.client.db.commit()
        

        
        await ctx.send("Anime mode disabled")
        
        
    @commands.command(name= 'enable-image')
    @commands.has_permissions(administrator=True)
    async def enable_image(self, ctx):
        
        
        cursor = await self.client.db.cursor()
        
    
        await cursor.execute("UPDATE Servers SET USE_IMAGE_FILTER = ? WHERE Guild_ID = ?", (1, ctx.guild.id))
        await self.client.db.commit()
        

            
        await ctx.send("Image filter enabled")
        
    @commands.command(name= 'disable-image')
    @commands.has_permissions(administrator=True)
    async def disable_image(self, ctx):
        
        
        cursor = await self.client.db.cursor()
        
    
        await cursor.execute("UPDATE Servers SET USE_IMAGE_FILTER = ? WHERE Guild_ID = ?", (0, ctx.guild.id))
        await self.client.db.commit()
        

        
        await ctx.send("Image filter disabled")
        
    @commands.command(name= 'enable-moods')
    @commands.has_permissions(administrator=True)
    async def enable_moods(self, ctx):
        
        
        cursor = await self.client.db.cursor()
        
    
        await cursor.execute("UPDATE Servers SET ENABLE_OR_DISABLE_ENDOR_CORE_MOOD_RESPONSES = ? WHERE Guild_ID = ?", (1, ctx.guild.id))
        await self.client.db.commit()
        

        
        await ctx.send("Moods enabled")
        
    @commands.command(name= 'disable-moods')
    @commands.has_permissions(administrator=True)
    async def disable_moods(self, ctx):
        
        
        cursor = await self.client.db.cursor()
        
    
        await cursor.execute("UPDATE Servers SET ENABLE_OR_DISABLE_ENDOR_CORE_MOOD_RESPONSES = ? WHERE Guild_ID = ?", (0, ctx.guild.id))
        await self.client.db.commit()
        

        
        await ctx.send("Moods disabled")
        
    @commands.command(name= 'max-strikes')
    @commands.has_permissions(administrator=True)
    async def disable_moods(self, ctx, args : int):
        
        
        cursor = await self.client.db.cursor()
        
    
        await cursor.execute("UPDATE Servers SET MAX_STRIKES = ? WHERE Guild_ID = ?", (args, ctx.guild.id))
        await self.client.db.commit()
        

        
        await ctx.send(f"Max strikes set to {args}")
        
    @commands.command(name= 'chatfilter')
    @commands.has_permissions(administrator=True)
    async def chatfilter(self, ctx, args : int):
        
        
        cursor = await self.client.db.cursor()
        
    
        await cursor.execute("UPDATE Servers SET CHAT_FILTER_LEVEL = ? WHERE Guild_ID = ?", (args, ctx.guild.id))
        await self.client.db.commit()
        

            
        await ctx.send(f"Chat filter level set to {args}")
            
            
    @commands.command(name= 'lock-mee6')
    @commands.has_permissions(administrator=True)
    async def mee6_lock(self, ctx, channel: discord.TextChannel):
        
        
        cursor = await self.client.db.cursor()
        
    
        await cursor.execute("UPDATE Servers SET MEE6_CHANNEL_LOCK = ? WHERE Guild_ID = ?", (channel.id, ctx.guild.id))
        await self.client.db.commit()
        

            
        await ctx.send(f"I will now only roast MEE6 in {channel.mention}")
        
    @commands.command(name= 'reset')
    @commands.has_permissions(administrator=True)
    async def reset(self, ctx):
        
        
        cursor = await self.client.db.cursor()
        await cursor.execute(f"SELECT Guild_ID FROM Servers WHERE Guild_ID = {ctx.guild.id}")
        result = await cursor.fetchone()
        
        if result == None:
        
            
            cursor = await self.client.db.cursor()
                
            sql = f"INSERT INTO Servers(Guild_ID) VALUES({ctx.guild.id})"
            
            await cursor.execute(sql)
            
        else:
            
            cursor = await self.client.db.cursor()
            
            sql_del = f"DELETE FROM Servers WHERE Guild_ID = {ctx.guild.id}"
            
            await cursor.execute(sql_del)
            
            sql = f"INSERT INTO Servers(Guild_ID) VALUES({ctx.guild.id})"
            
            await cursor.execute(sql)
            
        
        await self.client.db.commit()
        await cursor.close()
        
        
        await ctx.send("Server Config Settings Reset")
        
        

        
def setup(client):
    client.add_cog(Config(client))