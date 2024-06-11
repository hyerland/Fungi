"""
Discord bot for hosting self-hosted servers.
"""
import discord
from rich import print

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'[green][{client.user}][/green] Logged in successfully! :star:')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

if __name__ == '__main__':
    client.run('Hidden')