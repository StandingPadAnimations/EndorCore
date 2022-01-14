import discord
from discord import permissions 
from discord.ext import commands
from discord.commands import slash_command, permissions
from typing import Optional, Union


class Mod(commands.Cog):
    def __init__(self, client):
        
        self.client = client
        
    async def cog_check(self, ctx):
        cursor = await self.client.db.cursor()
        await cursor.execute("SELECT REASON FROM Blacklist WHERE User_ID = ?", (ctx.author.id,))
        result = await cursor.fetchone()
        if result is None:
            return ctx.author.id 
    
    
    @slash_command(name='kick')
    @permissions.has_any_role("EndorCoreMod", "Moderator", "Mod")
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        if reason == None:
            reason = "For being a -----" 

        if member.top_role > ctx.author.top_role:
            myembed = discord.Embed ()
            myembed.add_field(name=f'{member} is above you', value= "You can only kick people below your role", inline=False)
            await ctx.send(embed=myembed)         
            return 
        
        if member.top_role == ctx.author.top_role:
            myembed = discord.Embed ()
            myembed.add_field(name=f'{member} is equal you', value= "You can only kick people below your role", inline=False)
            await ctx.send(embed=myembed)         
            return
        
        
        
        if member.guild_permissions.kick_members == True:
            myembed = discord.Embed ()
            myembed.add_field(name="Kick Permission Detected", value= "Cannot kick a user with moderator perms!", inline=False)
            return await ctx.send(embed=myembed)
        
        else:
            myembed = discord.Embed ()
            myembed.add_field(name=f'{member} has been kicked', value= f'Reason: {reason}', inline=False)
            await ctx.member.send(embed=myembed)
            await member.kick(reason=reason)
            await ctx.send(embed=myembed)
                
        
        
    @slash_command(name='ban')
    @permissions.has_any_role("EndorCoreMod", "Moderator", "Mod")
    async def ban(self, ctx, member, *, reason=None):
        if reason == None:
            reason = "For being a -----" 
        
        if isinstance(member, discord.Member):
            
            member = ctx.guild.get_member(member.id)
            
            if member != None:
                if member.top_role > ctx.author.top_role:
                    myembed = discord.Embed ()
                    myembed.add_field(name=f'{member} is above you', value= "You can only ban people below your role", inline=False)
                    await ctx.send(embed=myembed)         
                    return 
                
                elif member.top_role == ctx.author.top_role:
                    myembed = discord.Embed ()
                    myembed.add_field(name=f'{member} is equal you', value= "You can only ban people below your role", inline=False)
                    await ctx.send(embed=myembed)         
                    return
                
                elif member.guild_permissions.ban_members == True:
                    myembed = discord.Embed ()
                    myembed.add_field(name="Ban Permission Detected", value= "Cannot ban a user with moderator perms!", inline=False)
                    return await ctx.send(embed=myembed)
            
                else:
                    myembed = discord.Embed ()
                    myembed.add_field(name=f'{member} has been banned', value= f'Reason: {reason}', inline=False)
                    await ctx.member.send(embed=myembed)
                    await member.ban(reason=reason)
                    await ctx.send(embed=myembed)
                    
            else:
                user = await self.client.fetch_user(member.id)
                await ctx.guild.ban(user, reason=reason, delete_message_days=0)
                myembed = discord.Embed ()
                myembed.add_field(name=f'{member} has been banned', value= f'Reason: {reason}', inline=False)
                await ctx.send(embed=myembed)
        else:
            user = await self.client.fetch_user(member)
            await ctx.guild.ban(user, reason=reason, delete_message_days=0)
            myembed = discord.Embed ()
            myembed.add_field(name=f'{member} has been banned', value= f'Reason: {reason}', inline=False)
            await ctx.send(embed=myembed)
        
    @slash_command(name='add-role')
    @permissions.has_any_role("EndorCoreMod", "Moderator", "Mod")
    async def role_add(self, ctx, member: discord.Member, role: discord.Role):
        
        if role > ctx.author.top_role:
            myembed = discord.Embed ()
            myembed.add_field(name="Role mentioned too high", value= "You can only add roles below your role", inline=False)
            await ctx.send(embed=myembed)         
            return 
        
        else:
            await member.add_roles(role)
            myembed = discord.Embed ()
            myembed.add_field(name="Role added", value= f'{member} now has {role} added', inline=False)
            await ctx.send(embed=myembed)

    @slash_command(name='remove-role')
    @permissions.has_any_role("EndorCoreMod", "Moderator", "Mod")
    async def role_remove(self, ctx, member: discord.Member, role: discord.Role):
        
        if role > ctx.author.top_role:
            myembed = discord.Embed ()
            myembed.add_field(name="Role mentioned too high", value= "You can only remove roles below your role", inline=False)
            await ctx.send(embed=myembed)         
            return
        
        else:
            await member.remove_roles(role)
            myembed = discord.Embed ()
            myembed.add_field(name="Role removed", value= f'{member} now has {role} removed', inline=False)
            await ctx.send(embed=myembed)
        
    @slash_command(name='unban')
    @permissions.has_any_role("EndorCoreMod", "Moderator", "Mod")
    async def unban(self, ctx, *, member):
        member_user = discord.Object(id=member)
        try:
            await ctx.guild.unban(member_user)
            await ctx.send(f"Unbanned {member_user}")
        except discord.NotFound:
            await ctx.send(f"{member} does not exist!")
            
    @slash_command(name='bans')
    @permissions.has_any_role("EndorCoreMod", "Moderator", "Mod")
    async def bans_guild(self, ctx):
        ban_list = []
        async for entry in ctx.guild.audit_logs(action=discord.AuditLogAction.ban):
            ban_list.append(f'{entry.user} banned {entry.target} at {entry.created_at} with reason {entry.reason}')
        await ctx.send("\n".join(ban_list))
        
    @slash_command(name='mute',)
    @permissions.has_any_role("EndorCoreMod", "Moderator", "Mod")
    async def mute(self, ctx, member: discord.Member):

        guild = ctx.guild 
        muted = discord.utils.get(ctx.guild.roles, name= "Muted")
        myembed = discord.Embed ()

        if not muted:
            perms =  discord.Permissions(speak=False, send_messages=False)
            muted = await guild.create_role(name= "Muted", permissions= perms)
            await muted.edit(position=1)

        
        myembed.add_field(name= "Muted", value= f'{member} has been muted', inline=False)

        await member.add_roles(muted)
        await ctx.send(embed=myembed)
        
        
    @slash_command(name='unmute')
    @permissions.has_any_role("EndorCoreMod", "Moderator", "Mod")
    async def unmute(self, ctx, member: discord.Member):
        
        muted = discord.utils.get(ctx.guild.roles, name= "Muted")

        
        myembed = discord.Embed ()
        myembed.add_field(name= "Unmuted", value= f'{member} has been unmuted', inline=False)

        await member.remove_roles(muted)
        await ctx.send(embed=myembed)
        
        
    @slash_command(name='purge')
    @permissions.has_any_role("EndorCoreMod", "Moderator", "Mod")
    async def purge(self, ctx, amount=1):
        await ctx.channel.purge(limit=amount + 1)

        myembed = discord.Embed ()
        myembed.add_field(name= "Purged", value= f'{amount} messages has been deleted', inline=False)

        await ctx.send(embed=myembed)
        
        
    @slash_command(name='strike')
    @permissions.has_any_role("EndorCoreMod", "Moderator", "Mod")
    async def strike(self, ctx, member : discord.Member):
        
        first_strike = 1
        
        
        cursor = await self.client.db.cursor()
        await cursor.execute(f"SELECT Strikes_Have FROM Strikes WHERE Guild_ID = {ctx.guild.id} AND User_ID = {member.id}")
        user_result = await cursor.fetchone()
        
        cursor = await self.client.db.cursor()
        await cursor.execute(f"SELECT MAX_STRIKES FROM Servers WHERE Guild_ID = {ctx.guild.id}")
        server_result = await cursor.fetchone()
        

        if user_result == None:
            
            cursor = await self.client.db.cursor()
                
            sql = f"INSERT INTO Strikes(Guild_ID, User_ID, Strikes_Have) VALUES({ctx.guild.id}, {member.id}, {first_strike})"
            
            await ctx.message.channel.send(f"Striked {member}")
            
            await cursor.execute(sql)
            await self.client.db.commit()
            await cursor.close()
            
            
        elif user_result["Strikes_Have"] == server_result["MAX_STRIKES"]:
                await ctx.message.channel.send(f"{member} has the max amount of stirkes specified by the server")

        else:
            
            cursor = await self.client.db.cursor()
                
            sql = f"UPDATE Strikes SET Strikes_Have = Strikes_Have + 1 where Guild_ID = {ctx.guild.id} AND User_ID = {member.id}"
            
            await ctx.message.channel.send(f"Striked {member}")
            
            await cursor.execute(sql)
            await self.client.db.commit()
            await cursor.close()
            
        
    @slash_command(name='pardon')
    @permissions.has_any_role("EndorCoreMod", "Moderator", "Mod")
    async def pardon(self, ctx, member : discord.Member, *, strikes : Optional[int]):
        
        if strikes == None:
            
            cursor = await self.client.db.cursor()
                
            sql = f"DELETE FROM Strikes WHERE Guild_ID = {ctx.guild.id} AND User_ID = {member.id}"
            await ctx.message.channel.send(f"Pardoned {member} of all strikes")
            
        else:
            
            cursor = await self.client.db.cursor()
                
            sql = f"UPDATE Strikes SET Strikes_Have = Strikes_Have - {strikes} where Guild_ID = {ctx.guild.id} AND User_ID = {member.id}"
            
            if strikes == 1:
                await ctx.message.channel.send(f"Pardoned {member} of {strikes} strike")
                
            else:
                await ctx.message.channel.send(f"Pardoned {member} of {strikes} strikes")
                
                
        await cursor.execute(sql)
        await self.client.db.commit()
        await cursor.close()
        
        
    @slash_command(name='infractions')
    @permissions.has_any_role("EndorCoreMod", "Moderator", "Mod")
    async def configset(self, ctx, member : discord.Member):
        
        cursor = await self.client.db.cursor()
        await cursor.execute(f"SELECT Strikes_Have FROM Strikes WHERE Guild_ID = {ctx.guild.id} AND User_ID = {member.id}")
        result = await cursor.fetchone()
        
        
        if result is None:
            myembed = discord.Embed ()
            myembed.add_field(name=f"No strikes for {member}", value= "Good Job", inline=False)
            await ctx.message.channel.send(embed=myembed)
            
        else:
            infractions = result["Strikes_Have"]
            myembed = discord.Embed ()
            myembed.add_field(name=f"Infractions for {member}", value= f"{infractions}", inline=False)
            
            
            await ctx.message.channel.send(embed=myembed)


def setup(client):
    client.add_cog(Mod(client))