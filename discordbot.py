from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

async def on_ready():
    print ("Starting up")
    print ("My username is " + bot.user.name + " and i am running with the ID: " + bot.user.id)
    await bot.change_presence(game=discord.Game(name="Test", type=1))
    print ("Started")


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


bot.run(token)
