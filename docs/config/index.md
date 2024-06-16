# Configuration 🔨

Fungi provides an extensive configuration file to change the bot's behavior. When running the bot for the first time,
a **first time setup** is launched to create the configuration file needed to run the bot.

An example of the configuration file is shown below:

```json
{
    "bot": {
        "token": "XXXXXXX",
        "name": "Fungi",
        "prefix": "!"
    },
    "settings": {
        "runtime_logs": true
    },
    "commands": {
        "ban": {
            "enabled": true,
            "help": "Bans mentioned user.",
            "require_reason": true
        },
        "roll": {
            "enabled": true,
            "help": "Rolls a random number between 1-10 by default.",
            "number": 20
        }
    },
    "other": {
        "disable_fungi_watermark": false
    }
}


```
