import discord
import os
import traceback

token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.event
async def on_ready():
    print ("Starting up")
activity = discord.Activity(name='python', type=discord.ActivityType.watching)
await client.change_presence(activity=activity)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')


bot.run(token)
