import discord
import random
#from yazitura import yazi_tura
#from password import gen_pass
from discord.ext import commands
import time
# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def yardım(ctx):
    await ctx.send('"/" sembolünü -havalı(herhangi bir isim), merhaba, Usipi, kek ve yardım- kelimelerinin başında yazarak sana cevap vermemi sağlayabilirsin.')
    await ctx.send('Örnek kullanımlar;')
    await ctx.send('/Usipi')
    await ctx.send('/merhaba')
    await ctx.send('/görüşürüz')
    await ctx.send('/havalı Usipi')
    await ctx.send('/kek (mutfak...)')
    await ctx.send('bu şekilde. İyi eğlenceler.\U0001f642')
    time.sleep(2)
    await ctx.send('(Yinede yeterli değil mi? "acelya.1"e doğrudan yazarak fikirlerini söyleyebilirsin. Böylece daha eğlenceli olurum belki. :))')


@bot.command()
async def Usipi(ctx):
    await ctx.send(f'Efendim {ctx.author}cım?')

@bot.command()
async def görüşürüz(ctx):
    await ctx.send(f'Sonra görüşürüz {ctx.author} \U0001f642!')

@bot.command()
async def merhaba(ctx):
    await ctx.send(f'Merhaba! {ctx.author}')

@bot.command()
async def joined(ctx, member: discord.Member):
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.group()
async def havalı(ctx):.
    if ctx.invoked_subcommand is None:
        await ctx.send(f'Hayır, {ctx.subcommand_passed} havalı değil.')


@havalı.command(name='acelya')
async def _acelya(ctx):
    await ctx.send('Evet, Açelya çok havalı.') 

@havalı.command(name='Usipi')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Evet, ben çok havalıyım.')

@bot.group()
async def kek(ctx):
    await ctx.send('Kek yapmak için ilk önce malzemeleri bulmalısın. Hangi odaya gitmek istersin?')

@kek.command()
async def mutfak(ctx):
        await ctx.send('Harika! Malzemeleri buldun. Tamam kolaydı evet. Peki kekini neyli yapmak istersin?')

bot.run("")
