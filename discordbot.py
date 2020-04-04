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
 
    if message.content == '/neko':
        await message.channel.send('にゃーん')


client.run(token)
