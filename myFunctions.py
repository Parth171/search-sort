
"""
title: This is useful functions for testing algorithms
author: Parth Sakpal
date-created: 9/14/2023
"""

import random, statistics, time

def getSortedList(SIZE):
    '''
    returns a sorted list of approximately size SIZE
    :param SIZE: int
    :return: list (int)
    '''

    NUMBERS = []

    for i in range(2 * SIZE):
        if random.randrange(2) == 1:
            NUMBERS.append(i)

    return NUMBERS


def getRandomList(SIZE):
    '''
    returning a randomized list of apporoximately size SIZE
    :param SIZE: int
    :return: list(int)
    '''

    NUMBERS = getSortedList(SIZE)

    random.shuffle(NUMBERS)

    return NUMBERS


def getAverage(LIST):
    '''
    returns an average of the given list
    :param LIST: list(int)
    :return: float
    '''

    return statistics.mean(LIST)


def getTime():
    '''
    return perf_counter()
    :return:
    '''

    return time.perf_counter()




if __name__ == "__main__":
    NUM = getRandomList(10)
    print(getAverage([3, 4, 5]))
    print(getTime())
    print(NUM)