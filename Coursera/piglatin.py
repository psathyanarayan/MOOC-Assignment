import json
def pig_latin(text):
  say = []
  # Separate the text into words
  words = text.split()
  for word in words:
    # Create the pig latin word and add it to the list
    for i in range(len(word)):
      if i!=0:
        say.append(word[i])
        if i==len(word)-1:
          say.append(word[0])
          say.append("ay ")
          end=""
        
    # Turn the list back into a phrase
  return json.dumps(("".join(say)).strip())
		
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"
