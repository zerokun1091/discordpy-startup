from discord.ext import commands
import os
import traceback

client = commands.Bot(command_prefix='.')
token = os.environ['DISCORD_BOT_TOKEN']


@client.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@client.event
async def on_ready():
    print ("Starting up")
activity = discord.Activity(name='python', type=discord.ActivityType.watching)
await client.change_presence(activity=activity)

@client.command()
async def ping(ctx):
    await ctx.send('pong')


client.run(token)
