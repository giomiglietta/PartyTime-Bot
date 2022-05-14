from discord.ext import commands
from discord import Guild, Member
import discord, time, os
from dotenv import load_dotenv

client = discord.Client()
bot = discord.ext.commands.Bot(command_prefix="$")
bot2 = discord.ext.commands.Bot(command_prefix="&")

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
DISCORD_TOKEN2 = os.getenv("DISCORD_TOKEN2")

# Finds Voice Channels
@bot.event
async def channels(ctx):
    voice_channel_list = ctx.guild.voice_channels
    return voice_channel_list


@bot.command(name="move", pass_context=True)
async def partyTime(ctx, member: discord.Member, seconds):
    list = await channels(ctx)
    t_end = time.time() + int(seconds)
    while time.time() < t_end:
        for x in list:
            time.sleep(2)
            await member.move_to(x)
            print("MOVED")


@bot2.event
async def channels(ctx):
    voice_channel_list = ctx.guild.voice_channels
    return voice_channel_list


@bot2.command(name="move", pass_context=True)
async def partyTime(ctx, member: discord.Member, seconds):
    list = await channels(ctx)
    t_end = time.time() + int(seconds)
    time.sleep(1)
    while time.time() < t_end:
        for x in list:
            time.sleep(2)
            await member.move_to(x)
            print("MOVED")


bot.run(DISCORD_TOKEN)
bot2.run(DISCORD_TOKEN2)
