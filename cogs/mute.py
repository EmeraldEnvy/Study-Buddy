from discord.ext import commands
import discord

class Mute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def hideText(self, context):
        guild = context.guild
        roles = guild.roles
        perms = discord.Permissions(send_messages = False)
        try:
            for i in roles:
                permissions = discord.Permissions()
                permissions.update(send_messages = True)
                await i.edit(permissions = permissions)
        except discord.Forbidden("r","r"):
            await context.send("Nope")

    @commands.command()
    async def revealText(self, context):
        guild = context.guild
        roles = guild.roles
        for i in roles:
            await i.edit(read_messages = True)

    @commands.command()
    async def hideVoice(self, context):
        guild = context.guild
        channels = guild.voice_channels
        roles = guild.roles
        for i in channels:
            for j in roles:
                await i.set_permissions(j, read_messages = False)
        await context.send("Hid voice channels")

    @commands.command()
    async def revealVoice(self, context):
        guild = context.guild
        channels = guild.voice_channels
        roles = guild.roles
        for i in channels:
            for j in roles:
                await i.set_permissions(j, read_messages = True)
        await context.send("Revealed voice channels")


def setup(bot):
    bot.add_cog(Mute(bot))