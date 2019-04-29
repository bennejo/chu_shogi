def click(pos):
    """
    :return: pos (x, y) in range 0-11 0-11
    """
    rect = (0, 0, 1000, 1000)

    x = pos[0]
    y = pos[1]
    if rect[0] < x < rect[0] + rect[2]:
        if rect[1] < y < rect[1] + rect[3]:
            divX = x - rect[0]
            divY = y - rect[1]
            j = int(divX / (rect[2]/12))
            i = int(divY / (rect[3]/12))
            return i, j

    return -1, -1


def move_string(space_from, space_to):
    return "" + str(space_from[0]) + ", " + str(space_from[1]) + ", " + str(space_to[0]) + ", " + str(space_to[1])