
"""
title: Bubble Sort
author: Parth Sakpal
date-created:
"""

from random import randrange
from time import perf_counter
from statistics import mean

def createArray(SIZE):
    """
    create a random amount of numbers
    :param SIZE: INT
    :return: list
    """

    NUMBERS = []

    for i in range(2*SIZE):
        if randrange(2) == 1:
            NUMBERS.append(i)
    return NUMBERS


def binarySearch(LIST, VALUE):
    """
    searches for a value within a LIST
    :param LIST: list (int)
    :param VALUE: int
    :return: bool
    """

    START_INDEX = 0
    END_INDEX = len(LIST) - 1

    while START_INDEX <= END_INDEX:
        #print(LIST[START_INDEX:END_INDEX]+1)
        MIDPOINT_INDEX = (START_INDEX + END_INDEX) // 2
        if LIST[MIDPOINT_INDEX] == VALUE:
            return True
        elif LIST[MIDPOINT_INDEX] < VALUE:
            START_INDEX = MIDPOINT_INDEX + 1
        else:
            END_INDEX = MIDPOINT_INDEX - 1

    return False




if __name__ == "__main__":
    NUMBERS = createArray(10000000)
    TIMES = []

    for i in range(30):

        NUM = NUMBERS[randrange(len(NUMBERS))]

        START_TIME =perf_counter()
        FOUND = binarySearch(NUMBERS, NUM)
        END_TIME = perf_counter()
        TIMES.append(END_TIME-START_TIME)
    print(mean(TIMES))





    print(FOUND)


