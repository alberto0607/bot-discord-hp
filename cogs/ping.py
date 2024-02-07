import discord
from discord.ext import commands


class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Conectado como {self.bot.user}.")

    @commands.command(name="ping", description="Muestra la latencia del bot.")
    async def ping(self, ctx):
        latency = round(self.bot.latency * 1000)
        await ctx.send(f"**Pong 🏓!** Tengo una latencia de {latency}ms.")

    @commands.command(name="hello", description="Muestra un saludo.")
    async def hello(self, ctx, *, member: discord.Member = None):
        """Says hello"""
        member = member or ctx.author
        if self._last_member is None or self._last_member.id != member.id:
            await ctx.send(f'Hello @{member.name}')
        else:
            await ctx.send(f'Hello {member.name}... This feels familiar.')
        self._last_member = member

async def setup(bot):
    await bot.add_cog(Ping(bot))
