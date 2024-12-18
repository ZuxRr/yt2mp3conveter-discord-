import discord
from discord.ext import commands
import os
import yt_dlp
from dotenv import load_dotenv

load_dotenv()
TOKEN = "PUT UR BOT DISCORD TOKEN HERE"

INTENTS = discord.Intents.default()
INTENTS.message_content = True
bot = commands.Bot(command_prefix="!", intents=INTENTS)

if not os.path.exists("downloads"):
    os.makedirs("downloads")

@bot.event
async def on_ready():
    print(f"BOT {bot.user} BY LERMIR IS READY TO USE!")

@bot.command(name="mp3")
async def ytmp3(ctx, url: str):
    await ctx.reply("Bentar Wak, Lagi Proses :v ...")

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': True,  
    }

    try:

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            file_name = ydl.prepare_filename(info).replace(info['ext'], 'mp3')

        user = ctx.author
        await user.send( file=discord.File(file_name))
        await ctx.reply("Berhasil Wakk, mantap 😁😁.")
        await user.send("This Script By Lermir.")

        os.remove(file_name)

    except Exception as e:
        await ctx.reply(f"Terjadi kesalahan: {e}")

bot.run(TOKEN)
