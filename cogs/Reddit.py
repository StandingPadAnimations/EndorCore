import discord 
from discord.ext import commands, tasks 
import asyncpraw
import json 
import asyncio
import random



with open(r"config.json") as f:
    data = json.load(f)



class Reddit(commands.Cog):
    
    def __init__(self, client):
        
        self.client = client 
        
        self.reddit = asyncpraw.Reddit(client_id = data["ID"], client_secret = data["SECRET"], username = data["REDDIT_USERNAME"], 
password = data["REDDIT_PASSWORD"], user_agent = data["USER_AGENT"])
        
        
        self.make_memes.start()
        
        
    @tasks.loop(minutes=5)
    async def make_memes(self):
        
        self.meme_subs = []
        self.cat_subs = []
        self.blend_subs = []
        self.anime_subs = []
        self.fine_collection_of_memes = ['https://media.discordapp.net/attachments/783048785092804628/850547921900273694/0pdqd4tqu8371.png', 'https://media.discordapp.net/attachments/778687491300393031/850146219464327168/gordan_thresholded.png?width=1239&height=701', 'https://images-ext-2.discordapp.net/external/eDgNhgzxUHoehryjkLINIZGtjLYmNa-lY1-yyWUxLfk/https/i.redd.it/32l0louqw3c61.jpg?width=1156&height=701', 'https://images-ext-2.discordapp.net/external/jJxg2rrC1eYKxmy0rI7Ixbvb2EybtfWQTyCZ6kuBjOA/https/i.redd.it/rfwbex5mpwz51.jpg?width=1097&height=701', 'https://images-ext-1.discordapp.net/external/ABHL3dQX8xrUSEMyWTsuZpjC8VUKeYNxm6fakonhD34/https/i.redd.it/flmspa8r6ma51.jpg?width=625&height=701', 'https://images-ext-2.discordapp.net/external/jDo7brhthO6bgXFn1zeBaMhojEVeNIKMZjpUfIFAR28/https/i.redd.it/9kiiyr5l5cn51.jpg', 'https://media.discordapp.net/attachments/783048785092804628/850080429678657597/unknown.png', 'https://media.discordapp.net/attachments/768919909886722109/848304288660848653/unknown.png', 'https://media.discordapp.net/attachments/783048785092804628/850063572176470096/unknown.png', 'https://media.discordapp.net/attachments/783048785092804628/850032834672197642/SPOILER_jny9d65q0x271.png', 'https://media.discordapp.net/attachments/783048785092804628/849956272836313088/Screenshot_20210603-000647_Instagram.png?width=696&height=701', 'https://images-ext-2.discordapp.net/external/6sb-4XQbH-kdNYK_8or5Pzj-35N_laujzOr1-SNHAwA/https/i.redd.it/f9ut261o90h51.jpg?width=415&height=700', ]
        
        meme_subreddit = await self.reddit.subreddit("memes")
        cat_subreddit = await self.reddit.subreddit("cats")
        blender_subreddit  = await self.reddit.subreddit("blender")
        anime_subreddit = await self.reddit.subreddit("Animememes")
        
        meme_hot = meme_subreddit.hot(limit = 1000)
        cat_hot = cat_subreddit.hot(limit = 1000)
        blend_hot = blender_subreddit.hot(limit = 1000)
        anime_hot = anime_subreddit.hot(limit = 1000)
        
        async for submission in meme_hot:
            self.meme_subs.append(submission)
            
        async for submission in cat_hot:
            self.cat_subs.append(submission)
            
        async for submission in blend_hot:
            self.blend_subs.append(submission)
            
        async for submission in anime_hot:
            self.anime_subs.append(submission)
    
    async def cog_check(self, ctx):
        cursor = await self.client.db.cursor()
        await cursor.execute("SELECT REASON FROM Blacklist WHERE User_ID = ?", (ctx.author.id,))
        result = await cursor.fetchone()
        if result is None:
            return ctx.author.id
        
        
    
    @commands.command(name='cat')
    async def cat(self, ctx):
        async with ctx.typing():
            await asyncio.sleep(0.5)
        
        
        random_sub = random.choice(self.cat_subs)
    
        name = random_sub.title 
        url = random_sub.url 
        
        myembed = discord.Embed (title = name, url = url)
        myembed.set_image(url = url)

        await ctx.send(embed=myembed)
        
    @commands.command(name='anime')
    async def anime(self, ctx):
        async with ctx.typing():
            await asyncio.sleep(0.5)
        
        random_sub = random.choice(self.anime_subs)
    
        name = random_sub.title 
        url = random_sub.url 
        
        myembed = discord.Embed (title = name, url = url)
        myembed.set_image(url = url)

        await ctx.send(embed=myembed)
        
    @commands.command(name='meme')
    async def meme(self, ctx):
        async with ctx.typing():
            await asyncio.sleep(0.5)

        random_sub = random.choice(self.meme_subs)
    
        name = random_sub.title 
        url = random_sub.url 
        
        myembed = discord.Embed (title = name, url = url)
        myembed.set_image(url = url)

        await ctx.send(embed=myembed)
        
        
    @commands.command(name='blend')
    async def blend(self, ctx):
        async with ctx.typing():
            await asyncio.sleep(0.5)
            
        random_sub = random.choice(self.blend_subs)
    
        name = random_sub.title 
        url = random_sub.url 
        
        myembed = discord.Embed (title = name, url = url)
        myembed.set_image(url = url)

        await ctx.send(embed=myembed)
        
    @commands.command(name='standing')
    async def standings_fine_collecton_of_memes(self, ctx):
        async with ctx.typing():
            await asyncio.sleep(0.5)
            
        random_sub = random.choice(self.fine_collection_of_memes)
        
        myembed = discord.Embed (title = "from Standing's favorite meme collection")
        myembed.set_image(url = random_sub)

        await ctx.send(embed=myembed)

        
def setup(client):
    client.add_cog(Reddit(client))