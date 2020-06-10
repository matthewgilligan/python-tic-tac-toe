game_list = [0, 1, 2]


def display_game(game_list):
  print("Here is the current list")
  print(game_list)


def replacement_choice(game_list, position):
  replacement = input("What would you like to replace it with? ")


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
        replacement_choice(game_list, int(choice)
      else:
        print("Sorry, that is not an available number!")
        included=False

# def gameon_choice():


display_game(game_list)
position=position_choice()
