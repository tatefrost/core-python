"""Restaurant rating lister."""

scores = open("scores.txt", "r")
ratings = {}

user_input = input("Please enter a restaurant name: ")
user_restaurant = user_input.capitalize()
user_score = 0

def judge_score():
    global user_score
    user_score = input("Please enter a rating between 0 and 5 for " + user_restaurant + ": ")
    if int(user_score) > 5 or int(user_score) < 0:
        print("That is not a number from 0 to 5, please try again.")
        judge_score()

def get_ratings():
    ratings[user_restaurant] = user_score
    for line in scores:
        pair = line.split(":")
        ratings[pair[0]] = pair[-1].strip()

def print_ratings_alphabetical():
    item = ratings.items()
    alpha = sorted(item)
    for pairs in alpha:
        print(pairs[0], "got a rating of", pairs[1] + ".")

judge_score()
get_ratings()
print_ratings_alphabetical()

scores.close()