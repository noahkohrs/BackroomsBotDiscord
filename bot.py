import discord
from random import randint
import time
from discord.ext import commands
import asyncio
from discord import FFmpegPCMAudio
import os
from dotenv import load_dotenv


guild = None
intents = discord.Intents.all()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)



@bot.command(pass_context=True)
async def test(ctx):
    global guild
    guild = ctx.guild
    await send()


def get_floor_channel():
    global guild
    if guild == None:
        return
    channels = guild.channels
    BackroomChannel = None
    for BackroomChannel in channels:
        if ("floor 0" in BackroomChannel.name) or ("backrooms" in BackroomChannel.name) :
            break
    return BackroomChannel

def get_random_channel() :
    global guild
    if guild == None:
        return
    channels = guild.channels

    channels = [channel for channel in channels if (isinstance(channel, discord.VoiceChannel)) and (len(channel.members) > 0) and ("floor" not in channel.name)]
    
    if len(channels) == 0:
        return None

    channel = channels[randint(0, len(channels)-1)]
    return channel 

def get_random_user(channel):
    global guild
    users = channel.members
    user = None

    users = [user for user in users]
    if len(users) != 0:
        user = users[randint(0, len(users)-1)]
    return user

async def remove_all_roles(user): 
    for role in user.roles:
        if role.name != "@everyone":
            await asyncio.sleep(0.1)
            await user.remove_roles(role)

async def add_all_roles(user,roles):
    for role in roles:
        if role.name != "@everyone":
            await user.add_roles(role)

async def sound(sound_file,Channel) :
    if Channel.guild.voice_client == None:
        voice = await Channel.connect()
        voice.play(FFmpegPCMAudio(sound_file))


async def send_user(user, channel, BackroomChannel):
    #Saving user data
    roles = user.roles 
        
    #remove all roles and send user to backrooms:
    await remove_all_roles(user)

    #await asyncio.sleep(5)
    await user.move_to(BackroomChannel)  
    
    #connect bot to backrooms:
    await sound("backkrooms.mp3",BackroomChannel)
    
    #time to wait in backrooms:
    await asyncio.sleep(15)
        
    #regive roles and save user from hell: 
    if user.voice != None:  
        await user.move_to(channel) 
    await add_all_roles(user,roles)

    

async def send():
    global guild
    if guild == None:
        return

    BackroomChannel = get_floor_channel()

    channel = get_random_channel()
    if channel == None:
        return

    user = get_random_user(channel)
    if user == None:
        return

    await send_user(user, channel, BackroomChannel)


async def send_random():
    global max_wait_time, min_wait_time
    while True:

        #if no one is in a voice channel, wait 5 seconds and try again
        if guild == None:
            print("No one in a voice channel")
            await asyncio.sleep(20)
            continue
        
        # Call the send function
        #print(time.strftime("%H:%M:%S", time.localtime()))
        # Setup a waiting time.
        x = randint(min_wait_time*60, max_wait_time*60)
        print("MINUTES BEFORE MOVING : %d MINUTES." % (x//60))
        await asyncio.sleep(x)
        #print(time.strftime("%H:%M:%S", time.localtime()))

        await send()

        
@bot.event
async def on_ready():
    print('Bot connecté en tant que {0.user}'.format(bot))
    bot.loop.create_task(send_random())

@bot.event
async def on_voice_state_update(member, before, after):
    if after.channel == None:
        return
    global guild
    guild = after.channel.guild
    BackroomChannel = get_floor_channel()
    if len(BackroomChannel.members) <= 1:
        if BackroomChannel.guild.voice_client != None:
            await BackroomChannel.guild.voice_client.disconnect()
    
if os.path.exists(".env"):
    load_dotenv()
    max_wait_time = eval(os.getenv("MAX_WAIT_TIME"))
    min_wait_time = eval(os.getenv("MIN_WAIT_TIME"))
    if min_wait_time == None:
        min_wait_time = 30
    if max_wait_time == None:
        max_wait_time = 180
else :
    exit("No .env file found, please refer to the README.md file.")
print("| MIN = %d MINUTES, MAX = %d MINUTES |" % (min_wait_time, max_wait_time))
bot.run(os.getenv("DISCORD_TOKEN"))