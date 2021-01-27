#imports
import discord
from discord.ext import commands
import aiohttp
import asyncio
import logging
import time
from discord import ext
from discord.ext import tasks
from dotenv import load_dotenv
import os
import random

#lists
client = discord.Client()

response_list = ["definitely!", "As I see it, yes!", "Yes!", "No!", "Very likely!", "Not even close!", "Maybe!", "Very unlikely!", "Ask again later!", "Better not tell you now!", " It is certain!", "My sources say no!", "Outlook good!", "Very Doubtful!", "Without a doubt!"]

anime_list = ["https://media1.tenor.com/images/c925511d32350cc04411756d623ebad6/tenor.gif?itemid=13462237", "https://media1.tenor.com/images/89289af19b7dab4e21f28f03ec0faaff/tenor.gif?itemid=12801687", "https://media1.tenor.com/images/e1f44b9d914ba61cc60efd8d3cf439a5/tenor.gif?itemid=9975267", "https://media.tenor.com/images/1d37a873edfeb81a1f5403f4a3bfa185/tenor.gif", "https://media.tenor.com/images/8f711b12e00bc1816694bf51909f8b8f/tenor.gif", "https://media.tenor.com/images/84e609c97fc79323c572baa4e8486473/tenor.gif", "https://media.tenor.com/images/c67648bdadbece24eed182a401abf576/tenor.gif", "https://media.tenor.com/images/46a74ce6228e7bc535263e1464cce46b/tenor.gif", "https://media.tenor.com/images/a173f1c95d81855afd10d51f3fa277ab/tenor.gif", "https://media.tenor.com/images/e1c9ad053d4aa0471727fbf36c3a3868/tenor.gif", "https://media.tenor.com/images/3f6457f7235edf481d542b8074740401/tenor.gif"]

zerotwo_list = ['https://media.tenor.com/images/4632e943653b0ad278a1fa7b8f49d82c/tenor.gif', 'https://media.tenor.com/images/3e7d551f4edbc139f1372a494eccd01d/tenor.gif', 'https://media.tenor.com/images/e046bd4175889014749d008bef023f25/tenor.gif', 'https://media.tenor.com/images/500953247d7ddda4d87908fa0bb2c7bc/tenor.gif', 'https://media.tenor.com/images/2e094b3c1f5bf047698dea434416d080/tenor.gif', 'https://media.tenor.com/images/09df52e29a5506287cd76fb4abafa2cc/tenor.gif', 'https://media.tenor.com/images/4f5f2d78f721fc36e10f4e5e2c340f47/tenor.gif', 'https://media.tenor.com/images/7691590d6ac021b483c39dfa794e2a1c/tenor.gif', 'https://64.media.tumblr.com/d03212d8697607c82bb85db886ee92af/tumblr_p2z0hgMv3g1wd81ruo1_540.gifv']

ichigo_list = ['https://media.tenor.com/images/d1fc46f2d0fd52740711b80b80a3c081/tenor.gif', 'https://media.tenor.com/images/b7687ce05975ad1d5c7ed52717e62f09/tenor.gif', 'https://data.whicdn.com/images/325037756/original.gif']

todoroki_list = ['https://pa1.narvii.com/6894/c584fe56b8dde82ac901aeb8e359cb2e157c3bdfr1-533-300_hq.gif', 'https://media1.tenor.com/images/30638e057d7c84c963619c3f9ab2a3df/tenor.gif?itemid=18024441', 'https://img.wattpad.com/e366789b1d68a2190987c27b2378395b6c0c7d66/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f776174747061642d6d656469612d736572766963652f53746f7279496d6167652f3152537645325f4f32366f6155673d3d2d3736373439353134382e313562376137353763303434343138363934363130373235393332302e676966?s=fit&w=720&h=720', 'https://i.pinimg.com/originals/2e/31/93/2e31935a326bdff0e6d1b91ae03d607f.gif', 'https://p.favim.com/orig/2018/08/01/boku-no-hero-academia-my-hero-academia-todoroki-shouto-Favim.com-6107451.gif']

nickwilde_list = ['https://fsa.zobj.net/crop.php?r=o-a4ILNuzRn8YwRkD-QM0H7an2GTrabiOjyMpROxtpiArleiFVaF6Fpmob4McDSJ93q3TqqQ00x3OoXqbLBl8bvMDwrnfI1wp7C_KNhsJGGAN-oQ3ZfRsouuic-dUowmbZU5cwncc1AETh4L', 'https://static.wikia.nocookie.net/zootropolis/images/6/6e/Nick_Wilde.png/revision/latest/scale-to-width-down/340?cb=20160326155400','https://pm1.narvii.com/6359/f79784f115daa6a84fda688b535c8330e0afd678_00.jpg', 'https://www.seekpng.com/png/detail/158-1582917_report-abuse-nick-wilde.png', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ80pNZPfmU6xPQIQnrRDfOYKLD-Xd0LykY4g&usqp=CAU']

headout_list = ['cya', 'peace out', 'stay safe', 'ttyl', 'have fun']

#client
@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))


@client.event

async def on_message(message):
    if message.author == client.user:
        return

#commands

#hello
    if message.content.startswith('%hello'):
        embed=discord.Embed(title="Hello!", color=0xff9efc)
        embed.set_footer(text="NULL.™")
        embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-mePBN4Q8D4Cb9WZE-w1370.gif')
        await message.channel.send(embed=embed)

#add bot
    if message.content.startswith('%addbot'):
        embed=discord.Embed(title="Add me to your server by clicking this link", color=0xff9efc)
        embed.add_field(name="https://bit.ly/null-bot-add", value="‎‎‎‎‎‎‎ ", inline=False)
        embed.set_footer(text="NULL.™")
        embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-mePBN4Q8D4Cb9WZE-w1370.gif')
        await message.channel.send(embed=embed)


#botver
    if message.content.startswith('%botver'):
        embed=discord.Embed(title="I am currently on Development version 0.22!", color=0xff9efc)
        embed.set_footer(text="NULL.™")
        embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-mePBN4Q8D4Cb9WZE-w1370.gif')
        await message.channel.send(embed=embed)


#icy
    if message.content.startswith('%is Icy the best and cutest in the world?'):
        embed=discord.Embed(title="I HOPE SO!", color=0xff9efc)
        embed.set_footer(text="NULL.™")
        embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-mePBN4Q8D4Cb9WZE-w1370.gif')
        await message.channel.send(embed=embed)

#icy
    if message.content.startswith("%will Icy be Muphs' boo?"):
        embed=discord.Embed(title="OF COURSE SHE IS!", color=0xff9efc)
        embed.set_footer(text="NULL.™")
        embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-mePBN4Q8D4Cb9WZE-w1370.gif')
        await message.channel.send(embed=embed)


#icy
    if message.content.startswith("%should i rethink my life?"):
        embed=discord.Embed(title="Yes!", color=0xff9efc)
        embed.set_footer(text="NULL.™")
        embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-mePBN4Q8D4Cb9WZE-w1370.gif')
        await message.channel.send(embed=embed)

#icy
    if message.content.startswith("%should Muphs be Icy's boyfriend?"):
        embed=discord.Embed(title="YES!", color=0xff9efc)
        embed.set_footer(text="NULL.™")
        embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-mePBN4Q8D4Cb9WZE-w1370.gif')
        await message.channel.send(embed=embed)

#laura
    if message.content.startswith("%islaurasupercool?"):
        embed=discord.Embed(title="idk, ask QNTM", color=0xff9efc)
        embed.set_footer(text="NULL.™")
        embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-mePBN4Q8D4Cb9WZE-w1370.gif')
        await message.channel.send(embed=embed)

#you
    if message.content.startswith("%amisupercool?"):
        embed=discord.Embed(title="YES!!!!!!", color=0xff9efc)
        embed.set_footer(text="NULL.™")
        embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-mePBN4Q8D4Cb9WZE-w1370.gif')
        await message.channel.send(embed=embed)

#cap
    if message.content.startswith("%was that cap?"):
        embed=discord.Embed(title="prolly, idk", color=0xff9efc)
        embed.set_footer(text="NULL.™")
        embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-mePBN4Q8D4Cb9WZE-w1370.gif')
        await message.channel.send(embed=embed)

#paulo
    if message.content.startswith("%ispaulosuperseggsyandsupercool?"):
        embed=discord.Embed(title="nah fam, straight up cap", color=0xff9efc)
        embed.set_footer(text="NULL.™")
        embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-mePBN4Q8D4Cb9WZE-w1370.gif')
        await message.channel.send(embed=embed)

#8ball
    if message.content.startswith("%8ball"):
        lucky_num = random.randint(0,len(response_list) - 1)
        embed=discord.Embed(title=(response_list[lucky_num]), color=0xff9efc)
        embed.set_footer(text="NULL.™")
        embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-mePBN4Q8D4Cb9WZE-w1370.gif')
        await message.channel.send(embed=embed)

#cuteanime
    if message.content.startswith("%cuteanime"):
        lucky_num = random.randint(0,len(anime_list) - 1)
        embed=discord.Embed(title='Awww', color=0xff9efc)
        embed.set_image(url=(anime_list[lucky_num]))
        embed.set_footer(text="NULL.™")
        embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-AMqGqMLEBnFQkD3l-w1370.gif')
        await message.channel.send(embed=embed)

#todoroki
    if message.content.startswith("%todoroki"):
        lucky_num = random.randint(0,len(todoroki_list) - 1)
        embed=discord.Embed(title=' ', color=0xff9efc)
        embed.set_image(url=(todoroki_list[lucky_num]))
        embed.set_footer(text="NULL.™")
        embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-AMqGqMLEBnFQkD3l-w1370.gif')

#zero two
    if message.content.startswith("%zerotwo"):
        lucky_num = random.randint(0,len(zerotwo_list) - 1)
        embed=discord.Embed(title='Awww', color=0xff9efc)
        embed.set_image(url=(zerotwo_list[lucky_num]))
        embed.set_footer(text="NULL.™")
        embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-AMqGqMLEBnFQkD3l-w1370.gif')
        await message.channel.send(embed=embed)

#ichigo
    if message.content.startswith("%ichigo"):
        lucky_num = random.randint(0,len(ichigo_list) - 1)
        embed=discord.Embed(title='Awww', color=0xff9efc)
        embed.set_image(url=(ichigo_list[lucky_num]))
        embed.set_footer(text="NULL.™")
        embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-AMqGqMLEBnFQkD3l-w1370.gif')
        await message.channel.send(embed=embed)

#nick
    if message.content.startswith("%nickwilde"):
        lucky_num = random.randint(0,len(nickwilde_list) - 1)
        embed=discord.Embed(title='Awww', color=0xff9efc)
        embed.set_image(url=(nickwilde_list[lucky_num]))
        embed.set_footer(text="NULL.™")
        embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-AMqGqMLEBnFQkD3l-w1370.gif')
        await message.channel.send(embed=embed)

#head out
    if message.content.startswith("%headout"):
        lucky_num = random.randint(0,len(headout_list) - 1)
        embed=discord.Embed(title=(headout_list[lucky_num]), color=0xff9efc)
        embed.set_image(url='https://media1.tenor.com/images/c57c8725cfdb74251c392e0ca46753ba/tenor.gif?itemid=15194343')
        embed.set_footer(text="NULL.™")
        embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-AMqGqMLEBnFQkD3l-w1370.gif')
        await message.channel.send(embed=embed)

#repeat
    #if message.content.startswith("%repeat"):
        #lucky_num = random.randint(0,len(response_list) - 1)
        #embed=discord.Embed("{}".format(" ".join(args))), color=0xff9efc
        #embed.set_footer(text="NULL.™")
        #embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-mePBN4Q8D4Cb9WZE-w1370.gif')
        #await message.channel.send(embed=embed)


    #await channel.send("{}".format(" ".join(args)))


#help
    if message.content.startswith('%help'):
        embed=discord.Embed(title="NULL.™ Help", color=0xff9efc)
        #hello
        embed.add_field(name="%hello", value="You're greeted by me!", inline=False)
        #add bot
        embed.add_field(name="%addbot", value="Add me to your server!", inline=False)
        #bot version
        embed.add_field(name="%botver", value="Get to know my current software version!", inline=False)
        #8ball
        embed.add_field(name="%8ball(your question)", value="Magic 8ball :O", inline=False)
        #pick
        embed.add_field(name="%pick", value="I pick from a list (separated by commas and spaces)", inline=False)
        #ping
        embed.add_field(name="%ping", value="Lists current ping in miliseconds!", inline=False)
        #repeat
        embed.add_field(name="%repeat", value="I repeat after you!", inline=False)
        #cute anime
        embed.add_field(name="%cuteanime", value="Cute anime gifs", inline=False)
        #todoroki
        embed.add_field(name="%todoroki", value="for the simps ;)", inline=False)
        #zero two
        embed.add_field(name="%zerotwo", value="for the simps ;)", inline=False)
        #ichigo
        embed.add_field(name="%ichigo", value="for the simps ;)", inline=False)
        #easter eggs
        embed.add_field(name="easter eggs :smirk:", value="Read the code on Muphs' Github to find out :smirk:", inline=False)
        embed.set_footer(text="NULL.™")
        embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-mePBN4Q8D4Cb9WZE-w1370.gif')
        await message.channel.send(embed=embed)



#credentials
load_dotenv('.env')

#run client
client.run(os.getenv('BOT_TOKEN'))
