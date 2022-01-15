from typing import Optional
import discord
from mediawiki import MediaWiki
from discord import File
from discord.ext import commands
from discord.commands import slash_command
from typing import Optional


def wiki_summery(arg):
    wikipedia = MediaWiki()
    result = wikipedia.page(arg, auto_suggest=True)
    define = result.summarize(chars=1000)
    return define


class Misc(commands.Cog):
    def __init__(self, client):
        self.client = client 
        
    async def cog_check(self, ctx):
        cursor = await self.client.db.cursor()
        await cursor.execute("SELECT REASON FROM Blacklist WHERE User_ID = ?", (ctx.author.id,))
        result = await cursor.fetchone()
        if result is None:
            return ctx.author.id
        
    @slash_command(name= 'user')
    async def user(self, ctx, member: Optional[discord.Member]):
            member = member or ctx.author
            myembed = discord.Embed(title="User information", colour=member.colour)
            myembed.set_thumbnail(url=member.avatar_url)
            myembed.add_field(name="Username", value=f"{member}")
            myembed.add_field(name="Joined Discord", value=f'''{member.created_at.strftime("%d/%m/%Y %H:%M:%S")}''', inline= True)
            myembed.add_field(name="Joined Server", value=f'''{member.joined_at.strftime("%d/%m/%Y %H:%M:%S")}''', inline= True)
            myembed.add_field(name="Highest Role", value=f"{member.top_role.mention}", inline= True)
            myembed.add_field(name="Nitro Booster?", value=f"{bool(member.premium_since)}", inline= True)
            myembed.add_field(name="Bot?", value=f"{member.bot}", inline= True)
            myembed.add_field(name="Current Status", value=f"{str(member.status).title()}", inline= True)
            myembed.add_field(name="Current Activity", value=f"{str(member.activity.type).split('.')[-1].title() if member.activity else 'N/A'} {member.activity.name if member.activity else ''}", inline= True)
            await ctx.respond(embed=myembed)
            
    @slash_command(name= 'server')
    async def server(self, ctx):
        myembed = discord.Embed(title= f"{ctx.guild.name}", color= ctx.guild.owner.colour)
        myembed.set_thumbnail(url=f"{ctx.guild.icon_url}")
        myembed.add_field(name= "Region", value= f"{ctx.guild.region}")
        myembed.add_field(name= "Members", value= f"{ctx.guild.member_count}")
        myembed.add_field(name= "Server Owner", value= f"{ctx.guild.owner}", inline= False)
        myembed.set_footer(icon_url=f"{ctx.guild.icon_url}", text= f"Guild ID: {ctx.guild.id}")
        await ctx.respond(embed=myembed)
        
    @slash_command(name= 'wiki')
    async def define(self, ctx, *, arg):
        wiki = await self.client.loop.run_in_executor(None, wiki_summery, arg)
        myembed = discord.Embed(title="According to Wikipedia", description=wiki, colour=discord.Colour.dark_blue())
        await ctx.respond(embed=myembed)
        
    @slash_command(name='neko')
    async def img(self, ctx):
        await ctx.respond(file=File("mp4.gif"))
        
    @slash_command(name='shut-up')
    async def shutup(self, ctx):
        await ctx.respond(":c")
        
    @slash_command(name='hi')
    async def hi(self, ctx):
        await ctx.respond("hi")
        
    @slash_command(name='gn')
    async def gn(self, ctx):
        await ctx.respond("gn")
        
    @slash_command(name='headpat')
    async def headpat(self, ctx):
        self.client.mood = 'happy'
        await ctx.respond("c:") 
    
    @slash_command(name='slap')
    async def slap(self, ctx):
        self.client.mood = 'angry'
        await ctx.respond(">:c") 
        
    @slash_command(name='gm')
    async def gm(self, ctx):
        await ctx.respond("gm")
        
    @slash_command(name='poll')
    async def poll(self, ctx, *, message):
        myembed = discord.Embed(title= "Poll", description= f"{message}")
        await ctx.channel.purge(limit=1)
        msg = await ctx.respond(embed=myembed)
        await msg.add_reaction('👍')
        await msg.add_reaction('👎')  
        
def setup(client):
    client.add_cog(Misc(client))
