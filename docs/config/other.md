# `other`

Used for settings in which are considered miscellaneous settings which don't have a specific place in the configuration file.

## `disable_fungi_watermark` <Badge type="tip" text="^0.1.0" />

:::tip
While you can disable the "Fungi Framework" watermark, the watermark is there to spread project awareness and helps keep the project alive and well supported.
The choice is ultimately yours but it would be great if you continued to raise awareness around the project. 💖
:::

Remove all "Fungi Framework" branding from the commands and messages.

::: code-group

```json [Enabled - Default]
"other": {
    "disable_fungi_watermark": true
}
```

```json [Disabled]
"other": {
    "disable_fungi_watermark": false
}
```

:::
