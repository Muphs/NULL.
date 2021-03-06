"""imports"""
from inspect import ArgInfo
import discord
from discord import *
from discord.ext import *
from discord.ext import commands
from discord.ext.commands.errors import UserNotFound
from discord.utils import *
import asyncio
import time
from discord import ext
from dotenv import load_dotenv
import os
import random
import json
import requests
from discord import member
from discord import Embed
from discord.utils import get
import youtube_dl
from youtube_search import YoutubeSearch
import datetime
import time
from jsonmerge import merge

"""defining variables"""
load_dotenv('.env')
bot_token = (os.getenv('BOT_TOKEN'))
prefix = (os.getenv('PREFIX'))
description = (os.getenv('DESCRIPTION'))
thumbnail = (os.getenv('THUMBNAIL'))
thumbnail_small = (os.getenv('THUMBNAIL_SMALL'))
fapikey = (os.getenv('FAPI_KEY'))
ipapi_key = (os.getenv('IPAPI_KEY'))
jsonbin_key = (os.getenv('JSONBIN_KEY'))
jsonbin_id = (os.getenv('JSONBIN_ID'))
color = 0xff9efc
bot = commands.Bot(command_prefix=(prefix), case_insensitive=True)
#bot.remove_command('help')

"""on ready event"""
@bot.event
async def on_ready():
    global startTime
    startTime = datetime.datetime.now().replace(microsecond=0)
    await bot.change_presence(activity=discord.Streaming(name='Back Online!', url=(os.getenv('STREAM_URL'))))
    print("------------------------------------")
    print("Bot Name: " + bot.user.name)
    print("Bot ID: " + str(bot.user.id))
    print("Servers: "+ str(len(bot.guilds)))
    print("Discord.py Version: " + discord.__version__)
    print("------------------------------------")
    print("Print statements / errors:")
    time.sleep(5)
    await bot.change_presence(activity=discord.Streaming(name=(os.getenv('STREAM')), url=(os.getenv('STREAM_URL'))))

"""language code"""
@bot.event
async def on_guild_join(guild):
    headers = {'Content-Type': 'application/json', 'X-Master-Key': jsonbin_key, 'X-Bin-Versioning': "false"}
    prev_get_data= requests.get(f'https://api.jsonbin.io/v3/b/{jsonbin_id}', headers=headers)
    prev_json_data = json.loads(prev_get_data.text)
    prev_json_data_processed = prev_json_data['record']
    if guild.id in prev_json_data_processed:
        return
    else:
        new_json_data = {
            f"{guild.id}": "en"
        }
        new_json_data_processed = merge(prev_json_data_processed, new_json_data)
        req = requests.put(f'https://api.jsonbin.io/v3/b/{jsonbin_id}', json=new_json_data_processed , headers=headers)
        print(f"Guild {guild.id} has been added to JSON.")



"""commands"""

@bot.command(aliases=['hi'])
async def hello(ctx):
    greetings_list = ['Hi', 'Hey!', 'Sup', 'Hello!', 'Hemlo :)', 'Hai', 'Hey, how are you? :)', "Hi, how are you doing?"]
    lucky_num = random.randint(0,len(greetings_list) - 1)
    embed=discord.Embed(title=greetings_list[lucky_num], color=color)
    embed.set_footer(text=description)
    embed.set_thumbnail(url=thumbnail)
    message = await ctx.reply(embed=embed, mention_author=True)

@bot.command(aliases=['simonsays', 'repeatafterme'])
async def say(ctx, *, arg):
    if len(arg) >= 256:
        embed=discord.Embed(title="This message is too long! The message has to be less than 256 characters long.", color=color)
        embed.set_footer(text=description)
        embed.set_thumbnail(url=thumbnail)
        message = await ctx.reply(embed=embed, mention_author=True)
        time.sleep(2.5)
        await message.delete()
    else:
        if ctx.author.id == 726512497649254481 or ctx.author.id == 783417515236917260:
            embed=discord.Embed(title="You're blocked from using this message!", color=color)
            embed.set_footer(text=description)
            embed.set_thumbnail(url=thumbnail)
            message = await ctx.reply(embed=embed, mention_author=True)
            time.sleep(2.5)
            await message.delete()
        elif ctx.author.id == 421506951269056522:
            embed=discord.Embed(title=(arg), color=color)
            embed.set_footer(text=description)
            if len(arg) >= 50:
                embed.set_thumbnail(url=thumbnail_small)
            else:
                embed.set_thumbnail(url=thumbnail)
            await ctx.send(embed=embed, mention_author=True)
            await ctx.message.delete()
        else:
            embed=discord.Embed(title=arg, color=color)
            embed.set_footer(text=description)
            if len(arg) >= 50:
                embed.set_thumbnail(url=thumbnail_small)
            else:
                embed.set_thumbnail(url=thumbnail)
            await ctx.reply(embed=embed, mention_author=True)

@bot.command()
async def ping(ctx):
    embed=discord.Embed(title="Pong! :ping_pong:", color=color, description=(f'Ponged back in `{round(bot.latency * 1000)}ms`'))
    embed.set_footer(text=description)
    embed.set_thumbnail(url=thumbnail)
    message = await ctx.reply(embed=embed, mention_author=False)

@bot.command()
async def addbot(ctx):
    embed=discord.Embed(title="Add me to your server by clicking here!", url="https://bit.ly/null-bot-add", color=color)
    embed.add_field(name="Notice:", value="NULL. Is still in the development, which may cause commands to not work and the bot to be offline from now and then with no schedule.", inline=False)
    embed.set_footer(text=description)
    embed.set_thumbnail(url=thumbnail)
    message = await ctx.reply(embed=embed, mention_author=True)

@bot.command()
async def joinserver(ctx):
    embed=discord.Embed(title="Join my server by clicking here!",url="https://bit.ly/null-bot-join", color=color)
    embed.set_footer(text=description)
    embed.set_thumbnail(url=thumbnail)
    message = await ctx.reply(embed=embed, mention_author=True)

@bot.command(aliases=['information', 'botinfo', 'botinformation'])
async def info(ctx):
    timeNow = datetime.datetime.now().replace(microsecond=0)
    deltaUpTIme = timeNow - startTime
    embed=discord.Embed(color=color)
    embed.add_field(name="Bot version:", value="Alpha 0.5.1 Pre-Release")
    embed.add_field(name='Discord.py version:', value=discord.__version__)
    embed.add_field(name='Servers I currently serve:', value=str(len(bot.guilds)))
    embed.add_field(name='Uptime:', value=str(deltaUpTIme))
    embed.set_footer(text=description)
    embed.set_thumbnail(url=thumbnail)
    message = await ctx.reply(embed=embed, mention_author=True)

@bot.command(aliases=['8ball', 'magic8ball'])
async def m8b(ctx):
    response_list = ['100% sure!', 'definitely not', 'no :(', 'yes :)', 'hmmmmmm, idk', 'maybe ask again', 'maybe ask someone else', "definitely!", "As I see it, yes!", "Yes!", "No!", "Very likely!", "Not even close!", "Maybe!", "Very unlikely!", "Ask again later!", "Better not tell you now!", " It is certain!", "My sources say no", "Outlook good!", "Very Doubtful!", "Without a doubt!", 'no:heart:']
    lucky_num = random.randint(0,len(response_list)-1)
    embed=discord.Embed(title=response_list[lucky_num], color=color)
    embed.set_footer(text=description)
    embed.set_thumbnail(url=thumbnail)
    message = await ctx.reply(embed=embed, mention_author=True)

@bot.command()
async def compliment(ctx):
    compliment_list = ['You have the best laugh.', 'Our system of inside jokes is so advanced that only you and I get it. And I like that.', 'Your perspective is refreshing.', 'You deserve a hug right now.', 'You’re more helpful than you realize.', 'You have a great sense of humor.', 'On a scale from 1 to 10, you’re an 11.', 'You’re even more beautiful on the inside than you are on the outside.', 'If cartoon bluebirds were real, a bunch of them would be sitting on your shoulders singing right now.', 'Your ability to recall random factoids at just the right time is impressive.', 'You may dance like no one’s watching, but everyone’s watching because you’re an amazing dancer!', 'You’re more fun than a ball pit filled with candy. (And seriously, what could be more fun than that?)', 'Everyday is just BLAH when I don’t see you fr! ', 'If you were a box of crayons, you’d be the giant name-brand one with the built-in sharpener.', 'Everyone gets knocked down sometimes, but you always get back up and keep going.', 'You’re gorgeous — and that’s the least interesting thing about you, too.', 'If you were a scented candle they’d call it Perfectly Imperfect (and it would smell like summer).']
    lucky_num = random.randint(0,len(compliment_list)-1)
    embed=discord.Embed(title=compliment_list[lucky_num], color=color)
    embed.set_footer(text=description)
    embed.set_thumbnail(url=thumbnail)
    message = await ctx.reply(embed=embed, mention_author=True)

@bot.command()
async def pickupline(ctx):
    pickup_list = ["Even if there was no gravity, i'd still fall for you", "Do you like raisins? How do you feel about a date?", "If I could rearrange the alphabet, I’d put ‘U’ and ‘I’ together.", "If you were a Transformer… you’d be Optimus Fine.", "Are you a parking ticket? Because you’ve got FINE written all over you.", "I'm no photographer, but I can picture us together.", "Are you related to Jean-Claude Van Damme? Because Jean-Claude Van Damme you’re sexy!", "are you from Tenesse? cus you are the only 10 i see", "Baby, if you were words on a page, you’d be fine print.", "You must be a high test score, because I want to take you home and show you to my mother", "I was blinded by your beauty; I’m going to need your name and phone number for insurance purposes.", "I was wondering if you had an extra heart. Because mine was just stolen.", "Is your name Google? Because you have everything I’ve been searching for.", "You’re so gorgeous you made me forget what my pick up line was", "Im learning of important dates in history, wanna be one?", "i must be in a museum, because you are truly a work of art", "If you cant live without something, it should be free. I can't live without you, so, when are you free?"]
    lucky_num = random.randint(0,len(pickup_list)-1)
    embed=discord.Embed(title=pickup_list[lucky_num], color=color)
    embed.set_footer(text=description)
    embed.set_thumbnail(url=thumbnail)
    message = await ctx.reply(embed=embed, mention_author=True)

@bot.command()
async def roast(ctx):
    roast_list = ['You’re the reason God created the middle finger.', 'You’re a grey sprinkle on a rainbow cupcake.', 'If your brain was dynamite, there wouldn’t be enough to blow your hat off.', 'You are more disappointing than an unsalted pretzel.', 'someday you’ll go far, stay there', 'Light travels faster than sound which is why you seemed bright until you spoke.', 'You have so many gaps in your teeth it looks like your tongue is in jail.', 'I wasn’t born with enough middle fingers to let you know how I feel about you', 'If I wanted to kill myself id climb your ego and jump to your IQ', 'Your face makes onions cry.', 'I would love to insult you, but I’m afraid I won’t do as well as nature did', 'If you’re going to be two-faced, at least make one of them pretty.', 'whenever you swim, you just add another piece of trash to the ocean', 'Zombies eat brains, you’re safe']
    lucky_num = random.randint(0,len(roast_list)-1)
    embed=discord.Embed(title=roast_list[lucky_num], color=color)
    embed.set_footer(text=description)
    embed.set_thumbnail(url=thumbnail)
    message = await ctx.reply(embed=embed, mention_author=True)

@bot.command(aliases=['milkyeet', 'mario', 'mariojudah', 'yeet'])
async def milk(ctx):
    embed=discord.Embed(title='YEEEEEEEEEEEEEEEEEEEEET', color=color)
    embed.set_image(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/mario-judah-throws-milk-_-m2WjP9Gx6yHOB0J1-w1370.gif')
    embed.set_footer(text=description)
    embed.set_thumbnail(url=thumbnail_small)
    message = await ctx.reply(embed=embed, mention_author=True)

@bot.command(aliases=['anime'])
async def cuteanime(ctx):
    anime_list = ["https://cdn.discordapp.com/emojis/814696607974031400.gif", "https://media1.tenor.com/images/c925511d32350cc04411756d623ebad6/tenor.gif?itemid=13462237", "https://media1.tenor.com/images/89289af19b7dab4e21f28f03ec0faaff/tenor.gif?itemid=12801687", "https://media1.tenor.com/images/e1f44b9d914ba61cc60efd8d3cf439a5/tenor.gif?itemid=9975267", "https://media.tenor.com/images/1d37a873edfeb81a1f5403f4a3bfa185/tenor.gif", "https://media.tenor.com/images/8f711b12e00bc1816694bf51909f8b8f/tenor.gif", "https://media.tenor.com/images/84e609c97fc79323c572baa4e8486473/tenor.gif", "https://media.tenor.com/images/c67648bdadbece24eed182a401abf576/tenor.gif", "https://media.tenor.com/images/46a74ce6228e7bc535263e1464cce46b/tenor.gif", "https://media.tenor.com/images/a173f1c95d81855afd10d51f3fa277ab/tenor.gif", "https://media.tenor.com/images/e1c9ad053d4aa0471727fbf36c3a3868/tenor.gif", "https://media.tenor.com/images/3f6457f7235edf481d542b8074740401/tenor.gif"]
    lucky_num = random.randint(0,len(anime_list)-1)
    embed=discord.Embed(title='Awww', color=color)
    embed.set_image(url=anime_list[lucky_num])
    embed.set_footer(text=description)
    embed.set_thumbnail(url=thumbnail_small)
    message = await ctx.reply(embed=embed, mention_author=True)

@bot.command(aliases=['02'])
async def zerotwo(ctx):
    zerotwo_list = ['https://media.tenor.com/images/4632e943653b0ad278a1fa7b8f49d82c/tenor.gif', 'https://media.tenor.com/images/3e7d551f4edbc139f1372a494eccd01d/tenor.gif', 'https://media.tenor.com/images/e046bd4175889014749d008bef023f25/tenor.gif', 'https://media.tenor.com/images/500953247d7ddda4d87908fa0bb2c7bc/tenor.gif', 'https://media.tenor.com/images/2e094b3c1f5bf047698dea434416d080/tenor.gif', 'https://media.tenor.com/images/09df52e29a5506287cd76fb4abafa2cc/tenor.gif', 'https://media.tenor.com/images/4f5f2d78f721fc36e10f4e5e2c340f47/tenor.gif', 'https://media.tenor.com/images/7691590d6ac021b483c39dfa794e2a1c/tenor.gif', 'https://64.media.tumblr.com/d03212d8697607c82bb85db886ee92af/tumblr_p2z0hgMv3g1wd81ruo1_540.gifv']
    lucky_num = random.randint(0,len(zerotwo_list)-1)
    embed=discord.Embed(title='Boku no darling!', color=color)
    embed.set_image(url=zerotwo_list[lucky_num])
    embed.set_footer(text=description)
    embed.set_thumbnail(url=thumbnail_small)
    message = await ctx.reply(embed=embed, mention_author=True)

@bot.command()
async def todoroki(ctx):
    todoroki_list = ['https://pa1.narvii.com/6894/c584fe56b8dde82ac901aeb8e359cb2e157c3bdfr1-533-300_hq.gif', 'https://media1.tenor.com/images/30638e057d7c84c963619c3f9ab2a3df/tenor.gif?itemid=18024441', 'https://img.wattpad.com/e366789b1d68a2190987c27b2378395b6c0c7d66/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f776174747061642d6d656469612d736572766963652f53746f7279496d6167652f3152537645325f4f32366f6155673d3d2d3736373439353134382e313562376137353763303434343138363934363130373235393332302e676966?s=fit&w=720&h=720', 'https://i.pinimg.com/originals/2e/31/93/2e31935a326bdff0e6d1b91ae03d607f.gif', 'https://p.favim.com/orig/2018/08/01/boku-no-hero-academia-my-hero-academia-todoroki-shouto-Favim.com-6107451.gif']
    lucky_num = random.randint(0,len(todoroki_list)-1)
    embed=discord.Embed(title='Awww', color=color)
    embed.set_image(url=todoroki_list[lucky_num])
    embed.set_footer(text=description)
    embed.set_thumbnail(url=thumbnail_small)
    message = await ctx.reply(embed=embed, mention_author=True)

@bot.command()
async def ichigo(ctx):
    ichigo_list = ['https://media.tenor.com/images/d1fc46f2d0fd52740711b80b80a3c081/tenor.gif', 'https://media.tenor.com/images/b7687ce05975ad1d5c7ed52717e62f09/tenor.gif', 'https://data.whicdn.com/images/325037756/original.gif']
    lucky_num = random.randint(0,len(ichigo_list)-1)
    embed=discord.Embed(title='Awww', color=color)
    embed.set_image(url=ichigo_list[lucky_num])
    embed.set_footer(text=description)
    embed.set_thumbnail(url=thumbnail_small)
    message = await ctx.reply(embed=embed, mention_author=True)

#bunny girl
@bot.command(aliases=['bunnygirlsenpai', 'bunnyg'])
async def bunnygirl(ctx):
    bunnygirl_list = ['https://media1.tenor.com/images/be4bfaaa1458ec4d4231938851cf085b/tenor.gif?itemid=19678646', 'https://media1.tenor.com/images/37439858992a315486549b6136f8d74f/tenor.gif?itemid=17742393', 'https://media1.tenor.com/images/58a14f9ec0549c516134ab9940e871cd/tenor.gif?itemid=19611956', 'https://media1.tenor.com/images/567ba9e70f306c5ce6432377840437d3/tenor.gif?itemid=14746195', 'https://media1.tenor.com/images/24408dbd5bf503ba838e5b9a65bd14e7/tenor.gif?itemid=13458967', 'https://media1.tenor.com/images/5f3d0649a01125104a08894fa673af35/tenor.gif?itemid=15988113', 'https://media1.tenor.com/images/64b2de700d17667c45d3bf34e316a29c/tenor.gif?itemid=20119299', 'https://media1.tenor.com/images/d3b0bf5cda58616be62ec013ca75a38e/tenor.gif?itemid=15988109']
    lucky_num = random.randint(0,len(bunnygirl_list)-1)
    embed=discord.Embed(title='Awww', color=color)
    embed.set_image(url=bunnygirl_list[lucky_num])
    embed.set_footer(text=description)
    embed.set_thumbnail(url=thumbnail_small)
    message = await ctx.reply(embed=embed, mention_author=True)

@bot.command()
async def slap(ctx):
    slap_list = ['https://media.tenor.com/images/1d8edce282f3e36abc6b730357d3cea2/tenor.gif', 'https://media.tenor.com/images/47698b115e4185036e95111f81baab45/tenor.gif', 'https://media.tenor.com/images/01cd05bde1ebcdd0efa9648db9c9e02b/tenor.gif', 'https://media.tenor.com/images/dc569ca06234b85e11177e4d5ac55e21/tenor.gif', 'https://media.tenor.com/images/4abceefdd1c6713471486ad4369f63e1/tenor.gif', 'https://media.tenor.com/images/39cf2806683782606bd6185528bf3fba/tenor.gif', 'https://media.tenor.com/images/daa9848169a4919967766555a8958fbb/tenor.gif', 'https://media.tenor.com/images/3d708f9789961e31a84aae0395361747/tenor.gif', 'https://media.tenor.com/images/ad8a2b661e5c9d69e90a46e587231f23/tenor.gif', 'https://media.tenor.com/images/1d65e3710ac1e73647dafebe2f4727d9/tenor.gif', 'https://media.tenor.com/images/5eaa11874c0cc46d4d6aeb929066766a/tenor.gif', 'https://media.tenor.com/images/d76151f7a50376264fe599165aea066d/tenor.gif', 'https://media.tenor.com/images/507022c3e5862960cc363f330b94d391/tenor.gif']
    slapresponse_list = ['oof, that must hurt', 'they must be dead', 'looks like someone got slapped lol']
    lucky_num = random.randint(0,len(slap_list)-1)
    lucky_num = random.randint(0,len(slapresponse_list)-1)
    embed=discord.Embed(title=(slapresponse_list[lucky_num]), color=color)
    embed.set_image(url=slap_list[lucky_num])
    embed.set_footer(text=description)
    embed.set_thumbnail(url=thumbnail_small)
    message = await ctx.reply(embed=embed, mention_author=True)

@bot.command()
async def hug(ctx):
    hug_list = ['https://media.tenor.com/images/bb67bef5f54d0191b7e2d3c1fd6e4bd3/tenor.gif', 'https://media.tenor.com/images/a9bb4d55724484be94d13dd94721a8d9/tenor.gif', 'https://media.tenor.com/images/a9730f44f28d959abb4c5b31edc77de8/tenor.gif', 'https://media.tenor.com/images/ca88f916b116711c60bb23b8eb608694/tenor.gif', 'https://media.tenor.com/images/1ca37ea5d3ec66ea08893d8679c04ae1/tenor.gif', 'https://media.tenor.com/images/9fe95432f2d10d7de2e279d5c10b9b51/tenor.gif', 'https://media.tenor.com/images/f2d41b50c49426ea42411f14779a7c1c/tenor.gif', 'https://media.tenor.com/images/8d33eeee359d0453de52c5779dd23c46/tenor.gif', 'https://media.tenor.com/images/2e1d34d002d73459b6119d57e6a795d6/tenor.gif', ]
    hugresponse_list = ['Awwwww, what a cute hug', 'i feel lonely <:apple_plead:812381767432536125>']
    lucky_num = random.randint(0,len(hug_list)-1)
    lucky_num = random.randint(0,len(hugresponse_list)-1)
    embed=discord.Embed(title=hugresponse_list[lucky_num], color=color)
    embed.set_image(url=hug_list[lucky_num])
    embed.set_footer(text=description)
    embed.set_thumbnail(url=thumbnail_small)
    message = await ctx.reply(embed=embed, mention_author=True)

@bot.command()
async def kiss(ctx):
    kiss_list = ['https://media.tenor.com/images/6702ca08b5375a74b6b9805382021f73/tenor.gif', 'https://media.tenor.com/images/924c9665eeb727e21a6e6a401e60183b/tenor.gif', 'https://media.tenor.com/images/197df534507bd229ba790e8e1b5f63dc/tenor.gif', 'https://media.tenor.com/images/21fed1c94754d21acdbccd52adfb53d0/tenor.gif', 'https://media.tenor.com/images/7b50048d76f76a8e5b3d8fc5a3fc6a21/tenor.gif', 'https://media.tenor.com/images/1f9175e76488ebf226de305279151752/tenor.gif', 'https://media.tenor.com/images/29b22bb26ecc0943c95b9a1be81d3054/tenor.gif', 'https://media.tenor.com/images/25359520a0973f896b002689ed90db8d/tenor.gif', 'https://media.tenor.com/images/7e640ecfea0090dd0e29b998c625c642/tenor.gif', 'https://media.tenor.com/images/48963a8342fecf77d8eabfd2ab2e75c1/tenor.gif', 'https://media.tenor.com/images/45246226e54748be5175ab15206de1c5/tenor.gif', 'https://media.tenor.com/images/822b11c4ab7843229fdd4abf5ccadf61/tenor.gif', 'https://media.tenor.com/images/7fefdf515b268e92554654a115211ce3/tenor.gif']
    kissresponse_list = ['I feel lonely <:apple_plead:812381767432536125>', 'I really need a gf <:apple_plead:812381767432536125>']
    lucky_num = random.randint(0,len(kiss_list)-1)
    lucky_num = random.randint(0,len(kissresponse_list)-1)
    embed=discord.Embed(title=kissresponse_list[lucky_num], color=color)
    embed.set_image(url=kiss_list[lucky_num])
    embed.set_footer(text=description)
    embed.set_thumbnail(url=thumbnail_small)
    message = await ctx.reply(embed=embed, mention_author=True)

@bot.command()
async def sigh(ctx):
    sigh_list = ['https://media1.tenor.com/images/34b67ecddde773b30dbe962d14ff27c7/tenor.gif?itemid=20668021']
    lucky_num = random.randint(0,len(sigh_list)-1)
    embed=discord.Embed(title='`*sighs*`', color=color)
    embed.set_image(url=sigh_list[lucky_num])
    embed.set_footer(text=description)
    embed.set_thumbnail(url=thumbnail_small)
    message = await ctx.reply(embed=embed, mention_author=True)

@bot.command()
async def clap(ctx):
    clap_list = ['https://media1.tenor.com/images/7460a26a07ef24d696eaac0b0ff4d5bf/tenor.gif?itemid=16461487', 'https://media.tenor.com/images/ba246f4d3f2845cac07466ab3d013279/tenor.gif', 'https://media.tenor.com/images/657f0c243282921245c0b9f4b1525c1b/tenor.gif', 'https://media.tenor.com/images/2cf9843ed2489b97be6ca65acd40b55f/tenor.gif', 'https://media.tenor.com/images/07908bbd4b8336d826c733de9b2f2988/tenor.gif', 'https://media.tenor.com/images/18ae86fcb295c6d30028dedf7a946970/tenor.gif', 'https://media.tenor.com/images/9f94b89d628518c67808ebadba924306/tenor.gif', 'https://media.tenor.com/images/bd235c84724d5eb04b5cfe39028e936c/tenor.gif']
    lucky_num = random.randint(0,len(clap_list)-1)
    embed=discord.Embed(title='`*clap*` `*clap*` `*clap*`', color=color)
    embed.set_image(url=clap_list[lucky_num])
    embed.set_footer(text=description)
    embed.set_thumbnail(url=thumbnail_small)
    message = await ctx.reply(embed=embed, mention_author=True) 

@bot.command()
async def dababy(ctx):
    dababy_list = ['https://media.tenor.com/images/57440c61f7c098edcf19e89064fcbbf7/tenor.gif', 'https://media1.tenor.com/images/c8edfdc06ef1c0cd01f03eaa20d8f8b7/tenor.gif?itemid=20883016', 'https://media1.tenor.com/images/fb4990d28060529e74d53b24fa9fa012/tenor.gif?itemid=15748120', 'https://media1.tenor.com/images/44e37453e27d700edbae6f112b9acd41/tenor.gif?itemid=20757217', 'https://cdn.discordapp.com/emojis/818521259125112893.gif?v=1', 'https://media.tenor.com/images/57440c61f7c098edcf19e89064fcbbf7/tenor.gif', 'https://media1.tenor.com/images/c8edfdc06ef1c0cd01f03eaa20d8f8b7/tenor.gif?itemid=20883016', 'https://media1.tenor.com/images/fb4990d28060529e74d53b24fa9fa012/tenor.gif?itemid=15748120', 'https://media1.tenor.com/images/44e37453e27d700edbae6f112b9acd41/tenor.gif?itemid=20757217', 'https://cdn.discordapp.com/emojis/818521259125112893.gif?v=1', 'https://media.tenor.com/images/57440c61f7c098edcf19e89064fcbbf7/tenor.gif', 'https://media1.tenor.com/images/c8edfdc06ef1c0cd01f03eaa20d8f8b7/tenor.gif?itemid=20883016', 'https://media1.tenor.com/images/fb4990d28060529e74d53b24fa9fa012/tenor.gif?itemid=15748120', 'https://media1.tenor.com/images/44e37453e27d700edbae6f112b9acd41/tenor.gif?itemid=20757217', 'https://cdn.discordapp.com/emojis/818521259125112893.gif?v=1']
    lucky_num = random.randint(0,len(dababy_list)-1)
    embed=discord.Embed(title='LESSSS GOOOOO :smiling_imp: :cold_face: :hot_face: :exclamation::exclamation: ', color=color)
    embed.set_image(url=dababy_list[lucky_num])
    embed.set_footer(text=description)
    embed.set_thumbnail(url=thumbnail_small)
    message = await ctx.reply(embed=embed, mention_author=True)

@bot.command()
async def hamster(ctx):
    hamster_list = ['https://wallpaperaccess.com/full/1646379.jpg', 'https://i.pinimg.com/736x/f4/44/e7/f444e7650cfec94d5b4b8a3b4e5736f3.jpg', 'https://www.irishtimes.com/polopoly_fs/1.3521320.1528297311!/image/image.jpg_gen/derivatives/ratio_1x1_w1200/image.jpg', 'https://s7d2.scene7.com/is/image/PetSmart/5081325', 'https://www.vin.com/AppUtil/Image/handler.ashx?imgid=4476518&w=325&h=323', 'https://static.maskokotas.com/blog/wp-content/uploads/2020/01/hamster-cuidados-manejo.jpg', 'https://i.natgeofe.com/n/bc0b53c1-e57e-4708-b592-f11e6ef855c0/european-hamsters-1.jpg?w=636&h=424', 'https://www.wittemolen.com/sites/default/files/styles/full_width/public/slides/SLIDER-Hamster.jpg?itok=t7h_LCJE', 'https://i.pinimg.com/originals/7e/b7/45/7eb745f90461e87655b755eaea1c1d41.jpg', 'https://www.parksidevets.com/pets/wp-content/uploads/sites/2/2019/05/parksite-vets-Hamster-care.jpg', 'https://www.omlet.com/images/originals/Russian_winter_white_pouches.jpg', 'https://www.burgesspetcare.com/wp-content/uploads/2020/02/hamster-diets.jpg']
    lucky_num = random.randint(0,len(hamster_list)-1)
    embed=discord.Embed(title='Awww', color=color)
    embed.set_image(url=hamster_list[lucky_num])
    embed.set_footer(text=description)
    embed.set_thumbnail(url=thumbnail_small)
    message = await ctx.reply(embed=embed, mention_author=True)

@bot.command()
async def frog(ctx):
    frog_list = ["https://ih1.redbubble.net/image.1448785672.7225/st,small,507x507-pad,600x600,f8f8f8.jpg", "https://media.istockphoto.com/vectors/cute-frog-cartoon-hand-drawn-style-vector-id1146849256", "https://reneelertzman.com/wp-content/uploads/2016/03/cute-little-green-frog-peeking-out-from-behind-PT9JUFJ.jpg", "https://ih1.redbubble.net/image.1490694325.8717/fposter,small,wall_texture,product,750x1000.jpg", "https://www.crushpixel.com/big-static12/preview4/cute-frog-seamless-pattern-background-1094038.jpg", "https://www.crushpixel.com/big-static12/preview4/cute-frog-seamless-pattern-background-1094038.jpg", "https://media.discordapp.net/attachments/791400172209963058/812447792114827274/IMG_20210217_180127_963.jpg", "http://onebigphoto.com/uploads/2014/09/hello-i-am-cute-frog.jpg", "https://imagesvc.meredithcorp.io/v3/mm/image?q=85&c=sc&poi=face&w=1503&h=1503&url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F20%2F2020%2F01%2Ffrog-trio-6.jpg", "https://media.discordapp.net/attachments/791400172209963058/812448117622046720/2lqtt9abx4561.png?width=371&height=500", "https://i.pinimg.com/originals/5c/a6/18/5ca6189bfca950c74ad266c30e587bb9.jpg", "http://1.bp.blogspot.com/-BkUS1SGdmLA/TpEiyhFFC4I/AAAAAAAAB3c/91Rh3vtHNT8/s1600/Cute-Frog-1.jpg", "https://media.discordapp.net/attachments/791400172209963058/812449043791085598/8mi859yc14251.png"]
    lucky_num = random.randint(0,len(frog_list)-1)
    embed=discord.Embed(title='Awww', color=color)
    embed.set_image(url=frog_list[lucky_num])
    embed.set_footer(text=description)
    embed.set_thumbnail(url=thumbnail_small)
    message = await ctx.reply(embed=embed, mention_author=True)

@bot.command()
async def jdm(ctx):
    jdm_list = ['https://images-ext-1.discordapp.net/external/52h-vS9a2mw65Fl7ITo7TuD0wdiGeneuTi0WlqIKays/https/soymotor.com/sites/default/files/imagenes/noticia/toyota-supra.jpg', 'https://images-ext-2.discordapp.net/external/kDofouMxYFqVGrwlHX3ZSy8l1d1L28zyKD6evy-EFMA/https/besthqwallpapers.com/Uploads/16-11-2019/111977/thumb2-nissan-s30-nissan-fairlady-z-tuning-datsun-240z-japanese-cars.jpg', 'https://images-ext-2.discordapp.net/external/OvGDRXylwLmqiccdMXBuPB76YlNE3eEpCJIC33AfgJc/https/www.motorbiscuit.com/wp-content/uploads/2020/10/1986-JDM-Toyota-AE86-Sprinter-Trueno-GT-Apex.jpg', 'https://images-ext-1.discordapp.net/external/mWPXDCBHCJPP-BPzgy10u-hefrtGcwI6QoJg405nTD0/https/i.pinimg.com/originals/88/83/bd/8883bd844c3046df557c7381d0633626.jpg', 'https://images-ext-2.discordapp.net/external/XCCVt9Kwv25RQV68Ad_1F4QnvbsELNGPvxrv9jpI_20/https/i.pinimg.com/originals/67/ff/ea/67ffeab000d8e7033e60360ea0a3bcce.jpg', 'https://images-ext-1.discordapp.net/external/ymHMBTo2uS6Ujq3okVeB2MEN6HLMmaTF3CavIAhJkXA/https/frenomotor.com/files/2015/04/skyline-paul-walker.jpg']
    lucky_num = random.randint(0,len(jdm_list)-1)
    embed=discord.Embed(color=color)
    embed.set_image(url=jdm_list[lucky_num])
    embed.set_footer(text=description)
    embed.set_thumbnail(url=thumbnail_small)
    message = await ctx.reply(embed=embed, mention_author=True)

@bot.command()
async def therock(ctx):
    rock_list = ['https://static.onecms.io/wp-content/uploads/sites/6/2016/11/dwayne-johnson.jpg', 'https://media.discordapp.net/attachments/791400172209963058/833880348143779840/Z.png', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRNniGFdkhKMp8dqSGYjDtnHnoF7IwH2nDSOiGuvk3JHj-Wt_VehhGHqIoZ6OiMNBmuR1I&usqp=CAU', 'https://media.discordapp.net/attachments/791400172209963058/833880832317718538/xqkvbXm.png', 'https://i.redd.it/d1qb1dqby73z.jpg', 'https://pics.me.me/dwayne-the-block-johnson-it-ain%E2%80%99t-butter-but-it%E2%80%99s-hard-62078044.png', 'https://media.discordapp.net/attachments/791400172209963058/833881114120159282/image0.jpg', 'https://pics.me.me/dwayne-the-log-johnson-me-irl-22713272.png', 'https://media.discordapp.net/attachments/791400172209963058/833881332651524157/image0.jpg', 'https://i.redd.it/pyd4r36xhcd41.jpg', 'https://i.imgur.com/o3hJf5H.jpg', 'https://i.pinimg.com/originals/4e/04/62/4e04622da507fcf31886b1dbc4da339a.png', 'https://pics.me.me/dwane-the-bop-johnson-spiy-fltk-it-twist-very-funny-51837846.png', 'https://pics.onsizzle.com/144p-1080p-4k-evolution-of-the-rock-23053816.png', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTe2M5nD9tqjFtdRdi91LgW3wi9T8X-m-UJmg&usqp=CAU', 'https://i.pinimg.com/originals/6c/82/5d/6c825d1140b2e2e4f7129ac0a015e3b0.png']
    lucky_num = random.randint(0,len(rock_list)-1)
    embed=discord.Embed(color=color)
    embed.set_image(url=rock_list[lucky_num])
    embed.set_footer(text=description)
    embed.set_thumbnail(url=thumbnail_small)
    message = await ctx.reply(embed=embed, mention_author=True)

@bot.command()
async def howsus(ctx):
    if ctx.author.id == 421506951269056522:
        embed=discord.Embed(title="0% sus:", color=color)
        embed.set_footer(text=description)
        embed.set_thumbnail(url=thumbnail)
        message = await ctx.reply(embed=embed, mention_author=True)
    else:
        sus = random.randint(0, 100)
        embed=discord.Embed(title=f"{str(sus)}% sus", color=color)
        embed.set_footer(text=description)
        embed.set_thumbnail(url=thumbnail)
        message = await ctx.reply(embed=embed, mention_author=True)

@bot.command()
async def howgay(ctx):
    if ctx.author.id == 421506951269056522:
        embed=discord.Embed(title="0% gay :gay_pride_flag:", color=color)
        embed.set_footer(text=description)
        embed.set_thumbnail(url=thumbnail)
        message = await ctx.reply(embed=embed, mention_author=True)
    else:
        gay = random.randint(0, 100)
        embed=discord.Embed(title=f"{str(gay)}% gay :gay_pride_flag:", color=color)
        embed.set_footer(text=description)
        embed.set_thumbnail(url=thumbnail)
        message = await ctx.reply(embed=embed, mention_author=True)

@bot.command()
async def iq(ctx):
    if ctx.author.id == 421506951269056522:
        embed=discord.Embed(title="1000 IQ", color=color)
        embed.set_footer(text=description)
        embed.set_thumbnail(url=thumbnail)
        message = await ctx.reply(embed=embed, mention_author=True)
    else:
        iq = random.randint(0, 1000)
        embed=discord.Embed(title=f"{str(iq)} IQ", color=color)
        embed.set_footer(text=description)
        embed.set_thumbnail(url=thumbnail)
        message = await ctx.reply(embed=embed, mention_author=True)

@bot.command(aliases=['quote'])
async def inspire(ctx):
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    embed=discord.Embed(title=quote, color=color)
    embed.set_footer(text=description)
    embed.set_thumbnail(url=thumbnail)
    message = await ctx.reply(embed=embed, mention_author=True)

@bot.command(aliases=['randomfact'])
async def fact(ctx):
    factapi = requests.get('https://useless-facts.sameerkumar.website/api')
    json_data = json.loads(factapi.text)
    fact = json_data['data']
    embed=discord.Embed(title=fact, color=color)
    embed.set_footer(text=description)
    embed.set_thumbnail(url=thumbnail)
    message = await ctx.reply(embed=embed, mention_author=True)

@bot.command(aliases=['random'])
async def rand(ctx, arg1, arg2, arg3):
    if arg1 == '-num' or arg1 == '-number' or arg1 == '-n':
        rng = random.randint((int(arg2)), (int(arg3)))
        embed=discord.Embed(title=f'Your random number is **{str(rng)}**', color=color)
        embed.set_footer(text=description)
        embed.set_thumbnail(url=thumbnail)
        message = await ctx.reply(embed=embed, mention_author=True)
    elif arg1 == '-img' or arg1 == '-image':
        picgen = random.randint(0, 999999999999999999999999999999999999999999999999999999)
        embed=discord.Embed(title=' ', color=color)
        embed.set_image(url=f'https://picsum.photos/seed/{str(picgen)}/3840/2160')
        embed.set_footer(text=description)
        embed.set_thumbnail(url=thumbnail_small)
        message = await ctx.reply(embed=embed, mention_author=True)

@bot.command(aliases=['covid19'])
async def covid(ctx):
    covid = requests.get('https://api.covid19api.com/world/total')
    json_data = json.loads(covid.text)
    embed=discord.Embed(title='COVID19 Info.', color=color)
    embed.set_thumbnail(url=thumbnail_small)
    embed.add_field(name="{:,}".format(json_data['TotalConfirmed']), value="Confirmed cases:", inline=True)
    embed.add_field(name="{:,}".format(json_data['TotalRecovered']), value="Recovered cases:", inline=True)
    embed.add_field(name="{:,}".format(json_data['TotalDeaths']), value="Deaths:", inline=True)
    embed.set_footer(text=description)
    message = await ctx.reply(embed=embed, mention_author=True)

@bot.command()
async def meme(ctx, *args):
    meme = requests.get('https://meme-api.herokuapp.com/gimme')
    json_data = json.loads(meme.text)
    global memeurl
    global memetitle
    global memeposturl
    global memesubreddit
    global memeauthor
    global memeups
    global memectxmsg
    memeNSFW = json_data['nsfw']
    memeurl = json_data['url']
    memetitle = json_data['title']
    memeposturl = json_data['postLink']
    memesubreddit = json_data['subreddit']
    memeauthor = json_data['author']
    memeups= json_data['ups']
    memectxmsg= ctx.message

    if not args:
        memeNSFW = json_data['nsfw']
    elif args[0] == 'debug':
        memeNSFW = 'true'

    if memeNSFW == 'true':
        embed=discord.Embed(title="This is an NSFW meme!", description="Do you still wanna view it?" , color=color)
        embed.set_footer(text=description)
        embed.set_thumbnail(url=thumbnail)
        global memensfwmessage
        memensfwmessage = await ctx.reply(embed=embed, mention_author=True)
        emojis = ['<:null_Y:849071815825162250>', '<:null_N:849071797671952394>']
        for emoji in emojis:
            await memensfwmessage.add_reaction(emoji)
    else:
        embed=discord.Embed(title=memetitle, url=memeposturl, description=f"Subreddit: {memesubreddit}\n Made by: {memeauthor}\n Upvotes: {memeups}" ,color=color)
        embed.set_image(url=memeurl)
        embed.set_footer(text=description)
        embed.set_thumbnail(url=thumbnail)
        message = await ctx.reply(embed=embed, mention_author=True)
@bot.event
async def on_reaction_add(reaction, user):
    if user.id == bot.user.id:
        return
    else:
        if reaction.message.id == memensfwmessage.id:
            memeembed=discord.Embed(title=memetitle, url=memeposturl, description=f"Subreddit: {memesubreddit}\n Made by: {memeauthor}\n Upvotes: {memeups}" ,color=color)
            memeembed.set_image(url=memeurl)
            memeembed.set_footer(text=description)
            memeembed.set_thumbnail(url=thumbnail)
            emojis = ['<:null_Y:849071815825162250>', '<:null_N:849071797671952394>']
            if str(reaction) == '<:null_Y:849071815825162250>':
                await memensfwmessage.edit(embed=memeembed)
                for emoji in emojis:
                    await memensfwmessage.remove_reaction(emoji, user)
                    await memensfwmessage.remove_reaction(emoji, bot.user)
            if str(reaction) == '<:null_N:849071797671952394>':
                await memensfwmessage.delete()
                await memectxmsg.delete()

@bot.command()
async def diceroll(ctx):
    dice = random.randint(1, 6)
    if str(dice) == '1':
        embed=discord.Embed(title=f'You rolled a {str(dice)}!', color=color)
        embed.set_footer(text=description)
        embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/824330739248005160.png?size=64')
        message = await ctx.reply(embed=embed, mention_author=True)
    elif str(dice) == '2':
        embed=discord.Embed(title=f'You rolled a {str(dice)}!', color=color)
        embed.set_footer(text=description)
        embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/824330526671765504.png?size=64')
        message = await ctx.reply(embed=embed, mention_author=True)
    elif str(dice) == '3':
        embed=discord.Embed(title=f'You rolled a {str(dice)}!', color=color)
        embed.set_footer(text=description)
        embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/824330652173729793.png?size=64')
        message = await ctx.reply(embed=embed, mention_author=True)
    elif str(dice) == '4':
        embed=discord.Embed(title=f'You rolled a {str(dice)}!', color=color)
        embed.set_footer(text=description)
        embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/824330571408474112.png?size=64')
        message = await ctx.reply(embed=embed, mention_author=True)
    elif str(dice) == '5':
        embed=discord.Embed(title=f'You rolled a {str(dice)}!', color=color)
        embed.set_footer(text=description)
        embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/824330607776759828.png?size=64')
        message = await ctx.reply(embed=embed, mention_author=True)
    elif str(dice) == '6':
        embed=discord.Embed(title=f'You rolled a {str(dice)}!', color=color)
        embed.set_footer(text=description)
        embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/824330708973518918.png?size=64')
        message = await ctx.reply(embed=embed, mention_author=True)

@bot.command(aliases=['dadjoke'])
async def joke(ctx):
    dad_joke = requests.get('https://official-joke-api.appspot.com/random_joke')
    json_data = json.loads(dad_joke.text)
    embed=discord.Embed(title=f"{json_data['setup']} {json_data['punchline']}",  color=color)
    embed.set_footer(text=description)
    embed.set_thumbnail(url=thumbnail)
    message = await ctx.reply(embed=embed, mention_author=True)

@bot.command(aliases=['kanyewest', 'ye'])
async def kanye(ctx):
    kanye = requests.get('https://api.kanye.rest/')
    json_data = json.loads(kanye.text)
    embed=discord.Embed(title=json_data['quote'], description='-Kanye West',  color=color)
    embed.set_footer(text=description)
    embed.set_thumbnail(url=thumbnail)
    message = await ctx.reply(embed=embed, mention_author=True)

@bot.command()
async def yomama(ctx):
    yomama = requests.get('https://api.yomomma.info/')
    json_data = json.loads(yomama.text)
    embed=discord.Embed(title=json_data['joke'],  color=color)
    embed.set_footer(text=description)
    embed.set_thumbnail(url=thumbnail)
    message = await ctx.reply(embed=embed, mention_author=True)

@bot.command()
async def stock(ctx, arg):
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-profile"
    querystring = {"symbol":arg}
    headers = {'x-rapidapi-key': fapikey, 'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    json_data = json.loads(response.text)
    embed=discord.Embed(title=json_data['price']['longName'], color=color)
    embed.add_field(name='Raw stock price', value=f"{json_data['price']['currencySymbol']}{str(json_data['price']['regularMarketPrice']['raw'])}", inline=True)
    embed.add_field(name='Stock price FMT', value=f"{json_data['price']['currencySymbol']}{str(json_data['price']['regularMarketPrice']['fmt'])}", inline=True)
    embed.set_footer(text=description)
    embed.set_thumbnail(url=thumbnail)
    message = await ctx.reply(embed=embed, mention_author=True)

@bot.command()
async def mcskin(ctx, arg):
    uuidAPI = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{arg}")
    uuidjson_data = json.loads(uuidAPI.text)
    embed=discord.Embed(title=uuidjson_data['name'], color=color)
    embed.set_image(url=f"https://crafatar.com/renders/body/{uuidjson_data['id']}?overlay=true&size=1920x1080")
    embed.set_footer(text=(description))
    embed.set_thumbnail(url=f"https://crafatar.com/renders/head/{uuidjson_data['id']}?overlay=true&size=1080x1080")
    message = await ctx.reply(embed=embed, mention_author=True)

@bot.command()
async def weather(ctx, arg):
    weatherapi = requests.get(f"https://api.weatherapi.com/v1/current.json?key={os.getenv('API_KEY')}&q={arg}")
    json_data = json.loads(weatherapi.text)
    embed=discord.Embed(title=f"{json_data['location']['name']}, {json_data['location']['country']}", color=color)
    embed.add_field(name="Time Zone", value=json_data['location']['tz_id'], inline=True)
    embed.add_field(name="Temperature °C", value=json_data['current']['temp_c'], inline=True)
    embed.add_field(name="Temperature °F", value=json_data['current']['temp_f'], inline=True)
    embed.add_field(name="Feels like °C", value=json_data['current']['feelslike_c'], inline=True)
    embed.add_field(name="Feels like °F", value=json_data['current']['feelslike_f'], inline=True)
    embed.add_field(name="Wind MPH", value=json_data['current']['wind_mph'], inline=True)
    embed.add_field(name="Wind KMPH", value=json_data['current']['wind_kph'], inline=True)
    embed.add_field(name="Wind Degree", value=json_data['current']['wind_degree'], inline=True)
    embed.add_field(name="Wind Direction", value=json_data['current']['wind_dir'], inline=True)
    embed.add_field(name="Pressure In", value=json_data['current']['pressure_in'], inline=True)
    embed.add_field(name="Precipitation mm", value=json_data['current']['precip_mm'], inline=True)
    embed.add_field(name="Visibility KM", value=json_data['current']['vis_km'], inline=True)
    embed.add_field(name="Visibility Miles", value=json_data['current']['vis_miles'], inline=True)
    embed.add_field(name="UV index", value=json_data['current']['uv'], inline=True)
    embed.add_field(name="Condition", value=json_data['current']['condition']['text'], inline=False)
    embed.set_image(url=f"https:{json_data['current']['condition']['icon']}")
    embed.set_footer(text=description)
    embed.set_thumbnail(url=thumbnail)
    message = await ctx.reply(embed=embed, mention_author=True)

@bot.command()
async def iplookup(ctx, arg):
    ip = requests.get(f"http://api.ipstack.com/{str(arg)}?access_key={ipapi_key}")
    json_data = json.loads(ip.text)
    embed=discord.Embed(title= (str(arg)) + ' Lookup result.', color=color)
    embed.add_field(name="IP address type:", value=json_data['type'], inline=True)
    embed.add_field(name="Continent:", value=json_data['continent_name'], inline=True)
    embed.add_field(name="Country:", value=f":flag_{json_data['country_code'].lower()}:", inline=True)
    embed.add_field(name="ZIP code:", value=json_data['zip'], inline=True)
    embed.add_field(name="Capital:", value=json_data['location']['capital'], inline=True)
    embed.set_footer(text=description)
    embed.set_thumbnail(url=thumbnail)
    message = await ctx.reply(embed=embed, mention_author=True)

@bot.command(aliases=['youtube', 'youtubesearch', 'yt'])
async def ytsearch(ctx, *args):
    if not args:
        embed=discord.Embed(title="You need to provide a search query like so:", description=f"> `{prefix}yt`/`youtube`/`youtubesearch`/`ytsearch` <your search>\n or: \n > `{prefix}yt`/`youtube`/`youtubesearch`/`ytsearch` `-l`/`-li`/`link` <your search>",color=(color))
        embed.set_footer(text=description)
        embed.set_thumbnail(url=thumbnail)
        message = await ctx.reply(embed=embed, mention_author=True)
    elif args[0] == '-l' or args[0] == '-li' or args[0] == '-link':
        results = YoutubeSearch(str(args[1:]), max_results=1).to_dict()
        await ctx.reply(f"https://youtube.com{results[0]['url_suffix']}")
    else:
        results = YoutubeSearch(str(args), max_results=1).to_dict()
        embed=discord.Embed(title=results[0]['title'], url=f"https://youtube.com{results[0]['url_suffix']}" ,color=(color))
        embed.set_image(url=results[0]['thumbnails'][0])
        embed.set_footer(text=description)
        embed.set_thumbnail(url=thumbnail_small)
        message = await ctx.reply(embed=embed, mention_author=True)

@bot.command()
async def hypixel(ctx, arg):
    uuidAPI = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{arg}")
    uuidjson_data = json.loads(uuidAPI.text)
    name = uuidjson_data['name']
    if name[-1] == 's':
        embed=discord.Embed(title=f"{name}' Hypixel stats:", color=color)
    else:
        embed=discord.Embed(title=f"{name}'s Hypixel stats:", color=color)
    embed.set_image(url=f"https://hypixel.paniek.de/signature/{uuidjson_data['id']}/general")
    embed.set_footer(text=description)
    embed.set_thumbnail(url=thumbnail_small)
    message = await ctx.reply(embed=embed, mention_author=True)

@bot.command(aliases=['define', 'definitionof'])
async def definition(ctx, *args):
    lang = args[0]
    if not args:
        lang = 'en_US'
    url = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/{lang}/{args[1]}")
    json_data = json.loads(url.text)
    embed=discord.Embed(title=f"{json_data[0]['word']} definition:", color=(color))
    embed.add_field(name="Pronunciation ", value=json_data[0]['phonetics'][0]['text'])
    embed.add_field(name="Definitions ", value=json_data[0]['meanings'][0]['definitions'][0]['definition'])
    embed.add_field(name="Examples ", value=json_data[0]['meanings'][0]['definitions'][0]['example'])
    embed.add_field(name="Synonym ", value=f"{json_data[0]['definitions']['synonyms'][0]}")
    embed.add_field(name="Audio URL ", value=json_data[0]['phonetics'][0]['audio'])
    embed.set_footer(text=(description))
    embed.set_thumbnail(url=(thumbnail))
    message = await ctx.reply(embed=embed, mention_author=True)
    print(json_data)

youtube_dl.utils.bug_reports_message = lambda: ''

#yt dl formatting (used for video downloading)
ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)


class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))
        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]
        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)


class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def join(self, ctx, *, channel: discord.VoiceChannel):
        """Joins a voice channel"""
        if ctx.voice_client is not None:
            return await ctx.voice_client.move_to(channel)
        await channel.connect(self_mute=False, self_deaf=True)

    @commands.command()
    async def play(self, ctx, *, arg):
        """Streams from a url (same as yt, but doesn't predownload)"""
        results = YoutubeSearch((arg), max_results=1).to_dict()
        async with ctx.typing():
            player = await YTDLSource.from_url(('https://youtube.com' + (results[0]['url_suffix'])), loop=self.bot.loop, stream=True)
            ctx.voice_client.play(player, after=lambda e: print(f'Player error: {e}') if e else None)
        embed=discord.Embed(title=f'Now playing: {player.title}', color=(color))
        embed.set_footer(text=(description))
        embed.set_image(url=(results[0]['thumbnails'][0]))
        embed.set_thumbnail(url=(thumbnail_small))
        message = await ctx.reply(embed=embed, mention_author=True)

    @commands.command()
    async def leave(self, ctx):
        """Stops and disconnects the bot from voice"""
        await ctx.voice_client.disconnect()
        embed=discord.Embed(title='Disconnected from voice channel.', color=(color))
        embed.set_footer(text=(description))
        embed.set_thumbnail(url=(thumbnail))
        message = await ctx.reply(embed=embed, mention_author=True)

    @play.before_invoke
    async def ensure_voice(self, ctx):
        if ctx.voice_client is None:
            if ctx.author.voice:
                await ctx.author.voice.channel.connect()
                embed=discord.Embed(title="Connected to voice channel!", color=(color))
                embed.set_footer(text=(description))
                embed.set_thumbnail(url=(thumbnail))
                message = await ctx.reply(embed=embed, mention_author=True)
            else:
                embed=discord.Embed(title="You aren't connected to a voice channel!", color=(color))
                embed.set_footer(text=(description))
                embed.set_thumbnail(url=(thumbnail))
                message = await ctx.reply(embed=embed, mention_author=True)
                raise commands.CommandError("Author not connected to a voice channel.")
        elif ctx.voice_client.is_playing():
            ctx.voice_client.stop()

"""RULES COMMAND FOR NULL'S SERVER ONLY"""
@bot.command()
async def rules(ctx):
    if ctx.author.id != 421506951269056522:
        return
    else:
        embed=discord.Embed(color=(color))
        embed.set_image(url='https://media.discordapp.net/attachments/828838646626910208/842506808807129148/ezgif.com-gif-maker_1.gif')
        message = await ctx.send(embed=embed)
        embed=discord.Embed(color=(color))
        embed.set_image(url='https://media.discordapp.net/attachments/819023119649079328/840781166462500864/rules-banner.png')
        message = await ctx.send(embed=embed)
        embed=discord.Embed(title='Rules', description="**1.** Channels \n > Please use the designated channels appropriately.\n \n **2.** NSFW content \n > NSFW will be prohibited outside of the NSFW channel. \n \n **3.** Spamming, raids etc. \n > No spam, ear rape or mic spam inside text and voice channels will be premitted. \n \n **4.** Terms Of Service \n > Do not violate the discord ToS (https://discord.com/terms) or the server rules. Otherwise, this will result in a punishment. \n \n **5.** Race, religion, politics, etc. \n > These topics shall not be discussed in this server. \n \n **6.** Profiles \n > Do not: \n > -Have an unpingable name / nickname \n > -Have a profile picture with NSFW content", color=(color))
        embed.set_footer(text=(description))
        embed.set_thumbnail(url=(thumbnail))
        message = await ctx.send(embed=embed)
        vokselid = '<@421506951269056522>'
        embed=discord.Embed(title="{}".format(ctx.message.author.mention()), color=(color))
        message = await ctx.send(embed=embed)
        await ctx.message.delete()


"""ADNIM COMMANDS"""
@bot.command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount=5):
    global confirmPurgeMessage
    global messagesToPurge
    global channelToPurge
    global purgeCTXMSG
    purgeCTXMSG = ctx.message
    channelToPurge = ctx.message.channel
    messagesToPurge = []
    async for message in channelToPurge.history(limit=amount + 1):
        messagesToPurge.append(message)
    embed=discord.Embed(title='Are you sure?', description=f"{ctx.author.mention}, You are about to purge {amount} messages!" ,color=color)
    embed.set_footer(text=description)
    embed.set_thumbnail(url=thumbnail)
    confirmPurgeMessage = await ctx.reply(embed=embed, mention_author=True)
    emojis = ['<:null_Y:849071815825162250>', '<:null_N:849071797671952394>']
    for emoji in emojis:
        await confirmPurgeMessage.add_reaction(emoji)
@purge.error
async def purge_error(ctx, amount=5):
    embed=discord.Embed(title='Purge error', description=f"{ctx.author.mention}, you do not have the necessary permissions to use this command!" ,color=color)
    embed.set_footer(text=description)
    embed.set_thumbnail(url=thumbnail)
    message = await ctx.reply(embed=embed, mention_author=True)
    time.sleep(5)
    await message.delete()
    await ctx.message.delete()
@bot.event
async def on_reaction_add(reaction, user):
    if user.id == bot.user.id:
        return
    else:
        if reaction.message.id == confirmPurgeMessage.id:
            if str(reaction) == '<:null_Y:849071815825162250>':
                await channelToPurge.delete_messages(messagesToPurge)
                await confirmPurgeMessage.delete()
            elif str(reaction) == '<:null_N:849071797671952394>':
                await confirmPurgeMessage.delete()
                await purgeCTXMSG.delete()

"""ON ERROR"""
@bot.event
async def on_command_error(ctx, error):
    print(f"{str(error)}")
    if str(error)[-9:] == 'not found': #'<:__:842869170990874646>'
        emojis = ['<:N_:842869093275271199>', '<:O_:842869124178509854>', '<:T_:842869147150450748>', '<:F_:842869215283511337>', '<:O2:842869245070409771>', '<:U_:842869292156583966>', '<:N2:842869322833199164>', '<:D_:842869349517361223>']
        for emoji in emojis:
            await ctx.message.add_reaction(emoji)
    else:
        embed=discord.Embed(title='An error occurred!', color=(color), description=f"{str(error)} \n Please report this to VOKSEL#3331")
        embed.set_footer(text=(description))
        if len(str(error)) >= 50:
            embed.set_thumbnail(url=thumbnail_small)
        else:
            embed.set_thumbnail(url=thumbnail)
        message = await ctx.reply(embed=embed, mention_author=True)

"""Embed template
embed=discord.Embed(title='Title Text', color=color)
embed.set_image(url='https://image-url')
embed.set_footer(text=description)
embed.set_thumbnail(url=thumbnail)
message = await ctx.reply(embed=embed, mention_author=True)"""

bot.add_cog(Music(bot))
bot.run(bot_token)
