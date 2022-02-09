import os
import discord
from discord.ext import commands
import keep_alive

token = os.environ['bot_token']
chid = int(os.environ['channel_id'])
intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.listen()
async def on_ready() :
	print("Bot ready for deployment")

@bot.listen()
async def on_message(message : discord.Message):
    if message.author==bot.user:
        return
    try : 
    	if message.channel.id==chid : 
            if message.author.dm_channel == None:
                await message.author.create_dm()
            await message.author.dm_channel.send(content='''Baited! Get Rekt! 
			Or contact HellFire#5410 if it was a genuine mistake and get unbanned 😅. 
			In the meantime, enjoy this video : https://www.youtube.com/watch?v=j5a0jTc9S10''')
            print("Banned : ", message.author.id)
            await message.author.ban(reason="Spam baited")
    except Exception as e:
        print(e)
		
keep_alive.keep_alive()

bot.run(token, reconnect = True)
