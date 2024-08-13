"""
title: Merge sort example
author: Parth Sakpal
date-created: 9/27/2023
"""

def mergeSortedLists(LIST_LEFT, LIST_RIGHT):
    """
    Merges two sorted lists together
    :param LIST_LEFT: int
    :param LIST_RIGHT: int
    :return: list - sorted list
    """

    # special case

    if len(LIST_LEFT) == 0:
        return LIST_RIGHT
    elif len(LIST_RIGHT) == 0:
        return LIST_LEFT

    # general case

    INDEX_LEFT = 0
    INDEX_RIGHT = 0

    LIST_MERGE = []

    LIST_LEN_TOTAL = len(LIST_LEFT) + len(LIST_RIGHT)

    while len(LIST_MERGE) < LIST_LEN_TOTAL:
        if LIST_LEFT[INDEX_LEFT] <= LIST_RIGHT[INDEX_RIGHT]:
            LIST_MERGE.append(LIST_LEFT[INDEX_LEFT])
            INDEX_LEFT = INDEX_LEFT + 1

        else:
            LIST_MERGE.append(LIST_RIGHT[INDEX_RIGHT])
            INDEX_RIGHT = INDEX_RIGHT + 1


        # optimization

        if INDEX_RIGHT == len(LIST_RIGHT):
            LIST_MERGE = LIST_MERGE + LIST_LEFT[INDEX_LEFT:]
            break

        elif INDEX_LEFT == len(LIST_LEFT):
            LIST_MERGE = LIST_MERGE + LIST_RIGHT[INDEX_RIGHT:]
            break


    return LIST_MERGE



def mergeSort(LIST):
    """
    performs the recursive split of list
    :param LIST: list
    :return: list - sorted
    """


    if len(LIST) <= 1: # base case
        return LIST

    else:

        MIDPOINT = len(LIST) // 2
        LEFT = LIST[:MIDPOINT]
        RIGHT = LIST[MIDPOINT:]


        return mergeSortedLists(mergeSort(LEFT), mergeSort(RIGHT))



if __name__ == "__main__":
    from myFunctions import *

    TIME = []

    for i in range(30):


        NUMBERS = getRandomList(10000)
        START_TIME = getTime()
        NUMBERS = mergeSort(NUMBERS)
        END_TIME = getTime()
        TIME.append(END_TIME - START_TIME)
        print(i)
    print(getAverage(TIME))
