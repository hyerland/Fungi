# `commands` <Badge type="tip" text="^0.1.0" />

:::warning
As of <Badge type="tip" text="0.1.0" /> and greater until **Fungi Framework** gets an overhaul, commands will be required to be within `fungi.json`
for the bot to run. No matter if `enabled` tag is set to `true` or not.
:::

Used as configuration only set for commands in which fungi framework would take given user information about said commands and adjust the code to reflect said functionality.

:::tip About `help` and `ping` commands
Both commands are considered vital to the framework and are required thus not allowing configuration to disable them nor customize them. `help` is the only semi-customizable command where information is pulled from configuration.
:::

## `help` <Badge type="tip" text="^0.1.0" /> <Badge type="warning" text="Semi-Customizable" />

Displays a list of all available commands and their descriptions pulled from `fungi.json`.

## `ping` <Badge type="tip" text="^0.1.0" /> <Badge type="danger" text="Not Customizable" />

Replies with pong and client latency. Useful for checking if the bot works.

## `ban` <Badge type="tip" text="^0.1.0" />

Bans mentioned user.

- `require_reason`: Whether the bot requires a reason to ban the user.

::: code-group

```json [Enabled - Default]
"ban": {
    "enabled": true,
    "help": "Bans mentioned user.",
    "require_reason": true
}
```

```json [Disabled]
"ban": {
    "enabled": false,
    "help": "Bans mentioned user.",
    "require_reason": true
}
```

:::

## `roll` <Badge type="tip" text="^0.1.0" />

Rolls a random number between 1-10 by default.

- `number`: Number to roll between. Rolls from 1 - `number` set by the configuration
  - Can be overridden by user when running the command

::: code-group

```json [Enabled - Default]
"roll": {
    "enabled": true,
    "help": "Rolls a random number between 1-10 by default.",
    "number": 10
}
```

```json [Disabled]
"roll": {
    "enabled": false,
    "help": "Rolls a random number between 1-10 by default.",
    "number": 10
}
```

:::
