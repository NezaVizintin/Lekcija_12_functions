from guess_the_number_3.functions import *

# initialisation:
while True:
    main_menu = str(input("Would you like to A) play a new game, B) see the best scores, or C) quit? ")).lower()

    if main_menu == "a":
       print()
       game_difficulty = str(input("Do you want to play the game with hints? (Y/N) ")).lower()
       if game_difficulty == "y":
           run_game_easy()
       elif game_difficulty == "n":
           run_game_hard()
       else:
           print()
           print("Oh jeez, worng input. Next time select 'y' for YES and 'n' for NO.")
           print()
           continue

    elif main_menu == "b":
        top_score()
    elif main_menu == "c":
        break
    else:
        print("Oh no, wrong input. Please enter 'a', 'b', or 'c'.")
