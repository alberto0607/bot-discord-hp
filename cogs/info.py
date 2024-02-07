import discord
from discord.ext import commands


class BotInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def info(self, ctx):
        owner = self.bot.get_user(729176123438792718)
        if not owner:
            owner_mention = "Owner not found"
        else:
            owner_mention = owner.mention

        embed = discord.Embed(
            title="Información del Bot",
            description="Herramienta multifuncional para Hive y más",
            color=discord.Color.blue()
        )
        embed.add_field(
            name="Comandos", value=("**$testigo** [testigo] [usuariohive] - Verifica el estado del usuario con respecto al testigo.\n"
                                    "**$ping** - Envia una respuesta de conexión\n"
                                    "**$info** - Devuelve información dellatada sobre el bot\n"
                                    "**Juegos**:\n"
                                    "**$gtn** - Juego Adivina el Número\n"
                                    "**$roll** - Lanza el dado\n"
                                    "**$flip** - Cara o Cruz\n"
                                    ), inline=False)
        embed.add_field(name="Desarrollador",
                        value=owner_mention, inline=False)
        embed.set_footer(
            text="Para más información, contacta al desarrollador.")

        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(BotInfo(bot))
