"""Restaurant rating lister."""


def restaurant_ratings(filename):
    """Takes in a file with restaurant names & ratings
    stores them in alphabetical order in a dictionary"""

    restaurant_ratings_dict = {}
    scores_file = open(filename)
    for line in scores_file:
        line = line.rstrip()

        name_score = line.split(":")
        name = name_score[0]
        score = name_score[1]

        restaurant_ratings_dict[name] = score

    restaurant_ratings_list = sorted(restaurant_ratings_dict.items())
    
    for rest_tup in restaurant_ratings_list:
        name_tup = rest_tup[0]
        score_tup = rest_tup[1]
        print(f"{name_tup} is rated at {score_tup}.")

    return 


restaurant_ratings("scores.txt")


# put your code here
