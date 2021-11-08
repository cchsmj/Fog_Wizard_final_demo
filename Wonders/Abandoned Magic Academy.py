from colorama import Fore, Style
from functions import data_update, riddle_ask, magic_academy
import time

def main():
  p = Fore.MAGENTA
  s = Style.RESET_ALL
  Mage_Academy = {'a': 'purple spellbound cobbwebs', 'b': 'enchanted textbook', 'c': 'dissected Bubonic frog', 'd': 'broken flasks'}

  magic_academy()
  time.sleep(4)
  print(p + 'An old academy full of past magic. The Fog Wizard\'s old pride and joy. Before his downfall, the Fog Wizard was an esteemed magi teacher. Now there are no students and the campus sits in its remains of past glory.\n' + s)

  print('Items found: ')
  for key, value in Mage_Academy.items():
    print(key,'.',value)


  collect = input('Do you wish to add any of these items? ')
  if collect.lower() == 'yes':
      key = input('The letter (a,b,c) of desired item: ')
      print('\n')
      item = Mage_Academy[key]
      data_update(item)
      riddle_ask()
  else:
    riddle_ask()
    
  

if __name__ == "__main__":
    main()