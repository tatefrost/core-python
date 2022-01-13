"""Restaurant rating lister."""

from os import EX_TEMPFAIL
from random import choice

print("\nHello, welcome to your favorite restaurant rater!")


scores = open("scores.txt", "r")
user_restaurant = ""
user_score = 0
ratings = {}
item = ratings.items()

def get_ratings():
    if user_restaurant != "":
        ratings[user_restaurant] = user_score
    for line in scores:
        pair = line.split(":")
        ratings[pair[0]] = pair[-1].strip()

def print_ratings_alphabetical():
    global item
    alpha = sorted(item)
    print("\n")
    for pairs in alpha:
        print(str(pairs[0]), "got a rating of", str(pairs[1]) + ".")

def judge_score():
    global user_restaurant
    global user_score
    user_input = input("\nPlease enter a restaurant name: ")
    user_restaurant = user_input.capitalize()
    user_score = input("\nPlease enter a rating between 0 and 5 for " + user_restaurant + ": ")
    if int(user_score) > 5 or int(user_score) < 0:
        print("\nThat is not a number from 0 to 5, please try again.")
        judge_score()

def update_random():
    global user_score
    global item
    get_ratings()
    in_list = list(item)
    random_choice = choice(in_list)
    print("\n" + str(random_choice[0]), "got a rating of", str(random_choice[1]) + ".")
    new_rating = input("\nGive " + str(random_choice[0]) + " a new rating: ")
    user_score = new_rating
    ratings[random_choice[0]] = new_rating
    get_ratings()
    print_ratings_alphabetical()

def update_chosen():
  global user_score
  get_ratings()
  print_ratings_alphabetical()
  user_choice = input("\nPlease type the exact name of the restaurant whose score you would like to update: ")
  new_rating = input("\nPlease enter a new score for " + user_choice + ": ")
  if user_choice not in ratings:
      print("\nThat restaurant is not in the list, please try again.\n")
      update_chosen()
  else:
      user_score = new_rating
      ratings[user_choice] = new_rating
      get_ratings()
      print_ratings_alphabetical()
      return

def main():
    print("\nWould you like to see all the ratings in alphabetical order?\nPress A\nWould you like to add a new restaurant?\nPress N\nWould you like to update the score on a chosen restaurant?\nPress UC\nWould you like to update a score on a random restaurant?\nPress UR\nWould you like to Quit?\nPress Q")
    user_operation = input("Enter here: \n")

    if user_operation.lower() == "a":
        get_ratings()
        print_ratings_alphabetical()
        main()
    elif user_operation.lower() == "n":
        judge_score()
        get_ratings()
        print_ratings_alphabetical()
        main()
    elif user_operation.lower() == "ur":
        update_random()
        main()
    elif user_operation.lower() == "uc":
        update_chosen()
        main()
    elif user_operation.lower() == "q":
        scores.close()
        return
    else:
        print("\nThat is not a valid command, please try again.")
        main()


main()