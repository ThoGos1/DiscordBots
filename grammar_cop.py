import discord
import os
from keep_alive import keep_alive


client = discord.Client()


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  await client.change_presence(status = discord.Status.online, activity = discord.Game("Eating tofu"))


@client.event
async def on_message(message):
  text = message.content.capitalize()
  wrong = False
  sug = ""
  

  ### Checks if message is from the bot ifself
  if(message.author == client.user):
    return
  
  
  ### Makes sure that the language might not be Danish
  if("å" in message.content or "ø" in message.content or "æ" in message.content):
    return


  ### Checks for dont and changes to don't
  while("dont" in text):
    wrong = True
    text = text.replace("dont", "don't")
    sug += "*don't"
    sug += " "


  ### Checks for i and changes to I
  while(" i " in text):
    wrong = True
    text = text.replace(" i ", " I ")
    sug += "*I"
    sug += " "
  

  ### Checks for im and changes to I'm
  while("im " in text):
    wrong = True
    text = text.replace("im", "I'm")
    sug += "*I'm"
    sug += " "


  ### Checks for isnt and changes to isn't
  while("isnt " in text):
    wrong = True
    text = text.replace("isnt", "isn't")
    sug += "*isn't"
    sug += " "


  ### Checks for aint and changes to ain't
  while("aint " in text):
    wrong = True
    text = text.replace("aint", "ain't")
    sug += "ain't"
    sug += " "


  ### Checks for couldve and change to could've
  while("couldve " in text):
    wrong = True
    text = text.replace("couldve", "could've")
    sug += "*could've"
    sug += " "


  ### Checks for ill and change to I'll
  while("ill " in text):
    wrong = True
    text = text.replace("ill", "I'll")
    sug += "*I'll"
    sug += " "

    
  ### Checks for youre and change to you're
  while("youre " in text):
    wrong = True
    text = text.replace("youre", "you're")
    sug += "*you're"
    sug += " "

    
  ### Sends the the suggested correction
  if(wrong):
    await message.channel.send(sug)

  ### End of Function


keep_alive()
# Make a .env file with your Discord bot token, or use Replit, as it has its own private/environment variable page, with easy access.
client.run(os.getenv('token'))
