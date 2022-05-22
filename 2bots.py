from discord.ext import commands
from discord.ext.commands import CommandInvokeError
from discord import Guild, Member
import os, discord, time, asyncio
from dotenv import load_dotenv
from discord.errors import HTTPException

load_dotenv()

bot = discord.ext.commands.Bot(command_prefix="&")
bot2 = discord.ext.commands.Bot(command_prefix="&")


DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
DISCORD_TOKEN2 = os.getenv("DISCORD_TOKEN2")

index = 0

# Finds Voice Channels
@bot.event
@bot2.event
async def channels(ctx):
    global num_of_channels
    voice_channel_list = ctx.guild.voice_channels
    num_of_channels = len(voice_channel_list)
    return voice_channel_list, num_of_channels


@bot.command(name="move", pass_context=True)
async def partyTime(ctx, member: discord.Member, seconds):
    global index
    index = 0
    list, num_of_channels = await channels(ctx)
    t_end = time.time() + int(seconds)
    while time.time() < t_end:
        await asyncio.sleep(1)
        try:
            await member.move_to(list[index])
            local = list[index]
        except IndexError:
            list = await channels(ctx)
            await member.move_to(list[0])
        except HTTPException:
            while True:
                try:
                    await member.move_to(list[index])
                    break
                except HTTPException:
                    await asyncio.sleep(1)
                    t_end += 1
        print("MOVED", local, index)
        if index == num_of_channels - 1:
            index = 0
        else:
            index += 1


@bot2.command(name="move", pass_context=True)
async def partyTime(ctx, member: discord.Member, seconds):
    global index, num_of_channels
    index = 0
    list, num_of_channels = await channels(ctx)
    t_end = time.time() + int(seconds)
    await asyncio.sleep(1)
    while time.time() < t_end:
        await asyncio.sleep(1)
        try:
            await member.move_to(list[index])
            local = list[index]
        except IndexError:
            list, num_of_channels = await channels(ctx)
            await member.move_to(list[index - 1])
        except HTTPException:
            while True:
                try:
                    await member.move_to(list[index])
                    break
                except HTTPException:
                    await asyncio.sleep(1)
                    t_end += 1
        print("MOVED 2", local, index)
        if index == num_of_channels - 1:
            index = 0
        else:
            index += 1


loop = asyncio.get_event_loop()
loop.create_task(bot.start(DISCORD_TOKEN, bot=True))
loop.create_task(bot2.start(DISCORD_TOKEN2, bot=True))
loop.run_forever()
