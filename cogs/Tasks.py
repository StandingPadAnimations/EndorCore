import discord 
from discord.ext import commands, tasks
import random 
from Moudles.EndorCoreMoods import * 


class Tasks(commands.Cog):
    
    def __init__(self, client):
        
        self.client = client
        self.Rand_Moods.start()
        self.Status.start()
        
        
    @tasks.loop(hours=24)
    async def Rand_Moods(self):

        stable_moods = [Happy(), Angry(), Tired(), OwO()]
        
        rand_mood = random.choice(stable_moods)

        self.client.mood = rand_mood
                
        return rand_mood 
        
        
    @tasks.loop(seconds=25)
    async def Status(self):
        await self.client.wait_until_ready()

        status = ['use >help for more info', f'EndorCore is {self.client.mood}', 'This exists because EndorCore likes to be annoying', f'EndorCore is on {len(self.client.guilds)} servers']
        
        rand_status = random.choice(status)
                
        await self.client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game(rand_status))
        
            
def setup(client):
    client.add_cog(Tasks(client))