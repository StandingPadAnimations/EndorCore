import discord 
from discord.ext import commands
from discord.commands import slash_command, permissions

class Help(commands.Cog):
    
    def __init__(self, client):
        
        self.client = client 
        
        
    async def cog_check(self, ctx):
        cursor = await self.client.db.cursor()
        await cursor.execute("SELECT REASON FROM Blacklist WHERE User_ID = ?", (ctx.author.id,))
        result = await cursor.fetchone()
        if result is None:
            return ctx.author.id
        
        
    @slash_command(name='help')
    async def help(self, ctx):
        myembed = discord.Embed (title="Help", color=0x00ff00)
        myembed.add_field(name="shut-up", value= "Tells bot to shut up", inline=False) 
        myembed.add_field(name="hi", value= "Says hi", inline=False)
        myembed.add_field(name="gn", value= "Says gn", inline=False)
        myembed.add_field(name="mod-help", value= "Shows mod commands", inline=False)
        myembed.add_field(name="config-help", value= "Shows config commands", inline=False)
        myembed.add_field(name="meme", value= "**MEMES**", inline=False)
        myembed.add_field(name="poll <question>", value= "Creates a poll", inline=False)
        myembed.add_field(name="cat", value= "**CATS**", inline=False)
        myembed.add_field(name="neko", value= "my favorite gif", inline=False)
        myembed.add_field(name="wiki <anything>", value= "Searches Wikipedia", inline=False)
        myembed.add_field(name="server", value= "Server Info", inline=False)
        myembed.add_field(name="user <member(optional)>", value= "User Info", inline=False)
        myembed.add_field(name="slap", value= "makes bot mad", inline=False)
        myembed.add_field(name="headpat", value= "makes bot happy", inline=False)
        myembed.add_field(name="pytha <number>", value= "some random math", inline=False)
        myembed.add_field(name="prime-list <number>", value= "shows primes in the amount specified", inline=False)
        myembed.add_field(name="primes <number 1> <number 2>", value= "shows how many primes there are between numbers", inline=False)
        myembed.add_field(name="For more info, please visit the wiki:", value= "https://sites.google.com/view/standingpadanimations/Development-Stuff/endorcore-wiki?authuser=0", inline=False)
        await ctx.message.channel.send(embed=myembed)  
        
    @slash_command(name='mod-help')
    @permissions.has_any_role("EndorCoreMod", "Moderator", "Mod")
    async def modhelp(self, ctx):
        myembed = discord.Embed (title="Help", color=discord.Colour.dark_blue())
        myembed.add_field(name="mute <member>", value= "Mutes people", inline=False) 
        myembed.add_field(name="unmute <member>", value= "Unmutes people", inline=False)
        myembed.add_field(name="kick <member> <reason>", value= "Kicks people", inline=False)
        myembed.add_field(name="ban <member or user id> <reason>", value= "Bans people", inline=False)
        myembed.add_field(name="unban <username + numbers>", value= "Unbans people", inline=False)
        myembed.add_field(name="purge <amount>", value= "Clears messages", inline=False)
        myembed.add_field(name="add-role <user> <role>", value= "Adds Roles", inline=False)
        myembed.add_field(name="remove-role <user> <role>", value= "Removes Roles", inline=False)
        myembed.add_field(name="strike <user>", value= "adds one strike", inline=False)
        myembed.add_field(name="pardon <user> <number(if no number is specified, the user is pardoned of all strikes)", value= "removes strikes", inline=False)
        myembed.add_field(name="infractions <user>", value= "shows infractions", inline=False)
        await ctx.message.channel.send(embed=myembed)
        
    @slash_command(name='config-help')
    @permissions.is_owner()
    async def confighelp(self, ctx):
        myembed = discord.Embed (title="Help", color=discord.Colour.dark_blue())
        myembed.add_field(name="disable-del", value= "disables the on message delete command", inline=False)
        myembed.add_field(name="enable-del", value= "enables the on message delete command", inline=False)
        myembed.add_field(name="disable-moods", value= "disables the mood responses", inline=False)
        myembed.add_field(name="enable-moods", value= "enables the mood responses", inline=False)
        myembed.add_field(name="max-strikes <number>", value= "changes max strikes", inline=False)
        myembed.add_field(name="chatfilter <number>", value= "changes chat filter level", inline=False)
        myembed.add_field(name="lock-mee6", value= "locks MEE6 roasts to a specific channel", inline=False)
        myembed.add_field(name="config-settings", value= "shows current settings", inline=False)
        myembed.add_field(name="**EXPERIMENTIAL**", value= "Experimential Features, use at risk!", inline=False)
        myembed.add_field(name="disable-image", value= "disables the image filter", inline=False)
        myembed.add_field(name="enable-image", value= "enables the image filter", inline=False)
        await ctx.message.channel.send(embed=myembed)
        
    @commands.command(name='config-settings')
    @permissions.is_owner()
    async def configset(self, ctx):
        cursor = await self.client.db.cursor()
        await cursor.execute(f"SELECT CHAT_FILTER_LEVEL FROM Servers WHERE Guild_ID = {ctx.guild.id}")
        result = await cursor.fetchone()
        chat_filter = result["CHAT_FILTER_LEVEL"]
        await cursor.execute(f"SELECT ENABLE_OR_DISABLE_ON_MSG_DELETE FROM Servers WHERE Guild_ID = {ctx.guild.id}")
        result = await cursor.fetchone()
        msg_del = result["ENABLE_OR_DISABLE_ON_MSG_DELETE"]
        await cursor.execute(f"SELECT MAX_STRIKES FROM Servers WHERE Guild_ID = {ctx.guild.id}")
        result = await cursor.fetchone()
        strike = result["MAX_STRIKES"]  
        await cursor.execute(f"SELECT ENABLE_OR_DISABLE_ENDOR_CORE_MOOD_RESPONSES FROM Servers WHERE Guild_ID = {ctx.guild.id}")
        result = await cursor.fetchone()
        mood_respond = result["ENABLE_OR_DISABLE_ENDOR_CORE_MOOD_RESPONSES"] 
        await cursor.execute(f"SELECT MEE6_CHANNEL_LOCK FROM Servers WHERE Guild_ID = {ctx.guild.id}")
        result = await cursor.fetchone()
        mee6 = result["MEE6_CHANNEL_LOCK"]
        
        if msg_del == 0:
            msg_embed = "Disabled"
            
        if msg_del == 1:
            msg_embed = "Enabled"
            
        if mood_respond == 0:
            mood_embed = "Disabled"
            
        if mood_respond == 1:
            mood_embed = "Enabled"
            
        if mee6 == 0:
            mee6_embed = "Disabled"
            
        
        myembed = discord.Embed ()
        myembed.add_field(name=f"Chat Filter Level", value= f"{chat_filter}", inline=False)
        myembed.add_field(name=f"Message Del Event", value= f"{msg_embed}", inline=False)
        myembed.add_field(name=f"Max Strikes", value= f"{strike}", inline=False)
        myembed.add_field(name=f"Mood Responses", value= f"{mood_embed}", inline=False)
        myembed.add_field(name=f"MEE6 Roast Channel", value= f"{mee6_embed}", inline=False)
        await ctx.message.channel.send(embed=myembed)


def setup(client):
    client.add_cog(Help(client))