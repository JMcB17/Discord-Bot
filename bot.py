#imports
import discord

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


#run whenever message sent
@client.event
async def on_message(message):
    #we don't want the bot to reply to itself
##    if message.author == client.user:
##        return 0
    #haha yes we do and if it's a problem we'll address it then

    #check for prefix
    if message.content.startswith(prefix):
        command = message[len(prefix):]
        if command in functions:
            

#functions

#test to run functions
def test(channel, function):
    

#basic print ello world thing
def greeting(channel):
    out_message = "print hello world"
    await client.send_message(channel, out_message)



