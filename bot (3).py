#imports
import asyncio
import discord
import re

#stating the obvious
#token
token = "NTQxNjEyNDk3NTE0MjY2NjI0.DziEFQ.ZDgR4mpvhIOw5iQQVQbh6hD6RjA"


#shell

#client
client = discord.Client()

#start bot
@client.event
async def on_ready():
    print("ENTER THE BOT DIMENSION")
    print("Name: {}".format(client.user.name))
    print("Bot: {}".format(client.user.bot))
    print("Notice: If Bot is not true, we are in deep -MESSAGE TERMINATED;")
    print("Running\n")

    out_msg = "hello there"
    #fix channel input
##    await client.send_message("joels-temp-bot-place", out_msg)

#run whenever message sent
@client.event
async def on_message(message):
    print("Message detected in channel: {}".format(message.channel))

    print("Checking for commands")
    
    #prefix
    prefix = "invoke"
    
    #we don't want the bot to reply to itself
##    if message.author == client.user:
##        return 0
    #haha yes we do and if it's a problem we'll address it then

    #check for prefix for commands
    if message.content.startswith(prefix):
        print("Command found:")
        #strip command and cast to list
        command = message.content.strip().split()
        print(message.content)
        #attempt run command
        #first item of command list will be the message for use by cmd funcs
        await run([message]+command)
    else:
        print("Not a command")
        
    #check for conditions

#DOCUMENTATION
#command[x]
#0 is message object
#1 is prefix
#2 is command name
#3+   passed arguments

#functions
            

#function to find command function
async def run(command):
    #check command is present and not just prefix
    if len(command) < 3:
        out_msg = "You can't invoke nothing!"
        await client.send_message(command[0].channel, out_msg)
        await bot_help(command)
        return 0
    
    #iterate over each function and run if correct
    for cmd_names in cmd_funcs.keys():
        if command[2].lower() in cmd_names:
            await cmd_funcs[cmd_names](command)
            return 1
    #else print not found
    print("Command not found")
    await client.send_message(command[0].channel, "Command not found.")
    return 0

#test to run functions
#DEPRECATED: realised it was pointless.
##def test(command, args):
##    run(function, args)

#basic print ello world thing
async def greeting(command):
    out_msg = "print hello world"
    await client.send_message(command[0].channel, out_msg)

#silly framework demo function I added
async def ronnoc(command):
    out_msg = "efilrebyc yb tnes diordna eht m'I"
    await client.send_message(command[0].channel, out_msg)

#help (list commands)
async def bot_help(command):
    out_msg = "Help section (wip) - list of commands:"
    for invocations in cmd_funcs.keys():
        out_msg += "\n {}".format(invocations[0])
    await client.send_message(command[0].channel, out_msg)

cmd_funcs = {("test", "run"): run,
             ("greeting", "hello", "hi"): greeting,
             ("ronnoc", "android"): ronnoc,
             ("bot help", "help",  "commands"): bot_help}


#message scan procedures




#run the bot
client.run(token)
