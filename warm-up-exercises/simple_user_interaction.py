def display_game(game_list):
  print("Here is the current list")
  print(game_list)


def gameon_choice():
  choice = 'wrong'

  while choice not in ['Y', 'N']:
    choice = input('Do you want to carry on playing? (Y or N) ')

    if choice not in ['Y', 'N']:
      print('Please choose either Y or N ')

  return choice == 'Y'


def replacement_choice(game_list, position):
  replacement = int(input("What would you like to replace it with? "))

  for n, i in enumerate(game_list):
    if i == position:
      game_list[n] = replacement

  return game_list


def position_choice():
  choice = 'wrong'
  included = False

  while choice.isdigit() == False or included == False:
    choice = input("Pick a a position to replace: ")

    if choice.isdigit() == False:
      print("Sorry that is not digit!")

    if choice.isdigit():
      if int(choice) in game_list:
        included = True
        return int(choice)
      else:
        included = False
        print("Sorry, that is not an available number!")


game_on = True
game_list = [0, 1, 2]

while game_on:
  display_game(game_list)

  position = position_choice()

  game_list = replacement_choice(game_list, position)

  display_game(game_list)

  game_on = gameon_choice()
