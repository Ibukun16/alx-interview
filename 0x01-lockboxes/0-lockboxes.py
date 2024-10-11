#!/usr/bin/python3
"""function that solves the 'canUnlockAll' challenge"""


def canUnlockAll(boxes):
    """
    The function checks if all the boxes in a list of boxes
    containing the keys (indices) to other boxes can be
    unlocked given that the first box is unlocked.
    If all boxes can be unlock return 'True' else return 'False'.
    """
    n = len(boxes)
    open_boxes = set()
    stack = [0]

    if (type(boxes) is not list):
        return False

    if (n == 0):
        return False

    while stack:
        cur_box = stack.pop()

        if (cur_box in open_boxes):
            continue
        open_boxes.add(cur_box)

        for key in boxes[cur_box]:
            if (key < n and key not in open_boxes):
                stack.append(key)
    return len(open_boxes) == n
