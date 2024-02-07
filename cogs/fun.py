import discord
from discord.ext import commands
import random


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="gtn", description="Juego Adivina el Número")
    async def gtn(self, ctx):
        # Code for Guess The Number game logic
        num = random.randint(1, 100)
        # Send intro message
        await ctx.send("Estoy pensando en un número entre 1 y 100. ¡Intenta adivinarlo!")
        # Keep track of number of guesses
        guess_count = 0
        # Accept guesses and give feedback
        while True:
            guess = await self.bot.wait_for('message')
            guess = int(guess.content)
            guess_count += 1
            if guess < num:
                await ctx.send("¡Demasiado bajo!")
            elif guess > num:
                await ctx.send("¡Demasiado alto!")
            else:
                await ctx.send(f"¡Lo lograste en {guess_count} intentos!")
                break

    @commands.command(name="roll", description="Lanza un dado")
    async def roll(self, ctx):
        # Code for dice rolling logic
        sides = 6
        roll = random.randint(1, sides)
        await ctx.send(f"Has lanzado un {roll} en un dado de {sides} caras.")

    @commands.command(name="flip", description="Voltea una moneda")
    async def flip(self, ctx):
        # Code for coin flipping logic
        choices = ["Cara", "Cruz"]
        flip = random.choice(choices)
        await ctx.send(f"Has volteado una moneda y obtuviste {flip}.")

    @commands.command(name="compliment", description="Da un cumplido al azar")
    async def compliment(self, ctx):
        # Code for random compliment logic
        compliments = ["¡Lo estás haciendo genial!", "Te ves maravilloso hoy.",
                       "Esa fue una idea realmente inteligente.", "Te aprecio.", "Tienes un corazón tan amable."]
        recipient = ctx.author.mention
        compliment = random.choice(compliments)

        await ctx.send(f"{recipient} {compliment}")

    @commands.command(name="fortune", description="Obtén una predicción")
    async def fortune(self, ctx):
        # Code for fortune telling logic
        fortunes = ["Un amigo fiel es una fuerte defensa.",
                    "Un mar tranquilo nunca hizo a un marinero hábil.",
                    "La aventura puede ser una verdadera felicidad.",
                    "Todo estará bien, aunque las cosas parezcan oscuras en este momento."]

        fortune = random.choice(fortunes)

        await ctx.send(fortune)

    @commands.command(name="quote", description="Obtén una cita inspiradora")
    async def quote(self, ctx):
        # Code for random inspirational quote
        quotes = ["Mantente hambriento. Mantente insensato.",
                  "Tu tiempo es limitado, así que no lo gastes viviendo la vida de otra persona.",
                  "Un buen juicio proviene de la experiencia, y la experiencia proviene de malos juicios.",
                  "El mejor momento para plantar un árbol fue hace 20 años. El segundo mejor momento es ahora."]

        quote = random.choice(quotes)

        await ctx.send(quote)


async def setup(bot):
    await bot.add_cog(Fun(bot))
