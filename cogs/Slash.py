import discord
from discord.ext import commands, tasks
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option, create_choice
import asyncpraw
import random
import json 

with open(r"config.json") as f:
    data = json.load(f)


class Slash(commands.Cog):
    def __init__(self, client):
        self.client = client
        
        self.reddit = asyncpraw.Reddit(client_id = data["ID"], client_secret = data["SECRET"], username = data["REDDIT_USERNAME"], 
password = data["REDDIT_PASSWORD"], user_agent = data["USER_AGENT"])
        
        self.gen_memes.start()
    
    async def cog_check(self, ctx):
        cursor = await self.client.db.cursor()
        await cursor.execute("SELECT REASON FROM Blacklist WHERE User_ID = ?", (ctx.author.id,))
        result = await cursor.fetchone()
        if result is None:
            return ctx.author.id
        
    @tasks.loop(minutes=5)
    async def gen_memes(self):
        
        self.meme_subs = []
        self.sao_subs = []
        self.anime_subs = []
        
        meme_subreddit = await self.reddit.subreddit("memes")
        sao_subreddit = await self.reddit.subreddit("swordartonlinememes")
        anime_subreddit = await self.reddit.subreddit("Animememes")
        
        meme_hot = meme_subreddit.hot(limit = 1000)
        sao_hot = sao_subreddit.hot(limit = 1000)
        anime_hot = anime_subreddit.hot(limit = 1000)
        
        async for submission in meme_hot:
            self.meme_subs.append(submission)
            
        async for submission in sao_hot:
            self.sao_subs.append(submission)
            
        async for submission in anime_hot:
            self.anime_subs.append(submission)


    @cog_ext.cog_slash(name="test", description="Tests the discord_slash library(though discord.py will gain slash commands in the next update)")
    async def test(self, ctx: SlashContext):
        await ctx.send(".__.\nwait until discord.py adds slash commands")
        
    @cog_ext.cog_slash(name="meme", description="memes but with slash commands", options=[create_option(name="anime_memes", description="sends anime memes", option_type=3, required=False, choices=[create_choice(name="Sword Art Online",value="swordartonlinememes"), create_choice(name="Anime",value="Animememes")])])
    async def meme(self, ctx: SlashContext, anime_memes : str=None):
        
        if anime_memes is not None:
            if anime_memes == "swordartonlinememes":
                random_sub = random.choice(self.sao_subs)
                
            if anime_memes == "Animememes":
                random_sub = random.choice(self.anime_subs)
        else:
            random_sub = random.choice(self.meme_subs)
    
        name = random_sub.title 
        url = random_sub.url 
        
        myembed = discord.Embed (title = name, url = url)
        myembed.set_image(url = url)

        await ctx.send(embed=myembed)

def setup(bot):
    bot.add_cog(Slash(bot))