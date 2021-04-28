import gtts 
a=input("enter text")
language='en'
b=gtts.gTTS(a,lang=language,slow=False)
c=input("enter audio file name to save converted speech to audio")
b.save(c+".mp3")
print("pls find the file in the executed folder with given name")
#os.system("mpg321 c.mp3")
#The above os.system function can be used if you have mpg321 tool in windows
