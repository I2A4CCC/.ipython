# creating  a program to find area
def pass_word():
    counter = 0
    pass_code = input('enter a random password: ')
    while counter != 3:
        if len(pass_code) < 8:
          print('pass_word is short try again')
        elif len(pass_code) >= 8 :
          print('Valid password')
        else:
          return
            
pass_word()
