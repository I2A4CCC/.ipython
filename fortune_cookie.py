# Write code below 💖

# creating a fortune cookie functions

import random

def fortune():
  
  option = random.randint(1, 8)
  if option == 1:
    print('Dont persue happiness, create it')
  elif option == 2:
    print('All things are difficult before they are easy.')
  elif option == 3:
    print('The early bird gets the worm, but the second mouse gets the cheese.')
  elif option == 4:
    print('Someone in your life needs a letter from you.')
  elif option == 5:
    print('Dont just think. Act!')
  elif option == 6:
    print('Your heart will skip a beat.')
  elif option == 7:
    print('The fortune you search for is in another cookie.')
  elif option == 8:
    print('Help! I amm being held prisoner in a Chinese bakery')
  else:
    print ('You ran out of tries')
  
fortune()


