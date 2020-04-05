import discord
import os
import traceback
import datetime

token = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()

@client.event
async def on_ready():
    print('ログインしました')
    activity = discord.Activity(name='discord.py', type=discord.ActivityType.watching)
    await client.change_presence(activity=activity)
    channel = client.get_channel(678913915123662907)
    embed = discord.Embed(title="Botが起動しました")
    dt_now = datetime.datetime.now()
    embed.set_footer(dt_now)
    await channel.send(embed=embed) 


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
        await message.channel.send(embed=embed) 

client.run(token)
