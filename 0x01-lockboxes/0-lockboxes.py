#!/usr/bin/python3
"""
Module for canUnlockAll method
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    :param boxes: List of lists containing keys for boxes
    :return: True if all boxes can be opened, else False
    """
    n = len(boxes)
    opened = [False] * n
    opened[0] = True
    stack = [0]

    while stack:
        box = stack.pop()
        for key in boxes[box]:
            if key < n and not opened[key]:
                opened[key] = True
                stack.append(key)

    return all(opened)
