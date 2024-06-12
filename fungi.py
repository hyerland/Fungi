import discord
import json
import logging
from discord.ext import commands
from rich import print
from rich.console import Console
from rich.logging import RichHandler

# * Load configuration
with open('fungi.json') as f:
    config = json.load(f)

#* Set up logging
# FORMAT = "[orange]Fungi Runtime[/orange] - %(message)s"
# formatter = logging.Formatter(FORMAT)

log = logging.getLogger("fungi")
log.addHandler(RichHandler(markup = True, console = Console()))

    

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix="!", intents=intents)

@client.event
async def on_ready():
    print(f'[green][{client.user}][/green] Logged in successfully! :star:')

@client.command()
async def test(ctx):
    await ctx.send('test')
    log.debug(f"{ctx.author} ran the `test` command")

def logLevel() -> int:
    if config['settings']['runtime_logs']:
        log.debug("Runtime logs enabled")
        return logging.DEBUG
    else:
        return logging.INFO

if __name__ == '__main__':
    client.run(config['token'], log_handler=RichHandler(markup = True, console = Console()), log_level = logLevel())