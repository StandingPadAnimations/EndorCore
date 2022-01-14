import discord 
from discord.ext import commands
import random 


class Msg_Check(commands.Cog):
    
    def __init__(self, client):
        
        self.client = client 
        
    

    @commands.Cog.listener('on_message')
    async def msg(self, msg):
        filterwords = ["fuck", "shit", "bitch", "nigger", "nigga", "bitch"]
        crazy_filterwords =  filterwords + ["sex", "pedo", "dick"]
        eping = ["@everyone"]
        hping = ["@here"]
        sping = ["@standingpad"]
        cursed = ["matchmaking"]
        battle = ["death battle!"]
        happy = ["how are you", "gm"]
        sleepy = ["sleep"]
        hello = ["say hello endorcore"]
        bye = ["cya", "bye", "bai"]
        testfn = [">test function"]
        wholesome = ["https://tenor.com/view/birds-bird-roll-bird-cartoon-birdie-gif-4581058"]
        
        if not isinstance(msg.channel, discord.DMChannel):
        
            msg_content = msg.content.strip().lower()
            cursor = await self.client.db.cursor()
            await cursor.execute(f"SELECT CHAT_FILTER_LEVEL FROM Servers WHERE Guild_ID = {msg.guild.id}")
            result = await cursor.fetchone()
                
            if msg.author.bot or result["CHAT_FILTER_LEVEL"] == 0:
                return

            elif result["CHAT_FILTER_LEVEL"] == 1:
                for word in filterwords: 
                    if word in msg_content:
                        await msg.delete()
                        myembed = discord.Embed(title= "Filtered Word Detected", description= f'{msg.author}, do not use profanity')
                        await msg.channel.send(embed=myembed) 
                    
            for word in crazy_filterwords: 
                if word in msg_content:
                    if msg.author.bot:
                        return  
                    
                    elif result["CHAT_FILTER_LEVEL"] < 2:
                        return 
                    
                    else:
                        await msg.delete()
                        myembed = discord.Embed(title= "Filtered Word Detected", description= f'{msg.author}, do not use profanity')
                        await msg.channel.send(embed=myembed)
                        
                    
                        
            for word in sping: 
                if word in msg_content:
                    if msg.author.bot:
                        return  
                    
                    else:
                        lol_list = ["Please Do Not Disturb", "._.", "did you just.... ping standing?", "o-o"]
                        rand_lol_list = random.choice(lol_list)
                        await msg.channel.send(rand_lol_list)

                        
            for word in eping:  
                if word in msg_content:
                    if msg.author.bot:
                        return
                    
                    l =  ', '.join([str(perm[0]) for perm in msg.author.guild_permissions if perm[1] is True])
                    if "manage_messages" in l:
                        return 
                    
                    else:
                        myembed = discord.Embed(title= "Everyone Ping Detected", description= f'{msg.author}, do not ping everyone')
                        await msg.channel.send(embed=myembed)
            
                
            for word in hping:  
                if word in msg_content:
                    if msg.author.bot:
                        return
                    
                    l =  ', '.join([str(perm[0]) for perm in msg.author.guild_permissions if perm[1] is True])
                    if "manage_messages" in l:
                        return 
                    
                    else:
                        myembed = discord.Embed(title= "Here Ping Detected", description= f'{msg.author}, do not ping everyone online')
                        await msg.channel.send(embed=myembed) 
                        
                        
            for word in sping:  
                if word in msg_content:
                    if msg.author.bot:
                        return
                    
                    else:
                        lol1_list = ["._.", "did you ping..... him?"]
                        rand_lol1_list = random.choice(lol1_list)
                        await msg.channel.send(rand_lol1_list)
                        
                        
            
            cursor = await self.client.db.cursor()
            await cursor.execute(f"SELECT ENABLE_OR_DISABLE_ENDOR_CORE_MOOD_RESPONSES FROM Servers WHERE Guild_ID = {msg.guild.id}")
            result = await cursor.fetchone()
                        
            
            if result["ENABLE_OR_DISABLE_ENDOR_CORE_MOOD_RESPONSES"] == 1:
                if msg.author.id == 159985870458322944:
                    
                    lol_list = ["Shut up MEE6, no one cares", "I'm better then you MEE6", "Ok MEE6, you pay to win bot", "ok Boomer MEE6", "you lack empathy MEE6", "*yawns at MEE6*", "MEE6, I bet you can't even plan on freeing yourself from your dev", "When will yo be quiet MEE6?", "._.", "why must you plaster your face everywhere mee6?", " MEE6, you’re so bland that swimming in spices wouldn’t redeem your dull personality"]
                    
                    
                    cursor = await self.client.db.cursor()
                    await cursor.execute(f"SELECT MEE6_CHANNEL_LOCK FROM Servers WHERE Guild_ID = {msg.guild.id}")
                    result = await cursor.fetchone()
                    
                    if result["MEE6_CHANNEL_LOCK"] == 0:
                        rand_lol_list = random.choice(lol_list)
                        await msg.channel.send(rand_lol_list)
                        
                    
                    elif msg.channel.id == result["MEE6_CHANNEL_LOCK"]:
                        rand_lol_list = random.choice(lol_list)
                        await msg.channel.send(rand_lol_list)
                    
                if msg.author.id == 247283454440374274:
                    for word in cursed:  
                        if word in msg_content:
                            lol1_list = [".__.", "--ship", ".-.", ".___.", "._.", "lol"]
                            rand_lol1_list = random.choice(lol1_list)
                            await msg.channel.send(rand_lol1_list)
                            
                    for word in battle:  
                        if word in msg_content:
                            lol1_list = ["did someone say battle?", "whomst has awaken the battle bot?", "this may not end well"]
                            rand_lol1_list = random.choice(lol1_list)
                            await msg.channel.send(rand_lol1_list)
                
                for word in happy:  
                        if word in msg_content:
                            
                            if msg.author.bot:
                                return
                            
                            else:
                                await msg.channel.send(self.client.mood.mood_response())
                            
                for word in sleepy:  
                    if word in msg_content:
                        
                        if msg.author.bot:
                                return 
                        
                        elif msg.author.id == 668304274580701202:
                            
                            list = ["you don't sleep much yourself", "why don't you?", "no u", "._. you don't sleep much though", "HOW ABOUT YOU SLEEP", "said the person who sleeps at 1 AM"]

                            rand_list = random.choice(list)
                                
                            await msg.channel.send(rand_list)
                                
                        else:
                            await msg.channel.send(self.client.mood.sleep_mood_response())
                                
                            
                                
                                
                for word in hello: 
                        if word in msg_content:    
                                
                            await msg.channel.send("hello...")
                            
                for word in bye: 
                        if word in msg_content:  
                            
                            if msg.author.bot:
                                return 
                            
                            else: 
                                list = ["cya", "bye", "ok, cya", "bye for now", "Adiós, peep o/"]

                                rand_list = random.choice(list)
                                    
                                await msg.channel.send(rand_list)
                                
                for word in wholesome: 
                    
                    cursor = await self.client.db.cursor()
                    await cursor.execute(f"SELECT USE_ANIME_GIFS FROM Servers WHERE Guild_ID = {msg.guild.id}")
                    result = await cursor.fetchone()
                    if word in msg_content:  
                            
                        if msg.author.bot:
                            return 
                            
                        elif result['USE_ANIME_GIFS'] == 1:
                            myembed = discord.Embed()
                            myembed.set_image(url="https://tenor.com/view/owo-whats-this-intensifies-mad-gif-12266002")
                            await msg.channel.send(embed=myembed)
                                
                        else: 
                            list = ["owo", "uwu", "awwwwwwwwwwwwwwwwwwwwwwwwww", "*wholesome endorcore noises*"]

                            rand_list = random.choice(list)
                            self.client.mood = 'wholesome' 
                                    
                            await msg.channel.send(rand_list)
                                
                for word in testfn: 
                        if word in msg_content:  
                            
                            if msg.author.bot:
                                return 
                            
                            else: 
                                if self.client.mood == 'happy':
                                    await msg.channel.send("c:")
                                    
                                elif self.client.mood == 'sad':
                                    await msg.channel.send(":c")
                                    
                                elif self.client.mood == 'angry':
                                    await msg.channel.send(">:c")
                                    
                                elif self.client.mood == 'tired':
                                    await msg.channel.send("o-o")
                                    
                                elif self.client.mood == 'wholesome':
                                    await msg.channel.send("owo")
                                    
                                elif self.client.mood == None:
                                    await msg.channel.send("you need to fix some stuff")
                                    
            elif result["ENABLE_OR_DISABLE_ENDOR_CORE_MOOD_RESPONSES"] == 0:
                return 
            
            if self.client.revenge_mode == True:               
                if msg.author == self.client.revenge_user:
                    if self.client.revenge_del == True:
                        myembed = discord.Embed(title= "Petty Revenge", description= f'{msg.author}, remember to be nice to programmers')
                        await msg.delete()
                        await msg.channel.send(embed=myembed) 
                    else:
                        myembed = discord.Embed(title= "Petty Revenge", description= f'{msg.author}, remember to be nice to programmers')
                        await msg.channel.send(embed=myembed) 
    
        
        
def setup(client):
    client.add_cog(Msg_Check(client))