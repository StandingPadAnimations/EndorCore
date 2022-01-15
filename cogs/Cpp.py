from discord import File
from discord.ext import commands
from discord.commands import slash_command
import build.Compiled.Test_py as Test_py
import concurrent.futures


class Cpp(commands.Cog):
    def __init__(self, client):
        self.client = client 
        
    def write_to_file(self, write):
        with open("primes.txt","w+") as file:
            file.write(f"{write}")
        return file 
    
    async def cog_check(self, ctx):
        cursor = await self.client.db.cursor()
        await cursor.execute("SELECT REASON FROM Blacklist WHERE User_ID = ?", (ctx.author.id,))
        result = await cursor.fetchone()
        if result is None:
            return ctx.author.id

    @slash_command(name='prime-list')
    async def prime_list(self, ctx, number : int):
        if number > 100000:
            await ctx.respond("That's way too high")

        else:
            with concurrent.futures.ProcessPoolExecutor() as pool:
                prime_list = await self.client.loop.run_in_executor(pool, Test_py.prime_finder_cython, number)
                
            if sum(len(str(prime)) for prime in prime_list) < 2000:
                await ctx.respond(f"According to this Cython file, {number} primes between 0 and 100000 is {prime_list}")

            else:
                await ctx.respond(file=File(await self.client.loop.run_in_executor(None, self.write_to_file, f"According to this Cython file, \n{number} primes between 0 and 100000 is {prime_list}")))
                
    @slash_command(name='pytha')
    async def pytha(self, ctx, number : int):
        with concurrent.futures.ProcessPoolExecutor() as pool:
            pythag = await self.client.loop.run_in_executor(pool, Test_py.count_triples, number)
            
            await ctx.respond(f"According to this Cython file, the pythagorym theroum thing idk I'm not a expert is {pythag}")
            
    @slash_command(name='primes')
    async def primes(self, ctx, number : int, *, number2 : int):
        with concurrent.futures.ProcessPoolExecutor() as pool:
            primes = await self.client.loop.run_in_executor(pool, Test_py.amount_of_primes, number, number2)
            
        await ctx.respond(f"According to this Cython file, there are {primes} prime numbers between {number} and {number2}")
        
def setup(client):
    client.add_cog(Cpp(client))