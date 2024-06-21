import discord
import json
import random
import asyncio
import logging
from datetime import datetime
from discord.ext import commands
from rich import print
from rich.console import Console
from rich.logging import RichHandler

#TODO: Rewrite or overhaul codebase to not require commands to be within `fungi.json`

#? Metadata
version = "0.1.1"

#* Load configuration
with open('fungi.json') as f:
    config = json.load(f)


#* Set up logging
# FORMAT = "[orange]Fungi Runtime[/orange] - %(message)s"
# formatter = logging.Formatter(FORMAT)

log = logging.getLogger("fungi")
log.addHandler(RichHandler(markup = True, console = Console()))

#* Set up intents
intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix=config['bot']['prefix'], intents=intents)
client.remove_command('help')

@client.event
async def on_ready():
    print(f'[green][{client.user}][/green] Logged in successfully! :star:')

@client.event
async def on_command_error(ctx, error):
        await ctx.send(f"An error occurred!\n> {error}")

@client.command(help="All available commands and their descriptions")
async def help(ctx):
    embed = discord.Embed(title=f"{config['bot']['name']} Commands", 
                          description=f"All available commands and their descriptions which can be used with the `{config['bot']['prefix']}` prefix.",
                          colour=0xa4aef5,
                          timestamp=datetime.now())
    for command in client.commands:
        embed.add_field(name=command.name, value=command.help, inline=True)

    if config['other']['disable_fungi_watermark']:
        embed.set_footer(text=f"(v{version})")
        # :(
    else:
        embed.set_footer(text=f"Fungi Framework (v{version}) | Instance serving {len(client.guilds)} Servers",
                 icon_url="https://cdn.discordapp.com/avatars/1249930441285177395/7e949ee8eea41f6c135dfc32907e499f.png?size=1024")
    await ctx.send(embed=embed)


@client.command(help="Find client latency.")
async def ping(ctx):
    await ctx.send(f"> Pong! {round(client.latency * 1000)}ms")
    log.info(f"{ctx.author} ran the `ping` command. Latency: {round(client.latency * 1000)}ms")

@client.command(help=config["commands"]["ban"]["help"])
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    if config["commands"]["ban"]["enabled"]:
        if config["commands"]["ban"]["require_reason"] and not reason:
            await ctx.send("Provide a reason. 🚫")
        else:
            try:
                await member.ban(reason=reason)
                await ctx.message.delete()
                await ctx.channel.send(f'{member.name} has been banned from server\n'
                                    f'> Reason: {reason}')
            except Exception:
                await ctx.channel.send(f"{config['bot']['name']} doesn't have enough permissions to ban someone." 
                                    "Upgrade the Permissions.")
            # except discord.ext.commands.errors.MissingRequiredArgument:
            #     await ctx.send("Please provide a member to ban. 🚫")
    else:
        await ctx.send("Provided configuration has disabled this command. 🚫")

@client.command(help=config["commands"]["roll"]["help"])
async def roll(ctx, number: int = config["commands"]["roll"]["number"]):
    if config["commands"]["roll"]["enabled"]:
       await ctx.send(f"{random.randint(1, number)}")
    else:
        await ctx.send("Provided configuration has disabled this command. 🚫")

@client.command(help=config["commands"]["purge"]["help"])
@commands.has_permissions(manage_messages=True)
async def purge(ctx, limit: int):
    if config["commands"]["purge"]["enabled"]:
        await ctx.message.delete()
        await asyncio.sleep(1)
        await ctx.channel.purge(limit=limit)
        purge_embed = discord.Embed(title='Purge [!purge]', 
                                    description=f'Successfully purged {limit} messages. \n Command executed by {ctx.author}.', 
                                    color=0xa4aef5)
        purge_embed.set_footer(text=str(datetime.now()))
        await ctx.channel.send(embed=purge_embed)
    else:
        await ctx.send("Provided configuration has disabled this command. 🚫")

def logLevel() -> int:
    if config['settings']['runtime_logs']:
        log.debug("Runtime logs enabled")
        return logging.DEBUG
    else:
        return logging.INFO

if __name__ == '__main__':
    client.run(config['bot']['token'], log_handler=RichHandler(markup = True, console = Console()), log_level = logLevel())
    