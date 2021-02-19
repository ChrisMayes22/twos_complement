# Chris Mayes
# Last updated 2/18/2021
# Function that accepts two arguments and returns the 2s complement of those numbers

def ones_complement(num: str):
    """
    Returns ones complement for a passed binary string.

    :param num: str, represents a binary number. Non-bit characters are ignored.
    :return: str, represents a binary number, or "" if no bits are in num.
    """

    template = ""

    for char in num:
        if char == "0":
            template += "1"
        else:
            template += "0"

    #  TODO: Add error check for |template| <= 0

    return template


def pad_number(num: str, sign_flag: int):
    """
    Applies padding to passed binary string so that # of bits
    are a multiple of 4

    :param num: binary string
    :param sign_flag: 1 for negative, 0 for positive. Used for padding
    :return: binary string
    """

    #  TODO: Add error checking for 0 <= sign_flag <= 1

    padding = str(sign_flag)

    while len(num) % 4 != 0:
        num = padding + num

    return num


def twos_complement(num: int, sign_flag: int):
    """
    Returns the twos complement binary string for a passed int

    :param num: Int
    :param sign_flag: 1 = negative, 0 = false
    :return: Str, represents a binary number
    """

    #  TODO: Add error checking for 0 <= sign_flag <= 1

    num = pad_number(bin(num)[2:], sign_flag)
    num = ones_complement(num)  # Slice off "0b" prefix
    num = int(pad_number(num, sign_flag), 2) + 1

    return pad_number(bin(num)[2:], sign_flag)


print("NUM AFTER:", twos_complement(56, 0))

