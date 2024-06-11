"""
The layer between you, as the user, and the bot. Used for managing the bot.
"""
import typer
import subprocess

app = typer.Typer(add_completion=False)


@app.callback()
def callback():
    """
    Provides the bot with information needed to run for individual hosting. 
    """


@app.command()
def start():
    subprocess.run(["python", "-m", "fungi"], shell=True)


if __name__ == "__main__":
    app()