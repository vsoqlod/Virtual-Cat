"""
Gabriel Quezada, Thuan Nguyen, Jae Bum Jang
Fall 2022, 10/18
Lab 9 - Group 17

This program is interactive pet game that user has own life points and interacts with different types of cats with different raise level.
"""

import tabby
import ocelot
import tiger
import check_input
import player

def interact_cat(cat, player):
  """Display cat menu, prompt user to choose one of option from it then display the choice of interaction with the cat."""
  print('Cat Menu:')
  print('1. Feed your cat')
  print('2. Play with your cat')
  print('3. Pet your cat')
  choice = check_input.get_int_range('Enter choice: ', 1, 3)
  if choice == 1:
    print(cat.feed(player))
  elif choice == 2:
    print(cat.play(player))
  elif choice == 3:
    print(cat.pet(player))



def main():
  """Prompt user to choose type of cat, let them name the cat then call the interaction with the cat based on the choice of the cat. Display message when player's hit point become zero then program terminate."""
  human = player.Player()
  
  print("Cat Selection:\n1. Tabby Cat\n2. Ocelot\n3. Tiger")
  choice_cat = check_input.get_int_range("Enter choice: ", 1, 3)
  name = input("Name your kitty: ")
  if choice_cat == 1:
    cat = tabby.Tabby(name)
  elif choice_cat == 2:
    cat = ocelot.Ocelot(name)
  elif choice_cat == 3:
    cat = tiger.Tiger(name)

  while human.hp_property > 0:
    print(human)
    print(cat)
    interact_cat(cat, human)

  print(f"\nYour cat, {cat.name} killed you...")
  
main()