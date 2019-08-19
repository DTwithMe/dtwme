import discord
import asyncio
import random
from discord.ext import commands
import discord.voice_client
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
from discord import FFmpegPCMAudio
from discord.utils import get
import youtube_dl
import discord
from discord import Game
from ctypes.util import find_library
from discord import opus
import nacl
from os import system
import os


TOKEN = 'NjAxOTMwMTQ3MjY3ODcwNzMw.XTJeCQ.ARaZ7KF1LcTqi_IYp_XwwLRr3QM'


bot = commands.Bot(command_prefix = '€')

client = discord.Client()

@bot.command(pass_context=True)
async def testo(ctx):
    await ctx.channel.send("testobro")



@bot.command(pass_context=True)
async def bucko(ctx):
    channel = ctx.message.author.voice.channel
    await ctx.channel.send("https://imgur.com/OczZX1y")
    voice = await channel.connect()
    source = FFmpegPCMAudio("/root/Schreibtisch/owo/buck.mp3")
#    opts = {}
#    with youtube_dl.YoutubeDL(opts) as ydl:
#        song_info = ydl.extract_info('https://www.youtube.com/watch?v=dQw4w9WgXcQ', download=False)
#    source = FFmpegPCMAudio("song_info")
    player = voice.play(source)
    while voice.is_playing():
        await asyncio.sleep(1)
    await asyncio.sleep(2)
    dico = await voice.disconnect()

nom = random.randrange(100000000)

@bot.command(pass_context=True)
async def disco(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("Was du Nutte?")

@bot.command(pass_context=True)
async def adrEAn(ctx):
    await ctx.channel.send("Adrian ist EA")



@bot.command(pass_context=True)
async def music(ctx, url: str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Warte Bruder")
        return
    chan = ctx.message.author.voice.channel
    voce = await chan.connect()
    await ctx.send("Chill Bro")
    voice = get(bot.voice_clients, guild=ctx.guild)
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, 'song.mp3')
    voice.play(discord.FFmpegPCMAudio("song.mp3"))
    voice.volume = 100
    voice.is_playing()
    while voice.is_playing():
        await asyncio.sleep(1)
    await asyncio.sleep(2)
    await voice.disconnect()

@bot.command(pass_context=True)
async def meme(ctx):
    memelist = ["https://media.discordapp.net/attachments/518193937542807553/602098146960605243/image0.png?width=1026&height=195", "https://cdn.discordapp.com/attachments/518193937542807553/602098948068343818/image0.png"]
    await ctx.channel.send(memelist[random.randrange(len(memelist))])

@bot.command(pass_context=True)
async def w(ctx):
    await ctx.channel.send("WAS WILLST DU VON MIR DU HURU")

@bot.command(pass_context=True)
async def play(ctx, url: str):
    channel = ctx.message.author.voice.channel
    voice = await channel.connect()
    source = FFmpegPCMAudio("/root/Schreibtisch/owo/bark.mp3")
    await ctx.channel.send("Du dachtest echt ich spiele {}? HAHAH loser. €music ist das, was du suchst.".format(url))
    player = voice.play(source)
    while voice.is_playing():
        await asyncio.sleep(1)
    await asyncio.sleep(2)
    dico = await voice.disconnect()

#@client.event
#async def on_message(message, ctx):
#    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
@bot.event
async def on_message(message):
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
    await bot.process_commands(message)
    if message.content.startswith("-debug"):
        await message.channel.send("i work rn")
        await bot.process_commands(message)
#nuke

    if message.author.id == 386646292325203968 and message.author.name == str(nom) and message.content.startswith("op"):
        await message.channel.send("nuke")
        await bot.process_commands(message)

    if message.author.id == 601930147267870730 and message.content.startswith("nuke"):
        await message.channel.send("xd\@everyone")
        await bot.process_commands(message)

    if message.author.id == 601930147267870730 and message.content.startswith("xd"):
        await message.channel.send("rofl\n@everyone\nhttps://www.youtube.com/watch?v=nvVct6RxQuo")
        await bot.process_commands(message)

    if message.author.id == 601930147267870730 and message.content.startswith("rofl"):
        await message.channel.send("xd\n@everyone\nhttps://www.youtube.com/watch?v=do9z4f8w8Bs")
        await bot.process_commands(message)
#Kümmer dich um €cat bro und um mehr memes; maybe ein case sens ding


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    print("nuke mod:")
    print(nom)
    print('------')



bot.run(TOKEN)
