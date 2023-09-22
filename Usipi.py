import discord
import random
import os
#from yazitura import yazi_tura
#from password import gen_pass
from discord.ext import commands
import time
import emoji
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

@bot.command()
async def oyun(ctx, tahmin):
    await ctx.send('Ne oynamak istersin?')
    await ctx.send('Eğer tahmin oyununu oynamak istiyorsan hangi zorlukta (kolay/orta/zor) oynamak istediğini belirtmeyi unutma!')

@bot.command()
async def tahmin(ctx):
    await ctx.send('Kolay mı orta mı zor mu?')
    @bot.command()
    async def kolay(ctx, sayi):
        sayi = random.randint(0, 11)
        await ctx.send('0 ile 10 arasından bir sayı seçtim.')
        await ctx.send('Bulabilmek ve bu kilidi açabilmek için üç hakkın var.\U0001f512')
        @kolay.command()
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

bot.command()
async def nasilsin(ctx):
    emojiler = ["\U0001f62D", "\U0001f601", "\U0001f610", '\U0001f622', "\U0001f922", "\U0001f621", "\U0001f60C", "\U0001f62A", "\U0001fAE5", "\U0001f92A", "\U0001F973"]
    durum = random.choices(emojiler)
    if durum == "\U0001f62D":
        await ctx.send(durum)
        await ctx.send("Çok üzgünüüüm!!!")
    if durum == "\U0001f601":
        await ctx.send(durum)
        await ctx.send("Çok mutluyum!!")
    if durum == "\U0001f610":
        await ctx.send(durum)
        await ctx.send("...")
    if durum == "\U0001f622":
        await ctx.send(durum)
        await ctx.send("Hiç moralim yok.")
    if durum == "\U0001f922":
        await ctx.send(durum)
        await ctx.send("Çok köt...")
    if durum == "\U0001f621":
        await ctx.send(durum)
        await ctx.send("Çok kızgınım!!")
    if durum == "\U0001f60C":
        await ctx.send(durum)
        await ctx.send("Çok sakinim.")
    if durum == "\U0001fAE5":
        await ctx.send(durum)
        await ctx.send("Ben aslında yoğum!")
    if durum == "\U0001f92A":
        await ctx.send(durum)
        await ctx.send("Çok iyiyim gerçekten!")
    if durum == "\U0001f62A":
        await ctx.send(durum)
        await ctx.send("Çok uykum var!")
    if durum == "\U0001F973":
        await ctx.send(durum)
        await ctx.send("Hadi parti verelim!")



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
