def click(pos):
    """
    :return: pos (x, y) in range 0-11 0-11
    """
    rect = (0, 0, 1000, 1000)
    delta = 1000/12.0

    y_pos = pos[1]
    x_pos = pos[0]
    top = False
    if rect[0] < x_pos < rect[0] + rect[2]:
        if rect[1] < y_pos < rect[1] + rect[3]:
            divX = x_pos - rect[0]
            divY = y_pos - rect[1]
            x = int(divX / delta)
            y = int(divY / delta)
            if y_pos < x_pos + delta * (y_pos - x_pos + 1):
                top = True

            return x, y, top

    return -1, -1, False


def move_string(space_from, space_to, fly=False, land = False, promote=False):
    if fly:
        return "" + str(space_from[0]) + ", " + str(space_from[1])
    elif land:
        return "" + str(space_to[0]) + ", " + str(space_to[1])
    elif promote:
        pass
    else:
        return "" + str(space_from[0]) + ", " + str(space_from[1]) + ", " + str(space_to[0]) + ", " + str(space_to[1])
