import discord
from discord.ext import commands


class Example(commands.Cog):

    def __init__(self, client):
        self.client = client

    #Commands
    @commands.command()
    async def c_helloworld(self, ctx): #C Hello World 출력
        await ctx.send('```c\n#include <stdio.h>\n\nint main()\n{\n    printf("Hello, World!");\n\n    return 0;\n}```')

    @commands.command()
    async def cpp_helloworld(self, ctx): #C++ Hello World 출력
        await ctx.send('```c++\n#include <iostream>\n\nint main()\n{\n    std::cout << "Hello, World!";\n\n    return 0;\n}```')

    @commands.command()
    async def csharp_helloworld(self, ctx): #C샵 Hello World 출력
        await ctx.send('```cpp\nusing System;\nusing System.Collections.Generic;\nusing System.Linq;\nusing System.Text;\nusing System.Threading.Tasks;\n\nnamespace ConsoleApp1\n{\n    class Program\n    {\n    static void Main(string[] args)\n    {\n        Console.WriteLine("Hello, World!");\n        Console.ReadLine();\n    }\n    }\n}```')

    @commands.command()
    async def clear(self, ctx, amount=1000): #채팅 메시지 삭제 *1000개
        await ctx.channel.purge(limit=amount)
        await ctx.send("**채팅 내역이 정리되었습니다.**")

    @commands.command()
    async def kick(self, ctx, member : discord.Member, *, reason=None): #유저 강퇴
        await member.kick(reason=reason)

    @commands.command()
    async def ban(self, ctx, member : discord.Member, *, reason=None): #유저 밴
        await member.ban(reason=reason)
        await ctx.send(f'{member.mention}님이 서버에서 영구추방되었습니다.')
        print(f'- {member.mention}님이 서버에서 영구추방되었습니다.')


def setup(client):
    client.add_cog(Example(client))