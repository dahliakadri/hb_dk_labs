"""Restaurant rating lister."""


def get_restaurant_ratings(ratings_file):
    """Restaurant rating lister."""
    # open a file
    ratings_dict = {}
    ratings = open(ratings_file)
    # remove extra space from the file
    for line in ratings:
        line = line.rstrip()
        restaurant, rating = line.split(":")
        ratings_dict[restaurant] = rating

    return ratings_dict


def get_user_restaurant_ratings(ratings_dict):
    """Gets user restaurant name and raiting and adds it to restaurant
    dictionary"""

    # get user input for restaurant name and rating
    print("Please share a restaraunt name.")
    user_restaurant_name = input(">")
    user_restaurant_name = user_restaurant_name.title()

    while True:
        print("Please share the corresponding restaurant rating.")
        user_restaurant_rating = input(">")

        if int(user_restaurant_rating) > 5:
            print("Invalid rating. Ratings should be integers, 1-5.")
        elif int(user_restaurant_rating) < 1:
            print("Invalid rating. Ratings should be integers, 1-5.")
        else:
            break

    ratings_dict[user_restaurant_name] = user_restaurant_rating

    return ratings_dict


def list_sorted_restaurant_ratings(final_ratings_dict):
    # use .tems to return a list of tuples, sort it, and then print ot the list
    for restaurant, rating in sorted(final_ratings_dict.items()):
        print(f"{restaurant} is rated at {rating}.")

def give_user_choices():

    ratings_dict = get_restaurant_ratings("scores.txt")

    while True:
        print("Below is a list of choices for you on restaurants")
        print("[1] - See all restaurant ratings in alphabetical order")
        print("[2] - Add a new restaurant and rating")
        print("[3] - Quit")
        user_input = int(input("Type 1, 2 or 3 to choose: "))

        if user_input == 1:
            list_sorted_restaurant_ratings(ratings_dict)
        elif user_input == 2:
            ratings_dict = get_user_restaurant_ratings(ratings_dict)
        elif user_input == 3:
            print("Quitting...")
            break


give_user_choices()
