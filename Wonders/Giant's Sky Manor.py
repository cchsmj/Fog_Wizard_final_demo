from colorama import Style
from functions import data_update, riddle_ask, sky_mansion, GSM_start
import time

def main():

  lb = '\033[38;5;37m'
  s = Style.RESET_ALL
  bb = Style.BRIGHT 
  i = '\033[3m'
  new_page = '\x1bc'
  Sky_Manor = {'a': 'jinmenshi fruit', 'b': 'Dragon\'s Poppy', 'c': 'Sinister Ivy', 'd': 'wisteria flower'}

  sky_mansion()
  time.sleep(4)
  print(lb + bb + '\nThe sky haven of the great Giant Theodore, who isn\'t quite friendly. He built his home on the magic bean sprout, which was stolen from him centuries ago...\n' + s)
  time.sleep(6)

  print(i + 'Giant: ' + s + 'Trespasser! What is your business here? Speak quickly or I shall eat you.') 
  time.sleep(4)
  print(i + 'You: ' + s + 'Wait, wait! The Fog Wizard sent me. I need an ingredient.')
  time.sleep(5)
  print(i + 'Giant: ' + s + 'Lucky you are that I know your Master. He helped me grow this very bean sprout...\n')
  time.sleep(3)
  print(i + 'Giant: ' + s + 'I tell you what. I\'m fond of gambling and treasure. I\'ll let you into my garden if you play Poison and Potion with me.')
  time.sleep(1)
  print(i + 'You: ' + s + 'Fine.')
  time.sleep(7)

  print(new_page)
  GSM_start()
  print(new_page)
  
  print(i + 'Giant: ' + s + 'Wow, you\'re a strong gambler. You\'re allowed to enter. I hope you find what you need here.\n')
  print('Items found: ')
  for key, value in Sky_Manor.items():
    print(key,'.',value)


  collect = input('Do you wish to add any of these items? ')
  if collect.lower() == 'yes':
      key = input('The letter (a,b,c) of desired item: ')
      print('\n')
      item = Sky_Manor[key]
      data_update(item)
      riddle_ask()
  else:
    riddle_ask()
  
if __name__ == "__main__":
    main()