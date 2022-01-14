import discord
import traceback
import sys
from discord.ext import commands
from discord import File


class CommandErrorHandler(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if hasattr(ctx.command, 'on_error'):
            return

        cog = ctx.cog
        if cog:
            if cog._get_overridden_method(cog.cog_command_error) is not None:
                return

        ignored = (commands.CommandNotFound, )
        error = getattr(error, 'original', error)

        if isinstance(error, ignored):
            return

        if isinstance(error, commands.DisabledCommand):
            await ctx.send(f'{ctx.command} has been disabled.')

        elif isinstance(error, commands.NoPrivateMessage):
            try:
                await ctx.author.send(f'{ctx.command} can not be used in Private Messages.')
            except discord.HTTPException:
                pass

        elif isinstance(error, commands.BadArgument):
            if ctx.command.qualified_name == 'tag list':
                await ctx.send('I could not find that member. Please try again.')
                
            else:
                await ctx.send('Bad Argument')

        else:
            
            
            tb = traceback.format_exception(type(error), error, error.__traceback__)
            
            traceback_text = ''.join(tb)
            if len(traceback_text) > 2000:
                file = open("error.txt","w+")
                file.write(f"Ignoring exception in command {ctx.command}:\n{traceback_text}")
                file = open("error.txt","rb")
                await ctx.send(file=File(file))
            else:
                await ctx.send(f'```Ignoring exception in command {ctx.command}:```\n```{traceback_text}```')
            
            
            
def setup(client):
    client.add_cog(CommandErrorHandler(client))