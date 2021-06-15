import discord
import os
from keep_alive import keep_alive
from sympy import *


client = discord.Client()

x = Symbol('x')


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  await client.change_presence(status = discord.Status.online, activity = discord.Game("Hanging with Newton"))


@client.event
async def on_message(message):
  
  ### Checks if message is from the bot ifself
  if(message.author == client.user):
    return

  eq = message.content[5:]
  print(eq)
  lims = ""
  a = ""
  b = ""
  c = ""
  btemp = ""

  if(',' in message.content):
    eq = message.content[5:message.content.index(',')]
    print("Equation:")
    print(eq)
    lims = message.content[message.content.index(',')+1:]
    print("lims value:")
    print(lims)

  if(',' in lims):
    a = lims[0:lims.index(',')]
    print("a value:")
    print(a)
    btemp = lims[lims.index(',')+1:]
    print("btemp value:")
    print(btemp)

  if(',' in btemp):
    b = btemp[0:btemp.index(',')]
    print("b value:")
    print(b)
  else:
    b = btemp

  if(',' in btemp):
    c = btemp[btemp.index(',')+1:]
    print("c value:")
    print(c)


  # Help Function
  if(message.content == '+help'):
    await message.channel.send('```Calculus Bot Help:\n\nLimits: +lims [function],[value]\nDerivative: +diff [function]\nAntiderivative: +inte [function]\nDefinite Integral: +defi [function],[a],[b]\nArea Between Curves: +area [function1],[function2],[a],[b]\nAverage Value: +avgv [function],[a],[b]\nInstantaneous Rate of Change: +iroc [function],[value]\nAverage Rate of Change on (a,b): +aroc [function],[a],[b]\n\nVolume of Revolutions:\nOBS: If the function(s) are revolved around another line than the x-axis, remember to subtract that line from the [function] part. Ex. if x^2 is revolved around x=2, then you would write x**2 - 2 as the function.\nDisk Volume of Revolution: +dvol [function],[a],[b]\nWasher Volume of Revolution: +wvol [function1],[function2],[a],[b]\n\nCross Section Volumes:\nOBS: These calculations can take a couple of seconds\nCross Section of Square: +cssq [function1],[function2],[a],[b]\nCross Section of Semi-Circle: +cssc [function1],[function2],[a],[b]\n\nHow functions and symbols look:\n2x^2 = 2*x**2\ne^x = exp(x)\nSquareroot of x = sqrt(x)\nInfinity = oo\n\nHelpful tip: All these functions are default for "y=" or "f(x)" but if you need horizontal strips for areas or your volume is revolved the y-axis then write the function as a "x=" or "f(y)" and also find the y= values for the limits, then you can put then in just using x, and get your answer!!!```')
  
  
  # Derivatives
  if(message.content.startswith('+diff')):
    expr = diff(eq, x)
    await message.channel.send(expr)
  

  # Antiderivative
  if(message.content.startswith('+inte')):
    expr = integrate(eq, x)
    defexp = "{} + C".format(expr)
    await message.channel.send(defexp)
  

  # Indef integrate
  if(message.content.startswith('+defi')):
    expr = integrate(eq, (x, a, b))
    await message.channel.send(expr)
  

  # Area between curves
  if(message.content.startswith('+area')):
    height = "{} - {}".format(eq, a)
    expr = integrate(height, (x, b, c))
    await message.channel.send(expr)


  # Washer Volume
  if(message.content.startswith('+wvol')):
    height = "({})**2 - ({})**2".format(eq, a)
    print("height val:")
    print(height)
    expr = integrate(height, (x, b, c))
    await message.channel.send(pi * expr)


  # Disk Volume
  if(message.content.startswith('+dvol')):
    height = "({})**2".format(eq)
    expr = integrate(height, (x, a, b))
    await message.channel.send(pi * expr)


  # Limits
  if(message.content.startswith('+lims')):
    expr = limit(eq, x, lims)
    await message.channel.send(expr)


  # Average Value
  if(message.content.startswith('+avgv')):
    expr = integrate(eq, (x, a, b))
    await message.channel.send(N(1/(int(b)-int(a)) * expr))


  # Square Cross Section
  if(message.content.startswith('+cssq')):
    height = "({} - {})**2".format(eq, a)
    expr = integrate(height, (x, b, c))
    await message.channel.send(N(expr))


  # Semi-Circle Cross Section
  if(message.content.startswith('+cssc')):
    height = "({} - {})**2".format(eq, a)
    expr = integrate(height, (x, b, c))
    print(8/pi * expr)
    await message.channel.send(N(8/pi * expr))


  # Instantaneous Rate of Change
  if(message.content.startswith('+iroc')):
    derv = diff(eq,x)
    expr = derv.subs(x, lims)
    await message.channel.send(expr)


  # Average Rate of Change
  if(message.content.startswith('+aroc')):
    derv = diff(eq,x)
    fb = derv.subs(x,b)
    fa = derv.subs(x,a)
    await message.channel.send((int(fb)-int(fa)) / (int(b)-int(a)))


  ### End of Function


keep_alive()
# Make a .env file with your Discord bot token, or use Replit, as it has its own private/environment variable page, with easy access.
client.run(os.getenv('token'))
