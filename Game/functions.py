from colorama import Fore
from colorama import Style
import random
import time


# def backpack_add(item):
#   backpack = []
#   response = input('Collect ' + item + '? ')
#   if  response == 'yes':
#     backpack.append(item)
#     print('\nYour Collection: ')
#     for items in backpack:
#       print(items)
#   return backpack
#   print('\nYour collection: \n')
#   for items in backpack:
#     print(items)
#   return backpack

# def compare_lists(backpack, wizard):
#   backpack = set(backpack)
#   wizard = set(wizard)
#   if wizard.difference(backpack):
#     print('You are missing: ')
#     for items in wizard.difference(backpack):
#       print(items)

def wizards_chamber():
  print(Fore.MAGENTA + '—' * len('Fog Wizard\'s Chambers'))
  print(Fore.GREEN + Style.DIM + 'Fog Wizard\'s Chambers' + Style.RESET_ALL)
  print(Fore.MAGENTA + '—' * len('Fog Wizard\'s Chambers') + Style.RESET_ALL)

def name_random(name):
  name_list = ['Mighty forager ', 'All seeing ', 'Curious ', 'Apprentice ', 'Chosen helper ', 'Great ', 'Heroic ']
  username = random.choice(name_list) + name
  return username

def riddle(num):
  color_list = ['\033[38;5;214m', '\033[38;5;65m', '\033[38;5;201m', '\033[38;5;9m', '\033[38;5;4m', '\033[38;5;197m']
  riddle_color = random.choice(color_list) + '\nRIDDLE # ' + str(num)
  return riddle_color

def instructions():
  print('\033[3m' + 'As the Fog Wizard said, navigate between the Wonders of the Quest Realm to find the requested items. Follow the riddles carefully.')
  print('\n')
  print('First type in \'cd ..\'. Then type \'cd Wonders\' to enter the Quest Realm.')
  print('\033[3m' + 'Look at your surroundings with the command \'ls\'.\n Move to a new location with the command \'python\' + the name of the location you wish to go.\n Backtrack with the command \'cd..\'\n')
  time.sleep(8)

