import discord
import os
import traceback

token = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()

@client.event
async def on_ready():
    print('ログインしました')
    activity = discord.Activity(name='discord.py', type=discord.ActivityType.watching)
    await client.change_presence(activity=activity)


@client.event
async def on_message(message):
    if message.author.bot:
        return
 
    if message.content == 'ねこ':
        await message.channel.send('にゃーん')

    if message.content == '.roles':
        await message.channel.send(message.guild.roles)

    if message.content == '.embedt':
        embed = discord.Embed(title="Hi!!",description="How are you?") 
        await channel.send(embed=embed) 

client.run(token)
