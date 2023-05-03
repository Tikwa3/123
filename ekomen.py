import discord
from discord.ext import commands
import os, random
import requests
# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я эко-мэн. я знаю команды: $mem - по которой можно посмотреть мемчик))), $duck - по котрой вы увидите милую уточку), $plastik - по которой вы увидите картинки :как сортировать пластик: $stecklo - по которой вы увидите картинки :как сортировать стекло:')

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''По команде duck вызывает функцию get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)


@bot.command('mem')
async def mem(ctx):
    img = random.choice(os.listdir("images"))
    with open(f'images/{img}', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)

@bot.command('plastik')
async def plastik(ctx):
    img = random.choice(os.listdir("plastik"))
    with open(f'plastik/{img}', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)

@bot.command('stecklo')
async def stecklo(ctx):
    img = random.choice(os.listdir("stecklo"))
    with open(f'stecklo/{img}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


bot.run("")

