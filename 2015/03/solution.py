"""Day 3: Perfectly Spherical Houses in a Vacuum.

First Part:

Santa is delivering presents to an infinite two-dimensional grid of houses.

He begins by delivering a present to the house at his starting location, and
then an elf at the North Pole calls him via radio and tells him where to move
next. Moves are always exactly one house to the north (^), south (v), east (>),
or west (<). After each move, he delivers another present to the house at his
new location.

However, the elf back at the north pole has had a little too much eggnog, and so
his directions are a little off, and Santa ends up visiting some houses more
than once. How many houses receive at least one present?

For example:

- > delivers presents to 2 houses: one at the starting location, and one to
      the east.

- ^>v< delivers presents to 4 houses in a square, including twice to the house
  at his starting/ending location.

- ^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2
  houses.

Second Part:

The next year, to speed up the process, Santa creates a robot version of
himself, Robo-Santa, to deliver presents with him.

Santa and Robo-Santa start at the same location (delivering two presents to the
same starting house), then take turns moving based on instructions from the elf,
who is eggnoggedly reading from the same script as the previous year.

This year, how many houses receive at least one present?

For example:

- ^v delivers presents to 3 houses, because Santa goes north, and then
  Robo-Santa goes south.

- ^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back
  where they started.

- ^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction
  and Robo-Santa going the other.

"""


def determine_visited_houses(instruction_str):
    """Determines the amount of visited houses given the instructions.

    Parameters
    ----------
    instruction_str : str
        The instructions that indicate to which direction Santa must move.

    Returns
    -------
    num_visited_houses : int or None
        The amount of houses Santa has been to, or None if an invalid
        instruction is found.
    """
    # Current (X, Y) position Santa has.
    X = 0
    Y = 0

    # The X and Y coordinates Santa has travelled.
    visited_coordinates = {(0, 0)}

    # Follow the instructions and move accordingly.
    for c in instruction_str:
        if c == "^":
            Y += 1
        elif c == "v":
            Y -= 1
        elif c == ">":
            X += 1
        elif c == "<":
            X -= 1
        else:
            return None

        # Append the current coordinate to the visited coordinates.
        visited_coordinates.add((X, Y))

    # Return the amount of different houses Santa has been to.
    num_visited_houses = len(visited_coordinates)
    return num_visited_houses


def determine_visited_houses_with_robot(instruction_str):
    """Determines the amount of visited houses by Santa and its robot.

    Parameters
    ----------
    instruction_str : str
        The instructions that indicate to which direction Santa must move.

    Returns
    -------
    num_visited_houses : int or None
        The amount of houses Santa and the robot has been to, or None if an
        invalid instruction is found.
    """
    # Current (X, Y) position Santa and Robo-Santa have.
    X_santa = 0
    Y_santa = 0
    X_robot = 0
    Y_robot = 0

    # The X and Y coordinates Santa has travelled.
    visited_coordinates = {(0, 0)}

    # Follow the instructions and move accordingly.
    # Keep track of the current index.
    i = 0
    for c in instruction_str:
        # If the current index is even, then Santa moves, otherwise the robot
        # moves.
        if c == "^":
            if i % 2 == 0:
                Y_santa += 1
            else:
                Y_robot += 1

        elif c == "v":
            if i % 2 == 0:
                Y_santa -= 1
            else:
                Y_robot -= 1

        elif c == ">":
            if i % 2 == 0:
                X_santa += 1
            else:
                X_robot += 1

        elif c == "<":
            if i % 2 == 0:
                X_santa -= 1
            else:
                X_robot -= 1

        else:
            return None

        # Append the current coordinate to the visited coordinates.
        if i % 2 == 0:
            visited_coordinates.add((X_santa, Y_santa))
        else:
            visited_coordinates.add((X_robot, Y_robot))

        # Move the index.
        i += 1

    # Return the amount of different houses Santa has been to.
    num_visited_houses = len(visited_coordinates)
    return num_visited_houses


if __name__ == "__main__":
    # Read the input file, and process its contents.
    input_file = open("input.txt", "r")
    inputs = input_file.readlines()

    print("--- First Part ---")
    for i in inputs:
        # Remove breakline.
        instruction_str = i.strip()

        # Determine the amount of visited houses.
        num_houses = determine_visited_houses(instruction_str)

        print("Visited Houses:", num_houses)

    print("--- Second Part ---")
    for i in inputs:
        # Remove breakline.
        instruction_str = i.strip()

        # Determine the amount of visited houses.
        num_houses_w_robot = determine_visited_houses_with_robot(instruction_str)

        print("Visited Houses with Robo-Santa:", num_houses_w_robot)
