import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename = 'discord.log', encoding='utf-8', mode = 'w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix = '!', intents = intents)

secret_role = "Gamer"

#Checking to see the bot is running
@bot.event
async def on_ready():
    print(f"We are ready to go in, {bot.user.name}")  

#Welcome to server when a member joins
@bot.event
async def on_member_join(member):
    await member.send(f"Welcome to the server {member.name}")

#Deletes a message if it contains a certain word
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if "shit" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention} no cussing!")

    await bot.process_commands(message)

@bot.command()
#ctx means context
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.mention}!")

#Assigns role
@bot.command()
async def assign(ctx):
    role = discord.utils.get(ctx.guild.roles, name = secret_role)
    if role:
        await ctx.author.add_roles(role)
        await ctx.send(f"{ctx.author.mention} has been given the role {secret_role}!")
    else:
        await ctx.send("This role does not exist.")

#Removes role
@bot.command()
async def remove(ctx):
    role = discord.utils.get(ctx.guild.roles, name = secret_role)
    if role:
        await ctx.author.remove_roles(role)
        await ctx.send(f"{ctx.author.mention} has had the role {secret_role} removed.")
    else:
        await ctx.send("This role does not exist.")

#Prints message if has secret_role(gamer)
@bot.command()
@commands.has_role(secret_role)
async def secret(ctx):
    await ctx.send("Welcome to the club!")

#Prints error if you don't have that role
@secret.error
async def secret_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send("You do not have permission to do that.")

#DMs you the message you sent.
@bot.command()
async def dm(ctx, *, msg):
    await ctx.author.send(f"You said {msg}")

@bot.command()
async def reply(ctx):
    await ctx.reply("This is a reply to your message!")

@bot.command()
async def poll(ctx, *, question):
    embed = discord.Embed(title = "New Poll", description = question)
    poll_message = await ctx.send(embed = embed)
    await poll_message.add_reaction("👍")
    await poll_message.add_reaction("👎")


bot.run(token, log_handler = handler, log_level = logging.DEBUG)