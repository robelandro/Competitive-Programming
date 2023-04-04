#!/usr/bin/env python3
"""Domino piling"""


def domino_pilling(length: int, width: int) -> int:
    """Calculate the number of dominoes that can be placed on the board
    :param length: length of the board
    :param width: width of the board
    :return: number of dominoes that can be placed on the board
    """
    value = 0

    while length > 1 and width > 1:
        value += (length // 2) * width
        length, width = width, length % 2

    return value + (length * width) // 2


if __name__ == '__main__':
    length, width = map(int, input().split())
    print(domino_pilling(length, width))
