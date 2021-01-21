import discord
import youtube_dl
import asyncio
import logging
from discord.ext import commands, tasks
import os
import random
import youtube_dl
import quiz

####################################################################################################################################

TOKEN = 'NzQ2NDM4ODA1NzQ1MTcyNTAy.X0AVTw.rnSojyBh1puPWy0X1hafb8Njp6I'
client = commands.Bot(command_prefix ='.')
#quiz = quiz.Quiz(client)
player = {}
id = 616984424344584201

###################################################################################################################################
#ON READY

@client.event
async def on_ready(*args):
    await client.change_presence(activity=discord.Game('!quiz'))
    print('###################')
    print('logged in as')
    print(client.user.name)
    print(client.user.id )

    channel = client.get_channel(800154656264683550)
    retStr = str("""```!help```""")
    retStr2 = str("""```!member```""")
    retStr3 = str("""```!quiz```""")
    retStr4 = str("""```!games```""")
    embed = discord.Embed(title="**𝕔𝕠𝕞𝕞𝕒𝕟𝕕𝕤**",color=0xcab8ff, description="\u200b")
    embed.set_author(name="saturn team", icon_url="https://i.imgur.com/o8JiG7R.png")
    embed.set_footer(text="thanks for reading", icon_url="https://i.imgur.com/o8JiG7R.png")
    embed.add_field(name=retStr,value="to see all \n commands \n ---------------------------", inline=False)
    embed.add_field(name=retStr2, value="to see how many\n members our server has \n ---------------------------", inline=False)
    embed.add_field(name=retStr4, value="to see all our games\n ---------------------------", inline=False)
    embed.add_field(name=retStr3, value="to play our quiz\n ---------------------------", inline=False)
    embed.add_field(name="\u200b", value="\u200b", inline=False)
    await channel.send(content=None, embed=embed)

#################################################################################################################################
#COMMANDS

@client.event
async def on_message(message):
        id = client.get_guild(616984424344584201)
        if message.content.startswith('!help'):

            retStr = str("""```!help```""")
            retStr2 = str("""```!member```""")
            retStr3 = str("""```!quiz```""")
            retStr4 = str("""```!games```""")
            embed = discord.Embed(title="**𝕔𝕠𝕞𝕞𝕒𝕟𝕕𝕤**",color=0xcab8ff, description="\u200b")
            embed.set_author(name="saturn team", icon_url="https://i.imgur.com/o8JiG7R.png")
            embed.set_footer(text="thanks for reading", icon_url="https://i.imgur.com/o8JiG7R.png")
            embed.add_field(name=retStr,value="to see all \n commands \n ---------------------------", inline=False)
            embed.add_field(name=retStr2, value="to see how many\n members our server has \n ---------------------------", inline=False)
            embed.add_field(name=retStr4, value="to see all our games\n ---------------------------", inline=False)
            embed.add_field(name=retStr3, value="to play our quiz\n ---------------------------", inline=False)
            
            embed.add_field(name="\u200b", value="\u200b", inline=False)
            await message.channel.send(content=None, embed=embed)
        
        elif message.content.startswith('!member'):
            await message.channel.send(f"""This Discor Server has {id.member_count} Member.""")

        elif message.content.startswith('!games'):

            retStr5 = str("""```!quiz```""")
            embed = discord.Embed(title="**𝕘𝕒𝕞𝕖𝕤**",color=0xcab8ff, description="\u200b")
            embed.set_author(name="saturn team", icon_url="https://i.imgur.com/o8JiG7R.png")
            embed.set_footer(text="more comming soon!", icon_url="https://i.imgur.com/o8JiG7R.png")
            embed.add_field(name=retStr5,value="play our quiz", inline=False)
            embed.add_field(name="\u200b", value="\u200b", inline=False)
            await message.channel.send(content=None, embed=embed)
        
        elif quiz is not None and quiz.started():
            print('Quiz started')
            await quiz.answer_question(message)

        elif message.content.startswith('!stop'):
            print('!stop')
            await message.channel.send('Leaving server. BYE!', tts=True)
            await quiz.stop()
        elif (message.content.startswith('!reset')):
            print('!reset')
            await quiz.reset()        
        elif message.content.startswith('!quiz'):
            print('!quiz')
            await quiz.start(message.channel)      
        elif message.content.startswith('!score'):
            print('!score')
            await quiz.print_scores()    
        elif (message.content.startswith('!next')):
            print('!next')
            await quiz.next_question(message.channel)
        elif quiz is not None and quiz.started():
            await quiz.answer_question(message)


####################################################################################################################################

#MUSICBOT#
#@client.event
#async def on_message(message):
#   if message.content.startswith('!join'):
#        channel = message.author.voice.channel
#        await channel.conect()
#
#   elif message.content.startswith('!leave'):
#        await message.voice_client.disconnect()
#
#@client.event
#async def play(message, url):
#    server = message.server
#    voice_client = client.voice_client_in(server)
#    player = await voice_client.creat.ytdl_player(url)
#    player[server.id] = player
#    player.start()

####################################################################################################################################

client.run(TOKEN)