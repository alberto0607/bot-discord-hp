import discord
from discord.ext import commands
import requests
import json


class Witness(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def testigo(self, ctx, witness, userhive):
        try:
            endpoint = f"https://hive.blog/@{userhive}.json"
            response = requests.get(endpoint)
            data = json.loads(response.text)

            # Verificar si el usuario no fue encontrado
            if data.get("status") == "404":
                await ctx.send(f"El usuario '{userhive}' no existe en Hive.")
                return

            response.raise_for_status()  # Verificar si hubo un error en la solicitud HTTP

            user_data = data.get("user", {})
            proxy = user_data.get("proxy", "")
            witness_votes = user_data.get("witness_votes", [])

            status_text = ""
            vote_link = ""

            if proxy == "":
                if witness in witness_votes:
                    status_text = "Aprobado"
                else:
                    status_text = "No aprobado"
                    vote_link = f"[Votar por {witness}](https://vote.hive.uno/@{witness})"
            elif proxy == witness:
                status_text = "Aprobado (Sigue el proxy)"
            else:
                proxy_endpoint = f"https://hive.blog/@{proxy}.json"
                proxy_response = requests.get(proxy_endpoint)
                # Verificar si hubo un error en la solicitud HTTP
                proxy_response.raise_for_status()
                proxy_data = json.loads(proxy_response.text)
                proxy_witness_votes = proxy_data.get(
                    "user", {}).get("witness_votes", [])

                if witness in proxy_witness_votes:
                    status_text = f"Aprobado a través del proxy {proxy}"
                else:
                    status_text = f"No aprobado a través del proxy {proxy}"
                    vote_link = f"[Votar por {witness}](https://vote.hive.uno/@{witness})"

            embed = discord.Embed(
                title="Resultado de la verificación",
                color=discord.Color.green() if "Aprobado" in status_text else discord.Color.red()
            )
            embed.add_field(name="Estado", value=status_text + " - " +
                            userhive, inline=False)
            embed.set_footer(text="Desarrollado por alberto0607")
            if vote_link:
                embed.add_field(name="Votar", value=vote_link, inline=False)

            await ctx.send(embed=embed)

        except requests.exceptions.RequestException as e:
            await ctx.send("Ocurrió un error al hacer la solicitud HTTP.")
        except json.JSONDecodeError as e:
            await ctx.send("Ocurrió un error al procesar los datos JSON.")

async def setup(bot):
    await bot.add_cog(Witness(bot))
    