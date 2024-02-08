#main.py
# Use: see README.md
# Note: Dev choices are `camelCaseEd` . . .
#  OR `PascalCase` where importing (see line 26+27).
# ~Instances of `snake_case` are from Discord Python Library `discord`~
# **Code narration fully left aligned**
# Import the standard Python logging library
import logging
# Set logging.DEBUG to see ALL logs; logging.INFO for less
logging.basicConfig(level=logging.INFO)

# Set Discord channel for to say Hello wen On Ready
#    1088511652619632670 (Server:CB Channel:#⏱│be-on-time)
# To easily get the channel/server ID: open Discord, go to Settings > Advanced; and enable `developer mode`. 
channelToPingWenReady = 1088511652619632670 
# Set the message you want to Announce to the World
messageToPingWenReady = "Hello!\nCasting Discord as Harmony:bangbang:"

# Be sure you have set your DISCORD_TOKEN as environment variable
import os
harmonyBotToken = os.environ.get('DISCORD_TOKEN')
logging.debug(harmonyBotToken)

# Create a Discord BOT object as beOnTime (camelCase)
#   `pip install discord` required for this code to work
import discord as Harmony
from discord.ext import commands as CommANDs
inTenTs = Harmony.Intents.default()
inTenTs.typing = True
inTenTs.presences = True
inTenTs.messages = True
inTenTs.guilds = True 
inTenTs.members = False 
inTenTs.message_content = True
beOnTime = CommANDs.Bot(command_prefix="~", intents=inTenTs)
# View the BOT Object if DEBUG logging is enabled.
logging.debug(f"--BOT START--\n{beOnTime}\n--BOT END--")

# Create an event listener for wen Discord BOT go `on_ready`
@beOnTime.event
async def on_ready():
# Change presence settings
    await beOnTime.change_presence( status=Harmony.Status.online, activity=Harmony.Game(messageToPingWenReady) )
# Get a channel for to ping wen first coming online
    gotChannel = beOnTime.get_channel(channelToPingWenReady)
# Check if we got a channel (does your bot have access to that?)
    if gotChannel is not None:
# Send a message to the channel
        await gotChannel.send(f"{messageToPingWenReady}")
# Get the topic of the channel
        chanTopic = gotChannel.topic
# Log details to the CONSOLE
        logging.debug(f"channelToPingWenReady topic set as: {chanTopic}")
        logging.info(f"BOT Activity: {beOnTime.activity}")
# Maybe that all failed, because your bot didn't have access.
    else:
# Log an error if unable to get `channelToPingWenReady`.
        logging.error(f"Unable to get channel: {channelToPingWenReady}")
    logging.info(f"We have logged in as: {beOnTime.user}")

# Create an event listener for wen Discord BOT get new `on_message`
@beOnTime.event
async def on_message(meSsage):
# Skip if from self (Harmony BOT)
    if meSsage.author == beOnTime.user:
# Log acknowledgment 2 da bACKend CONSOLE B4 return of Ray.
        logging.info(f"Hayyy you?? {meSsage.author.name} saw @{meSsage.author.id} echo!!")
        return
# Don't skip any other type of incoming message
    else:
# Set the Discord client intent `is typing...`
        async with meSsage.channel.typing():
# Do things like respond to `.hello`
            if meSsage.content.startswith('.hello'):
# Example: Log a message to the CONSOLE that command was received.
                logging.debug('-----\n.hello received\n---------------')
# Send a message back to the player that pinged this beOnTime
                await meSsage.channel.send("Hello Player!") 
# Example: Reply `.delete` to have the bot delete a message.
            elif meSsage.content.startswith('.delete'):
# Check if new meSsage contains a reference to Discord message
                if meSsage.reference:
# Perform a try-catch for exception handling while not able to delete
                    try:
# Set a reference ID while exist a `reference.message_id` or `None`
                        reFeRENcEdMesSage = await meSsage.channel.fetch_message(meSsage.reference.message_id)
# Make the code pause/`await` until the message is deleted.
                        await reFeRENcEdMesSage.delete()
# While any exception to deleting the message; throw exception as `eVoidEd`
                    except Exception as eVoidEd:
# Reply the exception error to Discord
                        await meSsage.channel.send(f"Error deleting message: {eVoidEd}")
# Log the exception error to the CONSOLE
                        logging.error(f"Error deleting message: {eVoidEd}")
# Delete the `.delete` command message regardless of try-catch
                await meSsage.delete()  # Delete the command message
                return
# Run the BOT that we just procedurally scripted as `beOnTime`
beOnTime.run(harmonyBotToken)
## (beOnTime see above; line 35 ??)
## (harmonyBotToken see above; line 21 ??)
