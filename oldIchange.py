  ### Checks for i's:
  if(' i ' in text):
    #print('i is in it: ' + message.content)
    #print(len(message.content))
    while(i < len(text)):

      if(text[i-1:i+2] == " i "):
        ret += text[i:i+1].upper()
        #print("index is i")
      else:
        ret += text[i:i+1]
        #print("index is not i")
      
      i = i+1
    


    await message.channel.send(ret + "*")
