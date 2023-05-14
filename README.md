# Discord Bot - Backrooms Random Mover

This Discord bot is designed to randomly move users to a designated backrooms voice channel. The backrooms concept is inspired by internet horror stories where individuals find themselves trapped in an endless maze of indistinguishable rooms. The bot adds an element of surprise and suspense to your Discord server by occasionally transporting users to the backrooms.

## Features

- Randomly moves users from voice channels to the backrooms and remove every of his roles to create an uncomforable situation.
- Run a sound effect upon arrival in the backrooms.
- Restores the user's original roles and moves them back after a certain duration.

## Prerequisites

- Python 3.7 or higher
- FFmpeg (for playing sound files)
- [discord.py](https://discordpy.readthedocs.io/) library (`pip install discord.py`)
- [python-dotenv](https://pypi.org/project/python-dotenv/) library (`pip install python-dotenv`)

## Bot Setup

1. Clone or download the project files to your local machine.
2. Install the required libraries by running the following command:

   ```
   pip install -r requirements.txt
   ```

3. Create a new Discord bot and generate a token. You can follow the guide in the [Discord Developer Portal](https://discord.com/developers/applications).
4. Create a new file named `.env` in the project directory and add the following line, replacing `<YOUR_DISCORD_TOKEN>` with your Discord bot token:

   ```
   DISCORD_TOKEN=<YOUR_DISCORD_TOKEN>
   ```
**Note:** You can also customise the waiting time beetween each move by adding the following line in the `.env` file:
   
   ```
   MIN_WAIT_TIME = <TIME_MIN_BEFORE_A_MOVE_IN_MINUTES>
   MAX_WAIT_TIME = <TIME_MAX_BEFORE_A_MOVE_IN_MINUTES>
   ```
5. Make sure to have FFmpeg installed on your system. You can download it from the official [FFmpeg website](https://ffmpeg.org/).
6. Customize the bot's behavior by adjusting the code in the provided script if desired.

## Server Setup

1. Create a new voice channel named `floor 0` or `backrooms` in your Discord server.
2. You have to make the role `@everyone` unable to do anything on the server. You can do this by going to the server settings, then to the roles tab, and then to the `@everyone` role. Then, you have to uncheck all the permissions for this role. The goal of this is to make the user unable to leave the backrooms by himself when the bot removes all his roles.
3. Create a replacement for the `@everyone` role. This role have the same permissions as the previous `@everyone` role, but it can be removed during the backrooms trip.


## Usage

1. Double-check the previous steps in Bot Setup and Server Setup, otherwise it will probably fail.
2. Invite the bot to your Discord server using the OAuth2 link generated in the Discord Developer Portal.
3. Run the bot by executing the following command:

   ```
   python bot.py
   ```

   The bot will connect to Discord and display a message indicating a successful connection.

4. To test the bot and manually trigger a user's movement to the backrooms, use the command `!test` in any text channel where the bot has permissions.
5. The bot will randomly select a user from a voice channel and move them to the backrooms.
6. After a specified duration, the user will be moved back to their original voice channel.


## Customization

You can customize the bot's behavior by modifying the code in the provided script. Here are a few possible modifications:

- Modify the sound effect played in the backrooms by replacing the file path in the `sound()` function call (`await sound("backkrooms.mp3", BackroomChannel)`).
- Customize the channel names and conditions for selecting random users by modifying the `get_floor_channel()`, `get_random_channel()`, and `get_random_user()` functions.

Feel free to explore and adapt the code according to your preferences and server requirements.


## Design

This bot is not designed to be well optimized or scalable. It is intended to be used in a small server with a limited number of users. The bot is designed to be simple and easy to use, and it can be easily modified to suit your needs.
**Warning** : The bot is not designed to be used once by more than 1 server at the same time. If you want to use it on multiple servers, you will need to create a new bot for each server or it could cause some issues.

## Disclaimer

This bot is intended for entertainment purposes only.
Please use this bot responsibly and consider the impact it may have on your server's members. It is essential to inform and gain consent from your community before introducing this type of bot to avoid any discomfort or negative experiences.

## Credits

This bot was created by [Arthur Mermet] and [Noah Kohrs] in 2 days to make a funny prank on our friends. 
We hope you will enjoy to use it as much as we enjoyed to create it.

Feel free to contact us if you have any questions or suggestions.