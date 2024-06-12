"""
The layer between you, as the user, and the bot. Used for managing the bot.
"""
import typer
import subprocess
import logging
import os
import json
from rich import print, print_json
from rich.logging import RichHandler
from rich.prompt import Prompt, Confirm
from typing_extensions import Annotated

#* Set up logging
#FORMAT = "[blue]Fungi CLI[/blue] - %(message)s"
#logging.basicConfig(
#    level="ERROR", format=FORMAT, datefmt="[%X]", handlers=[RichHandler(markup=True)]
#)

#log = logging.getLogger("rich")


#* Set up CLI application
app = typer.Typer(add_completion=False)

#? Metadata
version = "0.1.0"

@app.callback()
def callback(verbose: Annotated[bool, typer.Option("--verbose", "-v")] = False):
    """
    Provides the bot with information needed to run for individual hosting. 
    """
    if verbose:
        print('y')
        #log.setLevel("DEBUG")
        #log.debug("Verbose mode enabled")

    print(f"Starting [red]Fungi [b]v{version}[/b][/red] framework...")
    config_file = 'fungi.json'

    #log.debug("Checking if config file exists...")
    if not os.path.isfile(config_file):
        #log.debug("Config file does not exist, prompting first time setup...")

        print("Starting first time setup...")

        token = Prompt.ask("\n[dim](https://discord.com/developers)[/dim]\nEnter your discord bot token", password=True)
        prefix = Prompt.ask("What prefix would you like to use? (!ping or $ping)")

        temp = {
                "token": token,
                "bot": {
                    "prefix": prefix
                }
            }

        print_json(data=temp, indent=4)

        confirm = Confirm.ask("Generate configuration?", default=True)   
        if confirm:
            with open(config_file, 'w') as f:
                json.dump(temp, f, indent=4)
                f.write('\n')
        else:
            print("Exiting...")
            exit(1)

        print("[green]First time setup complete! :rocket:")

@app.command()
def start():
    #log.info("Starting bot services...")
    subprocess.run(["python", "-m", "fungi"], shell=True)


if __name__ == "__main__":
    app()