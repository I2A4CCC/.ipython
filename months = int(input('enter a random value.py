def pig_latin(texts):
  say = ""
  # Separate the text into words

  for text in texts:
    indexing = text[0:] 
    say = indexing
    return say
 
    
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"