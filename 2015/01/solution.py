"""Day 1: Not Quite Lisp.

Problem:

First Part:

Santa is trying to deliver presents in a large apartment building, but he can't
find the right floor - the directions he got are a little confusing. He starts
on the ground floor (floor 0) and then follows the instructions one character at
a time.

An opening parenthesis, (, means he should go up one floor, and a closing
parenthesis, ), means he should go down one floor.

The apartment building is very tall, and the basement is very deep; he will
never find the top or bottom floors.

For example:

- (()) and ()() both result in floor 0.
- ((( and (()(()( both result in floor 3.
- ))((((( also results in floor 3.
- ()) and ))( both result in floor -1 (the first basement level).
- ))) and )())()) both result in floor -3.

To what floor do the instructions take Santa?

Second Part:

Now, given the same instructions, find the position of the first character that
causes him to enter the basement (floor -1). The first character in the
instructions has position 1, the second character has position 2, and so on.

For example:

- ) causes him to enter the basement at character position 1.
- ()()) causes him to enter the basement at character position 5.

What is the position of the character that causes Santa to first enter the
basement?

"""


def get_floor(instruction_str):
    """Returns the floor Santa must get to.

    Parameters
    ----------
    instruction_str : string
        The instructions that determine to which floor Santa must go.

    Return
    ------
    floor : int or None
        The floor Santa must go, or None if an invalid character was found on
        the instructions.
    """
    # Current floor.
    floor = 0

    # If the instruction is empty, return the current floor.
    if len(instruction_str) == 0:
        return floor

    # Otherwise, traverse each character in the string and move accordingly.
    for c in instruction_str:
        if c == "(":
            floor += 1
        elif c == ")":
            floor -= 1
        else:
            # If you find a char different from "(" or ")", return None.
            return None

    # When finished following the instructions, return the current floor.
    return floor


def get_basement_position(instruction_str):
    """Returns the first char index that moves Santa to the basement.

    Parameters
    ----------
    instruction_str : string
        The instructions that determine to which floor Santa must go.

    Return
    ------
    index : int or None
        The first char index that moves Santa to the basement, 0 if Santa
        never entered the basement, or None an invalid character was found.
    """
    # Current floor.
    floor = 0

    # If the instruction is empty, return None as Santa isn't in the basement.
    if len(instruction_str) == 0:
        return floor

    # Otherwise, traverse each character in the string and move accordingly.
    # Keep track of the current index, start at 1.
    index = 1
    for c in instruction_str:
        if c == "(":
            floor += 1
        elif c == ")":
            floor -= 1
        else:
            return None

        # If the current floor is below the 0-th floor, return the index,
        # otherwise move to the next index.
        if floor < 0:
            return index
        else:
            index += 1

    # If Santa never entered the basement, return 0.
    return 0


if __name__ == "__main__":
    # Read the input file, and process each line.
    input_file = open("input.txt", "r")
    inputs = input_file.readlines()

    # First part of the puzzle.
    print("--- First Part ---")

    for i in inputs:
        # Remove the stripline.
        instruction = i.strip()

        floor = get_floor(instruction)

        if floor is not None:
            print("Floor: ", floor)
        else:
            print("Floor: Invalid input")

    # First part of the puzzle.
    print("--- Second Part ---")

    for i in inputs:
        # Remove the stripline.
        instruction = i.strip()

        pos = get_basement_position(instruction)

        if pos > 0:
            print("Position: ", pos)
        elif pos == 0:
            print("Position: Santa never entered the basement.")
        else:
            print("Position: Invalid input")
