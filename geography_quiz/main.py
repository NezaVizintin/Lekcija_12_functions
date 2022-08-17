from countryinfo import CountryInfo # used "pip install countryinfo" in terminal to install countryinfo module
import json
import random

# ------- if player gets answer wrong, let them try again -------

def run_game():
    try:
        correct_answer_boolean = True
        while correct_answer_boolean == True:
            answer = str(input("What is the capital of {0}? ".format(country))).lower()
            if answer == str(CountryInfo(country).capital()).lower():
                print("Well done!")
                correct_answer_boolean = False
            else:
                print("Sorry, try again!")
    except:
        print(CountryInfo(country))

def random_country():
    with open("countries.json", "r") as countries_file:
        countries = json.loads(countries_file.read())
    return random.choice(countries)

while True:
    country = random_country()
    continue_playing = str(input("Do you want to guess a capital? (Y/N) ")).lower()
    if continue_playing == "y" or continue_playing == "yes":
        run_game()
    elif continue_playing == "n" or continue_playing == "no":
        break
    else:
        print("Whoopsie, wrong input. Please enter 'y' or 'n'.")
        print()
        continue
