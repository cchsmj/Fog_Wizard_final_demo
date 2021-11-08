from colorama import Fore
from colorama import Style
import random
import time


def data_update(item):
  game_data = {'backpack': [], 'wizards_ingredients': []}

  response = input('Collect ' + item + '? ')
  if  response == 'yes':
    game_data['backpack'].append(item)
    print('\nYour Collection: ')
    for values in game_data['backpack']:
      print(values)
  return game_data['backpack']

  print('\nYour collection: \n')
  for values in game_data['backpack']:
      print(values)
  return game_data['backpack']

def compare_lists(backpack, wizard):
  backpack = set(backpack)
  wizard = set(wizard)
  if wizard.difference(backpack):
    print('You are missing: ')
    for values in wizard.difference(backpack):
      print(values)

def wizards_chamber():
  print(Fore.MAGENTA + '—' * len('Fog Wizard\'s Chambers'))

  print(Fore.GREEN + Style.DIM + 'Fog Wizard\'s Chambers' + Style.RESET_ALL)

  print(Fore.MAGENTA + '—' * len('Fog Wizard\'s Chambers') + Style.RESET_ALL)

def sky_mansion():
  print('\n')
  print(Fore.BLUE + '-' * len('Giant\'s Sky Mansion'))

  print('\033[38;5;44m' + Style.BRIGHT + 'Giant\'s Sky Mansion' + Style.RESET_ALL)

  print(Fore.BLUE + '-' * len('Giant\'s Sky Mansion'))

def magic_academy():
  print('\n')
  print(Fore.MAGENTA + '⁠—' * len('Abandoned Magic Academy'))
  print('\033[38;5;248m' + 'Abandoned Magic Academy')
  print(Fore.MAGENTA + '⁠—' * len('Abandoned Magic Academy'))

def card_name(card_rank):
    if card_rank == 1:
        return 'Wizard'
    if card_rank == 11:
        return 'Apprentice'
    if card_rank == 12:
        return 'Maiden'
    if card_rank == 13: 
        return 'King\'s Council'
    return str(card_rank)

def card_value(card_rank):
    if card_rank == 1:
        return 11
    if card_rank >= 11 and card_rank <= 13: 
        return 10
    return card_rank

def end_turn_status(hand):
    if hand > 21:
        return 'POISON.'
    if hand == 21:
        return 'POTION!'
    return ''

def end_game_status(user_hand, dealer_hand):
    if dealer_hand <= 21 and (dealer_hand > user_hand or user_hand > 21):
        return 'Giant wins!'
    if user_hand <= 21 and (user_hand > dealer_hand or dealer_hand > 21):
        return 'You win!'
    return 'Tie.'

def GSM_mini_game():
    print(Fore.MAGENTA + Style.BRIGHT + '\nYOUR TURN' + Style.RESET_ALL)

    user_hand = 0
    drawn_count = 0
    hit = 'y'

    while hit == 'y':
        card_rank = random.randint(1, 13)
        name = card_name(card_rank)
        value = card_value(card_rank)

        print('You drew a ' + name)
        user_hand += value

        drawn_count = drawn_count + 1

        if user_hand >= 21:
          hit = 'n'
        elif drawn_count >= 2:
          hit = input('You have ' + str(user_hand) + '. Draw again (y/n)? ')

    print('Final hand: ' + str(user_hand) + '.')
    print(end_turn_status(user_hand))

    print(Fore.RED + '\nGIANT\'S TURN' + Style.RESET_ALL)

    dealer_hand = 0
    drawn_count = 0

    while dealer_hand <= 17:
        if drawn_count >= 2:
          print('Giant has ' + str(dealer_hand) + '.')

        card_rank = random.randint(1, 13)
        name = card_name(card_rank)
        value = card_value(card_rank)

        print('Giant drew a ' + name)
        dealer_hand += value

        drawn_count = drawn_count + 1
    print('Final hand: ' + str(dealer_hand) + '.')
    print(end_turn_status(dealer_hand))

    print(Fore.GREEN + '\nGAME RESULT' + Style.RESET_ALL)

    print(end_game_status(user_hand, dealer_hand)) 
    return end_game_status(user_hand, dealer_hand)

def GSM_start():
  print('\033[3m' + 'Giant: ' + Style.RESET_ALL + 'To win Poison or Potion you need a hand of 21 or your hand must be greater than mine. If you go over 21, you get POISON. If you get 21 exact, you get POTION. You can draw as many times you want.\n')
  time.sleep(8)
  mini_game = ''
  while mini_game == '' or mini_game == 'Giant wins!' or mini_game == 'Tie.':
    mini_game = GSM_mini_game()
    if mini_game == 'You win!':
      time.sleep(5)
    else:
      print('Giant: Looks like you failed your Master. Better keep at it.')
      time.sleep(5)


def name_random(name):
  name_list = ['Mighty forager ', 'All seeing ', 'Curious ', 'Apprentice ', 'Chosen helper ', 'Great ', 'Heroic ']
  username = random.choice(name_list) + name
  return username

def riddle(num):
  color_list = ['\033[38;5;214m', '\033[38;5;65m', '\033[38;5;201m', '\033[38;5;9m', '\033[38;5;4m', '\033[38;5;197m']
  riddle_color = random.choice(color_list) + '\nRIDDLE # ' + str(num)
  return riddle_color

def instructions():
  print('\033[3m' + 'As the Fog Wizard said, navigate between the Wonders of the Quest Realm to find the requested values. Follow the riddles carefully.')
  print('\n')
  print('First type in \'cd ..\'. Then type \'cd Wonders\' to enter the Quest Realm.')
  time.sleep(4)
  print('\033[3m' + 'Look at your surroundings with the command \'ls\'.\n Move to a new location with the command \'cd\' + the name of the location you wish to go.\n Backtrack with the command \'cd..\'\n')
  time.sleep(6)

def riddle_ask():
  choice = input('\nDo you want the next riddle, or do you wish to keep looking?\na. next riddle \nb. keep looking\n')
  count = 5
  num = 1
  while count > 0:
    if choice == 'a' or choice == 'a.':
      print(riddle(num + 1))
      count -= 1
      print('Remember the story of the magic bean that sprouted high? Up above, treasures more than meets the eye? If you don\'t know what I mean then nevermind. Collect the sought after hallucinogen that makes grown men cry.')
    else:
      break