"""Restaurant rating lister."""


print("\nHello, welcome to your favorite restaurant rater!")


scores = open("scores.txt", "r")
user_restaurant = ""
user_score = 0
ratings = {}


def get_ratings():
    if user_restaurant != "":
        ratings[user_restaurant] = user_score
    for line in scores:
        pair = line.split(":")
        ratings[pair[0]] = pair[-1].strip()

def print_ratings_alphabetical():
    item = ratings.items()
    alpha = sorted(item)
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

def main():
    print("\nWould you like to see all the ratings in alphabetical order?\nPress A\nWould you like to add a new restaurant?\nPress N\nWould you like to Quit?\nPress Q")
    user_operation = input("Enter here: ")

    if user_operation.lower() == "a":
        get_ratings()
        print_ratings_alphabetical()
        main()
    elif user_operation.lower() == "n":
        judge_score()
        get_ratings()
        print_ratings_alphabetical()
        main()
    elif user_operation.lower() == "q":
        scores.close()
        return
    else:
        print("\nThat is not a valid command, please try again.")
        main()


main()