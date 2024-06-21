# Getting started with Fungi 🍄

:::tip Wait... where's the discord bot invite?
As of **June 13, 2024,** Fungi has **NO OFFICIAL DISCORD BOT INVITE** as one of the main reasons for the bot's existence being having the
ability to be self hosted by anyone and anywhere.
:::

> *Requires Python 3.8 or greater for installation.*

Fungi can easily be installed from **PyPi** by running:

```bash
pip install fungi-bot
```

This would install the **latest stable** version of Fungi to your python installation.

:::details Update Fungi to the latest version

To update Fungi to a latest version released, run the following command:

```bash
pip install fungi-bot --upgrade
```

:::

## Using Fungi

Using fungi can be done by doing the following within a terminal.

```bash
fungi start
```

> If you already have an application and token, you can skip this step.

### Creating an application

In order to continue, head to [discord.com/developers](https://discord.com/developers/) to create an application.

- After creating an application, go to the "Bot" tab and generate and copy the token.
  - Never post or share your token with anyone. It's a major security risk and could let to your account getting hacked by bad actors.
  
- Here is where you can customize the profile of the bot which isn't required but makes your bot nice to use.

:::warning
**Fungi** or **Fungi Framework** doesn't store any information about your application in servers, fungi only works on your local machine with your configuration.
:::

This will start the FTS *(First Time Setup)* of the Fungi Framework with only asking vital information such as, **token, name, prefix, and to have debug mode enabled**

By default, Fungi will store the configuration with the current working directory for instance, if you run `fungi start` in `C:/Users/Example/Documents` and the configuration will be stored in `C:/Users/Example/Documents/fungi.json` for later use and reference.

Once your configuration file is created, the bot will automatically start after FTS and will be ready to use. *See the [Configuration](../config/) guide for more information.*
