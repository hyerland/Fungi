# Configuration 🔨

Fungi provides an extensive configuration file to change the bot's behavior. When running the bot for the first time,
a **first time setup** is launched to create the configuration file needed to run the bot.

An example of the configuration file is shown below:

```json
{
    "token": "XXXXXXX",
    "bot": {
        "name": "Example",
        "prefix": "!"
    },
    "settings": {
        "runtime_logs": false
    },
    "commands": {
        "ban": {
            "enabled": true,
            "help": "Bans mentioned user.",
            "require_reason": true
        }
    },
    "other": {
        "disable_fungi_watermark": false
    }
}

```

:::warning
As of **v0.1.0** or greater, all commands are required to be included whatever you have `enabled` to true or false.
:::
