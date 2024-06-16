# `settings` <Badge type="tip" text="^0.1.0" />

Typically used to host bot wide settings in which provide extra information or features to the bot.

## `runtime_logs` <Badge type="tip" text="^0.1.0" /> <Badge type="info" text="FTS Field" />

Enable extra logs for the bot. Primarily used for debugging on developer environments to find root causes of bugs and issues.
Also displays error when the bot encounters an error in discord.

::: code-group

```json [Enabled]
"settings": {
    "runtime_logs": true
},
```

```json [Disabled]
"settings": {
    "runtime_logs": false
},
```

:::
