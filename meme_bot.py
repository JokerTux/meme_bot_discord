import discord
from random import randrange
from os import listdir, path

bot_token = '<Bot token here>'
bot = discord.Bot()

### Optional: add your server to the "servers" list
#servers = [<Your server ID. nr >]
servers = None

def file_path():
	dir_path = path.dirname(path.realpath(__file__))
	return dir_path


@bot.event
async def on_ready():
	print('Ready ! Bot is working...')


@bot.event
async def on_member_join(ctx):
	await channel.send(f'Hello {ctx.author.display_name}, its nice to see you. How are you today ?')


@bot.slash_command(guild_ids=servers, name='hello')
async def message(ctx):
	await ctx.respond(f'Hello {ctx.author.display_name}, type /meme to see a meme')


### For now, all images should be in a ".jpg" format and increment the file name (if the last file in the memes folder is called "4.jpg" just increment the name by 1 and edit it, to for example "5.jpg" )
@bot.slash_command(guild_ids=servers, name='meme')
async def meme(ctx):
	dir_path = file_path()
	files_in_dir = listdir(f'{dir_path}/memes/')
	count_memes = len(files_in_dir)
	file_nr = randrange(count_memes)
	meme_name = f'{file_nr}.jpg'

	# Console print
	print(f'POSTED meme : {dir_path}/{meme_name}')

	await ctx.respond('your random meme : ', file=discord.File(f'{dir_path}/memes/{meme_name}'))

bot.run(bot_token)
