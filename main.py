import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import config as cfg

intents = discord.Intents.default()
intents.guilds = True
intents.members = True
intents.voice_states = True  # Важливо для відстеження голосових каналів

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')


@bot.event
async def on_voice_state_update(member, before, after):
    if member.guild.id != cfg.GUILD_ID:
        return

    role = discord.utils.get(member.guild.roles, id=cfg.DEFAULTROLE_ID)
    if role not in member.roles:
        return

    # Отримуємо всі текстові та голосові чати серверу, крім cfg.RAIDCHAT_ID
    restricted_channels = [ch for ch in member.guild.text_channels + member.guild.voice_channels if
                           ch.id != cfg.RAIDCHAT_ID]

    for channel in restricted_channels:
        if after.channel:  # Користувач зайшов у голосовий канал
            await channel.set_permissions(member, send_messages=False)
        elif before.channel and not after.channel:  # Користувач вийшов
            await channel.set_permissions(member, overwrite=None)  # Скидаємо права


if __name__ == "__main__":
    load_dotenv()
    bot.run(os.getenv('TOKEN'))
