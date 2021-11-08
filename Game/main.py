import time
from colorama import Fore, Style
from functions import wizards_chamber, name_random, riddle, instructions


def main():

  s = Style.RESET_ALL
  r = Fore.RED
  g = Fore.GREEN
  b = Fore.BLUE
  y = Fore.YELLOW
  p = Fore.MAGENTA
  i = '\033[3m'
  new_page = '\x1bc'
  book_color = '\033[38;5;196m'
  

  #Intro to game
  name = input('\nWelcome to the Quest Realm!\nWhat is your name wanderer? ')
  print('Prepare yourself '+ name_random(name) + ' for a quest that will test your mind and sanity...')
  print('\n')
  time.sleep(3)

  print(r + 'Your journey begins now' + s)
  time.sleep(5)

  #Intro to quest and instructions
  wizards_chamber()
  print(i + 'Wizard: ' + s + 'I\'ve been waiting for you...')
  time.sleep(2)
  print(i + 'You: ' + s + 'Me?...Why? ')
  time.sleep(2)
  print(i + 'Wizard: ' + s + 'I\'ve waited years to finish my ' + g + 'potion.' + s + '\n')
  time.sleep(3)

  print(i + 'Wizard: '+ s + 'No time to waste...' + i + ' I need ingredients.')
  time.sleep(3)

  print(i + 'You: ' + s + 'Wait. What\'s in it for me?')
  time.sleep(2)
  print(i + 'Wizard: ' + s + '*tsk* I guess I can compensate you for this great task. That is if you succeed.')
  time.sleep(5)

  print('\n')
  print(i + 'Wizard: ' + s + 'BEHOLD.' + book_color + ' The Book of the Gods.' + s + ' I shall reward you with ' + i +  'all' + s +  ' knowledge, wisdom, and power, both good and evil, possessed in this book.')
  time.sleep(4)

  print(i + 'You: ' + s + 'Whoa... that\'s crazy. I don\'t know if I can take such an important book. Are you sure?')
  time.sleep(4)

  print('\n')
  commission = input(i + 'Wizard: ' + s + 'Do you accept the challenge, yes or no? ')

  if commission.lower() == 'no':
    print(i + 'Wizard: ' + s + r + 'THEN OUT OF MY SIGHT!')
    time.sleep(2)
    print(new_page)
  else:
    print('\n')
    print(i + 'Wizard: ' + s + 'Excellent. Each ingredient I need for my potion exists in the 5 Wonders of the Quest Realm. Follow the riddles, go to the Wonders, collect the items, and return them to me. You shall be greatly rewarded.')
    time.sleep(12)
    print(new_page)

    instructions()
    print('\n')

    # Quest begins with riddles. Needed Items are listed. 
    print(riddle(1))
    print('In a place of striveled dreams, a teacher once with spirits of breeze, now fog and debris. Beneath the rubble, find the cobbwebs covered in purple magic subtle.')

if __name__ == "__main__":
    main()