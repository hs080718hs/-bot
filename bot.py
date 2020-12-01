import discord
import requests
import string
import random
import time
from captcha.image import ImageCaptcha
import asyncio
import os

client = discord.Client()

@client.event
async def on_ready():
    print("봇이 성공적으로 실행되었습니다.")
    game = discord.Game('문이는 열일중 !!')
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith('!청소'):
        try:
            # 메시지 관리 권한 있을시 사용가능
            if message.author.guild_permissions.manage_messages:
                amount = message.content[4:]
                await message.delete()
                await message.channel.purge(limit=int(amount))
                message = await message.channel.send(embed=discord.Embed(title='🧹 메시지 ' + str(amount) + '개 삭제됨', colour=discord.Colour.green()))
                await asyncio.sleep(2)
                await message.delete()
            else:
                await message.channel.send('``명령어 사용권한이 없습니다.``')
        except:
            pass

@client.event
async def on_message(message):
    if message.content.startswith("/출근"):
        try:
            # 메시지 관리 권한 있을시 사용가능
            if message.author.guild_permissions.manage_messages:
                author = message.guild.get_member(int(message.author.id))
                embed = discord.Embed(color=0x80E12A)
                channel = 783220292101079052
                embed.set_author(name=author, icon_url=message.author.avatar_url)
                embed.add_field(name='관리자 출근 알림', value='모든문의 주세요!')
                embed.set_image(url="https://cdn.discordapp.com/attachments/782162902014099487/783214977187315712/5f51a3497758d2e6.png")
                await client.get_channel(int(channel)).send(embed=embed)
        except:
            pass

    if message.content.startswith("/퇴근"):
        try:
            if message.author.guild_permissions.manage_messages:
                author = message.guild.get_member(int(message.author.id))
                embed = discord.Embed(color=0xFF0000)
                channel = 783220320668483604
                embed.set_author(name=author, icon_url=message.author.avatar_url)
                embed.add_field(name='관리자 퇴근 알림', value='문의들 못받습니다.')
                embed.set_image(url="https://cdn.discordapp.com/attachments/782162902014099487/783214977187315712/5f51a3497758d2e6.png")
                await client.get_channel(int(channel)).send(embed=embed)
        except:
            pass

@client.event
async def on_ready():
    print("봇이 성공적으로 실행되었습니다.")
    game = discord.Game('문이는 열일중 !!')
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith("!색깔"):
        await message.channel.send('`빨강` `주황` `노랑` `초록` `파랑` `보라` `분홍` `검정` `민트` `하늘` `갈색` `회색` `남색`')

    if message.content.startswith("!임베드"):
        if message.content[5:7] == '빨강':
            selcolor = 0xFF0000
        if message.content[5:7] == '주황':
            selcolor = 0xFF8C00
        if message.content[5:7] == '노랑':
            selcolor = 0xFFDC37
        if message.content[5:7] == '초록':
            selcolor = 0x00FC08
        if message.content[5:7] == '파랑':
            selcolor = 0x006AFF
        if message.content[5:7] == '보라':
            selcolor = 0x9932CC
        if message.content[5:7] == '분홍':
            selcolor = 0xFF00FF
        if message.content[5:7] == '검정':
            selcolor = 0x000000
        if message.content[5:7] == '민트':
            selcolor = 0x00FFDD
        if message.content[5:7] == '하늘':
            selcolor = 0x3CFBFF
        if message.content[5:7] == '갈색':
            selcolor = 0x8B4F1D
        if message.content[5:7] == '회색':
            selcolor = 0x828282
        if message.content[5:7] == '남색':
            selcolor = 0x3700FF

        value = message.content[8:]
        embed = discord.Embed(color=selcolor)
        embed.add_field(name="\u200b", value=value, inline=False)
        embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)

        await message.channel.send(embed=embed)
        await message.delete()

@client.event
async def on_ready():
    print("인증 봇이 정상적으로 실행되었습니다.")
    game = discord.Game('문이는 열일중 !!')
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("달빛아 인증"): #명령어 달빛아 인증
        a = ""
        Captcha_img = ImageCaptcha()
        for i in range(6):
            a += str(random.randint(0, 9))

        name = str(message.author.id) + ".png"
        Captcha_img.write(a, name)

        await message.channel.send(f"""{message.author.mention} 아래 숫자를 10초 내에 입력해주세요. """)
        await message.channel.send(file=discord.File(name))

        def check(msg):
            return msg.author == message.author and msg.channel == message.channel

        try:
            msg = await client.wait_for("message", timeout=10, check=check) # 제한시간 10초
        except:
            await message.channel.purge(limit=3)
            chrhkEmbed = discord.Embed(title='❌ 인증실패', color=0xFF0000)
            chrhkEmbed.add_field(name='닉네임', value=message.author, inline=False)
            chrhkEmbed.add_field(name='이유', value='시간초과', inline=False)
            await message.channel.send(embed=chrhkEmbed)
            print(f'{message.author} 님이 시간초과로 인해 인증을 실패함.')
            return

        if msg.content == a:
            role = discord.utils.get(message.guild.roles, name="♦️손님♦️")
            await message.channel.purge(limit=4)
            tjdrhdEmbed = discord.Embed(title='인증성공', color=0x04FF00)
            tjdrhdEmbed.add_field(name='닉네임', value=message.author, inline=False)
            tjdrhdEmbed.add_field(name='5초후 인증역할이 부여됩니다.', value='** **', inline=False)
            tjdrhdEmbed.set_thumbnail(url=message.author.avatar_url)
            await message.channel.send(embed=tjdrhdEmbed)
            time.sleep(5)
            await message.author.add_roles(role)
        else:
            await message.channel.purge(limit=4)
            tlfvoEmbed = discord.Embed(title='❌ 인증실패', color=0xFF0000)
            tlfvoEmbed.add_field(name='닉네임', value=message.author, inline=False)
            tlfvoEmbed.add_field(name='이유', value='잘못된 숫자', inline=False)
            await message.channel.send(embed=tlfvoEmbed)
            print(f'{message.author} 님이 잘못된 숫자로 인해 인증을 실패함.')

@client.event
async def on_ready():
    print("봇이 성공적으로 실행되었습니다.")
    game = discord.Game('문이는 열일중 !!')
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith('달빛아 니트로'):
        ranNitro = ""
        for i in range(0, 16):
            ranNitro += str(random.choice(string.ascii_letters))
            NitroEmbed = discord.Embed(title='💵니트로 생성기', description='https://discord.gift/' + ranNitro)
        await message.channel.send(embed=NitroEmbed)

@client.event
async def on_ready():
    print("봇이 성공적으로 실행되었습니다.")
    game = discord.Game('문이는 열일중 !!')
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith('!문상') or message.content.startswith('달빛아 문상'):
        a = random.randint(2100, 3800)
        b = random.randint(1000, 9999)
        b2 = random.randint(1000, 9999)
        c = random.randint(100000,999999)
        TICKETembed = discord.Embed(title='문상 생성기', description=str(a) + '-' + str(b) + '-' + str(b2) + '-' + str(c))
        await message.channel.send(embed=TICKETembed)

@client.event
async def on_ready():
    print("봇이 성공적으로 실행되었습니다.")
    game = discord.Game('문이는 열일중 !!')
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith('달빛아 실검'):
        json = requests.get('https://www.naver.com/srchrank?frm=main').json()
        ranks = json.get("data")
        data = []
        for r in ranks:
            rank = r.get("rank")
            keyword = r.get("keyword")
            if rank > 10:
                break
            data.append(f'**{rank}**위 {keyword}')

        dat = str(data)
        dat = dat.replace("'","")
        dat = dat.replace(", ","\n")
        dat = dat[1:-1]
        print(dat)
        embed = discord.Embed(title= '네이버 실시간 검색어 순위', description=(dat),colour=0x19CE60)
        await message.channel.send(embed=embed)

client.run(os.environ['token'])
