import discord
from discord.ext import commands 
import Moudles.asqlite as asqlite
import json 
from datetime import datetime
from discord.ext import tasks
from Moudles.EndorCoreMoods import * 


class EndorCore(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        with open(r"config.json") as f:
            data = json.load(f)
            self.dev = data["STANDINGPAD"]
            self.token = data["TOKEN"]
            self.db_filepath = data["DATABASE"]

        self.mood = None
        self.revenge_mode = False 
        self.revenge_user = None 
        self.revenge_del = False 
        self.launch_time = datetime.utcnow()
        self.del_time = 0 
        self.restart = False 
        self.db = None 
        self.remove_command('help') 

        discord_intents = discord.Intents.default()  
        discord_intents.members = True 
        discord_intents.presences = True 
        discord_intents.messages = True 
        commands.Bot.__init__(self, command_prefix = ">", intents=discord_intents)

        self.Rand_Moods.start()
        self.Status.start()

        
    @tasks.loop(hours=24)
    async def Rand_Moods(self):
        stable_moods = [Happy(), Angry(), Tired(), OwO()]
        rand_mood = random.choice(stable_moods)
        self.mood = rand_mood
        return rand_mood 
        
    @tasks.loop(seconds=25)
    async def Status(self):
        await self.wait_until_ready()
        status = ['use >help for more info', f'EndorCore is {self.mood}', 'This exists because EndorCore likes to be annoying', f'EndorCore is on {len(self.guilds)} servers']
        rand_status = random.choice(status)
        await self.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game(rand_status))

    @Rand_Moods.before_loop
    async def initionalize(self):
        await self.wait_until_ready()
        self.db = await asqlite.connect(self.db_filepath)