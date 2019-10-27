# put your code here.


def word_count(filename):

    """takes in a text file and counts the number of times each word appears
    in the file"""

    # open a file
    file_data = open(filename)

    # create an empyt dictionary
    text_word_count = {}
    # loop through the file
    for line in file_data:
        # strips blank space from right side of file
        line = line.rstrip()
        # clear spacing on each line and then seperate each word by spaces to
        # create a list of words
        words = line.split(" ")

        for word in words:

            # assign value to the key 'word'
            # check to see if word is in dictionary
            # at key 'word' setting a value of 0 if not yet in the dictionary,
            # otherwise incrementing by 1
            text_word_count[word] = text_word_count.get(word, 0) + 1

    # for each key, value pair creating a list of tupples and then looping over
    # the list to print up the tuple
    for word, count in text_word_count.items():
        print(word, count)

    return


word_count("test.txt")
