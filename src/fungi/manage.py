"""
The layer between you, as the user, and the bot. Used for managing the bot.
"""
import typer
import subprocess
import os
import json
from rich import print, print_json
from rich.prompt import Prompt, Confirm
from typing_extensions import Annotated

#* Set up CLI application
app = typer.Typer(add_completion=False)

#? Metadata
version = "0.1.0"

@app.callback()
def callback():
    """
    Provides the bot with information needed to run for individual hosting. 
    """

    print(f"Starting [red]Fungi [b]v{version}[/b][/red] framework...")
    config_file = 'fungi.json'

    if not os.path.isfile(config_file):
        print("Starting first time setup...")

        name = Prompt.ask("What would you like to name your bot?")
        token = Prompt.ask("\n[dim](https://discord.com/developers)[/dim]\nEnter your discord bot token", password=True)
        prefix = Prompt.ask("What prefix would you like to use? (!ping or $ping)")
            
        debug = Confirm.ask("Would you like to enable debug mode?", default=True)

        # temp = config
        temp = {
                "token": token,
                "bot": {
                    "name": name,
                    "prefix": prefix
                },
                "settings": {
                    "runtime_logs": debug
                },
                "commands": {
                    "ban": {
                        "enabled": True,
                        "help": "Bans mentioned user.",
                        "require_reason": True
                    }
                },
                "other": {
                    "disable_fungi_watermark": False
                }
                }

        shorthand_temp = {
            "token": token,
            "name": name,
            "prefix": prefix,
            "debug?": debug
        }

        print_json(data=shorthand_temp, indent=4)

        confirm = Confirm.ask("Generate configuration?", default=True)   
        if confirm:
            with open(config_file, 'w') as f:
                json.dump(temp, f, indent=4)
                f.write('\n')
        else:
            print("Exiting...")
            exit(1)

        print("[green]First time setup complete! :rocket:\nVisit https://fungibot.netlify.app/ for more info on configuration.")

@app.command()
def start():
    subprocess.run(["python", "-m", "fungi.fungi"], shell=True)


if __name__ == "__main__":
    app()