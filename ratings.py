"""Restaurant rating lister."""

scores = open("scores.txt", "r")
ratings = {}

user_restaurant = input("Please enter a restaurant name: ")
user_score = input("Please enter a rating between 0 and 5 for " + user_restaurant + ": ")

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

get_ratings()
print_ratings_alphabetical()

scores.close()