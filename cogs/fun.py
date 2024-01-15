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
                await ctx.respond("¡Demasiado bajo!")
            elif guess > num:
                await ctx.respond("¡Demasiado alto!")
            else:
                await ctx.respond(f"¡Lo lograste en {guess_count} intentos!")
                break

    @commands.command(name="roll", description="Lanza un dado")
    async def roll(self, ctx):
        # Code for dice rolling logic
        sides = 6
        roll = random.randint(1, sides)
        await ctx.respond(f"Has lanzado un {roll} en un dado de {sides} caras.")

    @commands.command(name="flip", description="Voltea una moneda")
    async def flip(self, ctx):
        # Code for coin flipping logic
        choices = ["Cara", "Cruz"]
        flip = random.choice(choices)
        await ctx.respond(f"Has volteado una moneda y obtuviste {flip}.")

    @commands.command(name="rps", description="Juega piedra, papel o tijera")
    async def rps(self, ctx):
        # Code for rock paper scissors logic
        choices = ["Piedra", "Papel", "Tijeras"]
        player_choice = await self.bot.wait_for('message')
        bot_choice = random.choice(choices)
        player_choice = player_choice.content.title()

        if player_choice == bot_choice:
            result = "¡Es un empate!"
        elif player_choice == "Piedra":
            if bot_choice == "Papel":
                result = "¡Has perdido! El papel vence a la piedra."
            else:
                result = "¡Has ganado! La piedra vence a las tijeras."
        elif player_choice == "Papel":
            if bot_choice == "Tijeras":
                result = "¡Has perdido! Las tijeras vencen al papel."
            else:
                result = "¡Has ganado! El papel vence a la piedra."
        elif player_choice == "Tijeras":
            if bot_choice == "Piedra":
                result = "¡Has perdido! La piedra vence a las tijeras."
            else:
                result = "¡Has ganado! Las tijeras vencen al papel."

        await ctx.respond(f"Elegiste {player_choice} y yo elegí {bot_choice}. {result}")

    @commands.command(name="8ball", description="Hazle una pregunta a la bola mágica 8")
    async def eight_ball(self, ctx):
        # Code for magic 8 ball logic
        responses = ["Es seguro", "Sin duda", "Definitivamente", "Sí, definitivamente",
                    "Puedes confiar en ello", "Según mi punto de vista, sí", "Probablemente", "Perspectivas favorables",
                    "Sí", "Las señales apuntan a que sí", "Respuesta poco clara, intenta de nuevo", "Pregunta de nuevo más tarde",
                    "Mejor no decirte ahora", "No puedo predecirlo ahora", "Concéntrate y pregunta de nuevo",
                    "No cuentes con eso", "Mi respuesta es no", "Mis fuentes dicen que no", "Perspectivas no tan buenas",
                    "Muy dudoso"]

        question = await self.bot.wait_for('message')
        answer = random.choice(responses)

        await ctx.respond(f"Pregunta: {question.content}\nRespuesta: {answer}")

    @commands.command(name="compliment", description="Da un cumplido al azar")
    async def compliment(self, ctx):
        # Code for random compliment logic
        compliments = ["¡Lo estás haciendo genial!", "Te ves maravilloso hoy.", "Esa fue una idea realmente inteligente.", "Te aprecio.", "Tienes un corazón tan amable."]
        recipient = ctx.author.mention
        compliment = random.choice(compliments)

        await ctx.respond(f"{recipient} {compliment}")

    @commands.command(name="wouldyourather", description="Haz la pregunta ¿Preferirías?")
    async def wouldyourather(self, ctx):
        # Code for would you rather logic
        questions = [["¿Tener fuerza sobrehumana o inteligencia sobrehumana?", "fuerza", "inteligencia"],
                    ["¿Vivir en el pasado o en el futuro?", "pasado", "futuro"],
                    ["¿Tener el poder de la invisibilidad o la capacidad de volar?", "invisibilidad", "volar"]]

        question = random.choice(questions)
        option1 = question[1]
        option2 = question[2]

        response = await self.bot.wait_for('message')
        player_choice = response.content

        if player_choice == option1:
            result = f"Elegiste {option1}."
        elif player_choice == option2:
            result = f"Elegiste {option2}."
        else:
            result = "Elección no válida, por favor elige la primera o segunda opción."

        await ctx.respond(f"¿Preferirías: {question[0]}\nTu elección: {result}")

    @commands.command(name="fortune", description="Obtén una predicción")
    async def fortune(self, ctx):
        # Code for fortune telling logic
        fortunes = ["Un amigo fiel es una fuerte defensa.",
                    "Un mar tranquilo nunca hizo a un marinero hábil.",
                    "La aventura puede ser una verdadera felicidad.",
                    "Todo estará bien, aunque las cosas parezcan oscuras en este momento."]

        fortune = random.choice(fortunes)

        await ctx.respond(fortune)

    @commands.command(name="quote", description="Obtén una cita inspiradora")
    async def quote(self, ctx):
        # Code for random inspirational quote
        quotes = ["Mantente hambriento. Mantente insensato.",
                  "Tu tiempo es limitado, así que no lo gastes viviendo la vida de otra persona.",
                  "Un buen juicio proviene de la experiencia, y la experiencia proviene de malos juicios.",
                  "El mejor momento para plantar un árbol fue hace 20 años. El segundo mejor momento es ahora."]

        quote = random.choice(quotes)

        await ctx.respond(quote)

def setup(bot):
    bot.add_cog(Fun(bot))
