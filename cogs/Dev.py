import discord
from discord.errors import NotFound 
from discord.ext import commands
from discord.commands import slash_command, permissions
from datetime import datetime
import os 

import Moudles.asqlite as asqlite 
import asyncio

DEV_ID = 668304274580701202
def check_if_it_is_me(ctx):
    return ctx.message.author.id == 668304274580701202 

def temperature_of_raspberry_pi():
    cpu_temp = os.popen("vcgencmd measure_temp").readline()
    return cpu_temp.replace("temp=", "")

loop = asyncio.get_event_loop()
        
        
class Dev(commands.Cog):
    
    def __init__(self, client):
        
        self.client = client 
    
    @slash_command(name='dev')
    @permissions.permission(user_id=DEV_ID, permission=True)
    async def dev(self, ctx):
        myembed = discord.Embed (title= "Dev Portal", description= f'Welcome back {ctx.author}', color= discord.Colour.blurple())
        myembed.add_field(name= "dev-purge", value= "shuts down client")
        myembed.add_field(name= "kill", value= "kills bot")
        myembed.add_field(name= "pinge", value= "pings everyone")
        myembed.add_field(name= "pingh", value= "pings everyone online")
        myembed.add_field(name= "revenge-on", value= "enables revenge mode")
        myembed.add_field(name= "revenge-off", value= "disables revenge mode")
        myembed.add_field(name= "uptime", value= "shows how long bot has been online")
        myembed.add_field(name= "ping", value= "shows latency")
        myembed.add_field(name= "pi-temp", value= "shows tempurature of Raspberry Pi")
        myembed.add_field(name= "restart", value= "restarts systemd process")
        
        await ctx.respond(embed=myembed)

    @slash_command(name='dev-purge')
    @permissions.permission(user_id=DEV_ID, permission=True)
    async def dev_purge(self, ctx, amount=1):
        await ctx.channel.purge(limit=amount + 1)
        myembed = discord.Embed ()
        myembed.add_field(name= "Purged", value= f'{amount} messages has been deleted', inline=False)
        await ctx.respond(embed=myembed)


    @slash_command(name='kill')
    @permissions.permission(user_id=DEV_ID, permission=True)
    async def shutdown(self, ctx):
        print("shutdown")
        await self.client.db.close()
        myembed = discord.Embed (name= "Shuting Down")
        myembed.add_field(name= "Shut Down", value= f'{ctx.author} has shut down the bot :c', inline=False)
        await ctx.respond(embed=myembed)
        await ctx.bot.logout()
        os.popen("sudo systemctl stop EndorCore_service.service").readline()
    
    @slash_command(name='w-kill')
    @permissions.permission(user_id=DEV_ID, permission=True)
    async def w_shutdown(self, ctx):
        print("shutdown")
        await self.client.db.close()
        myembed = discord.Embed (name= "Shuting Down")
        myembed.add_field(name= "Shut Down", value= f'{ctx.author} has shut down the bot :c', inline=False)
        await ctx.respond(embed=myembed)
        await ctx.bot.logout()   

        
    @slash_command(name='pinge')
    @permissions.permission(user_id=DEV_ID, permission=True)
    async def pinge(self, ctx):
        await ctx.respond("@everyone")
        
    @slash_command(name='pingh')
    @permissions.permission(user_id=DEV_ID, permission=True)
    async def pinge(self, ctx):
        await ctx.respond("@here")
        

    @slash_command(name='revenge-on')
    @permissions.permission(user_id=DEV_ID, permission=True)
    async def revenge_on(self, ctx, member : discord.Member, *, args=None):
        if member == None:
            await ctx.respond("Select a member to revenge")
        
        else:
            if args == None:
                self.client.revenge_mode = True 
                self.client.revenge_user = member 
                await ctx.respond("Revenge Mode Enabled")
            else:
                self.client.revenge_mode = True 
                self.client.revenge_user = member 
                self.client.revenge_del = True 
                await ctx.respond("Revenge Mode Enabled")
        
    @slash_command(name='revenge-off')
    @permissions.permission(user_id=DEV_ID, permission=True)
    async def revenge_off(self, ctx):
        self.client.revenge_mode = False
        self.client.revenge_user = None
        self.client.revenge_del  = False 
        await ctx.respond("Revenge Mode Disabled")
        
    @slash_command(name='uptime')
    @permissions.permission(user_id=DEV_ID, permission=True)
    async def uptime(self, ctx):
        delta_uptime = datetime.utcnow() - self.client.launch_time
        hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)
        await ctx.respond(f"I have been online for {days} days, {hours} hours, {minutes} minutes")
    
    @slash_command(name='ping')
    @permissions.permission(user_id=DEV_ID, permission=True)
    async def ping(self, ctx):
        await ctx.respond(f'My ping to the Raspberry Pi is {round(self.client.latency *1000)} ms')
        
    @slash_command(name='pi-temp')
    @permissions.permission(user_id=DEV_ID, permission=True)
    async def tempurature(self, ctx):
        await ctx.respond(f'The Raspberry Pi is {await loop.run_in_executor(None, temperature_of_raspberry_pi)}')
        
    @slash_command(name='restart')
    @permissions.permission(user_id=DEV_ID, permission=True)
    async def restart(self, ctx):
        await ctx.respond('Restarting...')
        await self.client.db.close()
        os.popen("sudo systemctl restart EndorCore_service").readline()
        
    @slash_command(name='connect')
    @permissions.permission(user_id=DEV_ID, permission=True)
    async def connect(self, ctx):
        self.client.db = await asqlite.connect("Databases/servers.db")
        await ctx.respond("Connected")
        
        
    @slash_command(name='disconnect')
    @permissions.permission(user_id=DEV_ID, permission=True)
    async def disconnect(self, ctx):
        await self.client.db.close()
        await ctx.respond("Disconnected")
        
        
    @slash_command(name='cogs')
    @permissions.permission(user_id=DEV_ID, permission=True)
    async def cogs_check(self, ctx):
        cogs = []
        await ctx.respond("List of cogs")
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                cogs.append(filename[:-3])
        await ctx.respond(cogs)
        
    @slash_command(name='blacklist')
    @permissions.permission(user_id=DEV_ID, permission=True)
    async def blacklist(self, ctx, member : int, *, reason=None):
        if isinstance(member, int):
            try:
                member = await self.client.fetch_user(member)
                cursor = await self.client.db.cursor()
                await cursor.execute("SELECT REASON FROM Blacklist WHERE User_ID = ?", (member.id,))
                result = await cursor.fetchone()
            except NotFound:
                await ctx.message.channel.send(f"{member} not found")
        if result == None:
            if reason == None:
                reason = 'StandingPad got annoyed'
            await ctx.message.channel.send(f"Blacklisted {member}. Reason: {reason}")
            await cursor.execute('INSERT INTO Blacklist(User_ID, REASON) VALUES(?, ?)', (member.id, reason))
            await self.client.db.commit()
            await cursor.close()
            
        else:
            await ctx.message.channel.send(f"{member} is already blacklisted. Reason: {result['REASON']}")
            await cursor.close()
            
    @slash_command(name='unblacklist')
    @permissions.permission(user_id=DEV_ID, permission=True)
    async def unblacklist(self, ctx, member : int):
        if isinstance(member, int):
            try:
                member = await self.client.fetch_user(member)
                cursor = await self.client.db.cursor()
                await cursor.execute("SELECT REASON FROM Blacklist WHERE User_ID = ?", (member.id,))
                result = await cursor.fetchone()
            except NotFound:
                await ctx.message.channel.send(f"{member} not found")
        if result != None:
            await ctx.message.channel.send(f"Removed {member} from blacklist")
            await cursor.execute('DELETE FROM Blacklist WHERE User_ID = ?', (member.id,))
            await self.client.db.commit()
            await cursor.close()
            
def setup(client):
    client.add_cog(Dev(client))
