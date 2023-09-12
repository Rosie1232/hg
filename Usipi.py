import discord
import random
import os
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
    await ctx.send('"/" sembolünü -havalı(herhangi bir isim), merhaba, Usipi ve yardım- kelimelerinin başında yazarak sana cevap vermemi sağlayabilirsin.')
    await ctx.send('Örnek kullanımlar;')
    await ctx.send('/Usipi')
    await ctx.send('/merhaba')
    await ctx.send('/görüşürüz')
    await ctx.send('/havalı Usipi')
    await ctx.send('bu şekilde. İyi eğlenceler.\U0001f642')
    time.sleep(2)
    await ctx.send('(Yinede yeterli değil mi? "acelya.1"e doğrudan yazarak fikirlerini söyleyebilirsin. Böylece daha eğlenceli olurum belki. :))')


@bot.command()
async def Usipi(ctx):
    await ctx.send(f'Efendim {ctx.author}cım?')

@bot.command()
async def görüşürüz(ctx):
    await ctx.send(f'Sonra görüşürüz {ctx.author}!')

@bot.command()
async def merhaba(ctx):
    await ctx.send(f'Merhaba! {ctx.author}')

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.group()
async def oyun(ctx):
    await ctx.send('Ne oynamak istersin?')
    await ctx.send('Eğer tahmin oyununu oynamak istiyorsan hangi zorlukta (kolay/orta/zor) oynamak istediğini belirtmeyi unutma!')

@oyun.command()
async def tahmin(ctx, kolay, orta, zor, sayi, anahtar):
    if len(ctx.content) > 8:
        if ctx.content > kolay:
            sayi = random.randint(0, 11)
            await ctx.send('0 ile 10 arasından bir sayı seçtim.')
            await ctx.send('Bulabilmek ve bu kilidi açabilmek için üç hakkın var.\U0001f512')
        else:
            await ctx.send('Üzgünüm. Maalesef anlayamadım.\U0001f610')
@oyun.command()
async def sayi(ctx, sayi, anahtar):
    for i in range(3):
        if sayi == ctx.content:
            await ctx.send('Harika! Seçtiğim sayıyı bulabildin ve bir anahtar kazandın!\U0001f511')
            anahtar += 1
        else:
            await ctx.send('Yanlış!\U0001f512')
    if anahtar == 0:
        await ctx.send('Malesef bulamadın. Belki de en baştan başlayıp tekrar deneyebilirsin!\U0001f510')
@bot.group()
async def havalı(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'Hayır, {ctx.subcommand_passed} havalı değil.')

#bot.command()
#async def nasılsın(ctx, emojiler):
#    emojiler = ["\N{crying face}", "\N{smiling face}", "\N{grinning face}", "\N{sad face}", ]
#    durum = random.choices(emojiler)
#    await ctx.send(durum)



@havalı.command(name='acelya')
async def _acelya(ctx):
    """Is the bot cool?"""
    await ctx.send('Evet, Açelya çok havalı.') 

@havalı.command(name='Usipi')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Evet, ben çok havalıyım.')



@bot.command()
async def mem(ctx):
    resim = random.choice(os.listdir('python\images'))

    with open(f'python\images\{resim}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        resim = discord.File(f)
    await ctx.send(file=resim)

bot.run("")
