"""
The layer between you, as the user, and the bot. Used for managing the bot.
"""
import typer
import subprocess
import logging
from rich import print
from rich.logging import RichHandler

FORMAT = "[blue]Fungi CLI[/blue] - %(message)s"
logging.basicConfig(
    level="NOTSET", format=FORMAT, datefmt="[%X]", handlers=[RichHandler(markup=True)]
)

log = logging.getLogger("rich")
app = typer.Typer(add_completion=False)


@app.callback()
def callback():
    """
    Provides the bot with information needed to run for individual hosting. 
    """
    log.info("Starting fungi framework...")


@app.command()
def start():
    log.info("Starting bot services...")
    subprocess.run(["python", "-m", "fungi"], shell=True)


if __name__ == "__main__":
    app()