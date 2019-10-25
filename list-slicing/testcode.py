def custom_reverse(input_list):
    """Reverse the elements of the input_list.

    Like input_list.reverse(), custom_reverse(input_list) should reverse the
    elements of the original list and return nothing (we call this reversing
    "in place").

    For example:

        >>> multiples = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
        >>> custom_reverse(multiples)
        >>> multiples == [27, 24, 21, 18, 15, 12, 9, 6, 3, 0]
        True

    """
    copy_input_list = []

    copy_input_list[:] = input_list[:]

    index_input = 0
    index_copy = 1
    for item in input_list:
        input_list[index_input] = copy_input_list[-index_copy]
        index_input += 1
        index_copy += 1

    return input_list

multiples = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]

print(custom_reverse(multiples))