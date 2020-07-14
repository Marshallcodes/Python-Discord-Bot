import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix = '!')

#Cogs Start
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
#Cogs End



#Events
@client.event
async def on_ready(): #봇 동작 여부
    await client.change_presence(activity = discord.Streaming(name = "\n", url = "https://www.twitch.tv/search?term=Hello%20There")) #커스텀 status
    print('Bot is online! :D')

@client.event
async def on_member_join(member): #서버 접속 콘솔 출력
    print(f'- {member}님이 서버에 접속하였습니다.')

@client.event
async def on_member_remove(member): #서버 퇴장 콘솔 출력
    print(f'- {member}님이 서버에서 퇴장하였습니다.')


#Commands
@client.command()
async def ping(ctx): #자신의 ping 출력
    await ctx.send(f'**🎆 {round(client.latency * 1000)}ms**입니다.')

@client.command()
async def unban(ctx, *, member): #밴 해제
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if(user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            print(f'{user}님의 밴이 해제되었습니다.')
            return


client.run('paste your token here')