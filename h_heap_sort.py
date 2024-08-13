"""
title: Heap sort
author: Parth Sakpal
date-created: 10/5/2023
"""


def heapify(LIST, LEN_ARRAY, ROOT_INDEX):
    """
    this moves the highest value to index 0
    :param LIST: list (int)
    :param LEN_ARRAY: int
    :param ROOT_INDEX: int
    :return:
    """

    LARGEST_INDEX = ROOT_INDEX

    LEFT_INDEX = 2 * ROOT_INDEX + 1
    RIGHT_INDEX = 2 * ROOT_INDEX + 2

    # CHECK IF LEFT CHILD IS GREATER THAN PARENT

    if LEFT_INDEX < LEN_ARRAY and LIST[ROOT_INDEX] < LIST[LEFT_INDEX]:
        LARGEST_INDEX = LEFT_INDEX

    # CHECK IF THE RIGHT CHILD IS GREATER THAN PARENT/LEFT INDEX

    if RIGHT_INDEX < LEN_ARRAY and LIST[LARGEST_INDEX] < LIST[RIGHT_INDEX]:
        LARGEST_INDEX = RIGHT_INDEX

    # CHANGE THE ROOT AND PARENT IF NEED WITH CHILD INDEX

    if LARGEST_INDEX != ROOT_INDEX:
        TEMP = LIST[ROOT_INDEX]
        LIST[ROOT_INDEX] = LIST[LARGEST_INDEX]
        LIST[LARGEST_INDEX] = TEMP

        heapify(LIST, LEN_ARRAY, LARGEST_INDEX)



def heapSort(LIST):
    """
    sorts the array using a binary tree
    :param LIST: list (int)
    :return: None
    """

    # build a max heap (highest number is at the top of each tree)

    LEN_ARRAY = len(LIST)



    for i in range(LEN_ARRAY, -1, -1):
        heapify(LIST, LEN_ARRAY, i)

    # extract the highest element
    for i in range(LEN_ARRAY-1, 0, -1):
        TEMP = LIST[0]
        LIST[0] = LIST[i]
        LIST[i] = TEMP

        heapify(LIST, i, 0)


if __name__ == "__main__":

    from myFunctions import *

    TIMES = []

    for i in range(30):

        NUMBERS = getRandomList(10000)
        START_TIME = getTime()
        heapSort(NUMBERS)
        END_TIME = getTime()
        TIMES.append(END_TIME-START_TIME)
        print(i)

    print(getAverage(TIMES))




