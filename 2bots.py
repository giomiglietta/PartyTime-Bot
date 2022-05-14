from discord.ext import commands
from discord import Guild, Member
import os, discord, time, asyncio
from dotenv import load_dotenv

load_dotenv()

bot = discord.ext.commands.Bot(command_prefix="&")
bot2 = discord.ext.commands.Bot(command_prefix="&")


DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
DISCORD_TOKEN2 = os.getenv("DISCORD_TOKEN2")

num_of_channels = 0
index = 0

# Finds Voice Channels
@bot.event
@bot2.event
async def channels(ctx):
    global num_of_channels
    voice_channel_list = ctx.guild.voice_channels
    num_of_channels = len(voice_channel_list)
    return voice_channel_list


@bot.command(name="move", pass_context=True)
async def partyTime(ctx, member: discord.Member, seconds):
    global index
    list = await channels(ctx)
    t_end = time.time() + int(seconds)
    while time.time() < t_end:
        await asyncio.sleep(1)
        try:
            await member.move_to(list[index])
        except IndexError:
            await member.move_to(list[0])
        if index == num_of_channels - 1:
            index = 0
        else:
            index += 1
        try:
            local = list[index]
        except IndexError:
            pass
        print("MOVED", local, index)


@bot2.command(name="move", pass_context=True)
async def partyTime(ctx, member: discord.Member, seconds):
    global index
    list = await channels(ctx)
    t_end = time.time() + int(seconds)
    await asyncio.sleep(1)
    while time.time() < t_end:
        await asyncio.sleep(1)
        try:
            await member.move_to(list[index])
        except IndexError:
            await member.move_to(list[index - 1])
        if index == num_of_channels - 1:
            index = 0
        else:
            index += 1
        try:
            local = list[index]
        except IndexError:
            pass
        print("MOVED 2", local, index)


loop = asyncio.get_event_loop()
loop.create_task(bot.start(DISCORD_TOKEN, bot=True))
loop.create_task(bot2.start(DISCORD_TOKEN2, bot=True))
loop.run_forever()
