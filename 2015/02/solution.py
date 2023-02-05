"""Day 2: I Was Told There Would Be No Math

Problem:

First Part:

The elves are running low on wrapping paper, and so they need to submit an order
for more. They have a list of the dimensions (length l, width w, and height h)
of each present, and only want to order exactly as much as they need.

Fortunately, every present is a box (a perfect right rectangular prism), which
makes calculating the required wrapping paper for each gift a little easier:
find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l. The elves also
need a little extra paper for each present: the area of the smallest side.

For example:

- A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of
  wrapping paper plus 6 square feet of slack, for a total of 58 square feet.  

- A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square feet
  of wrapping paper plus 1 square foot of slack, for a total of 43 square feet.

All numbers in the elves' list are in feet. How many total square feet of
wrapping paper should they order?

Second Part:

The elves are also running low on ribbon. Ribbon is all the same width, so they
only have to worry about the length they need to order, which they would again
like to be exact.

The ribbon required to wrap a present is the shortest distance around its sides,
or the smallest perimeter of any one face. Each present also requires a bow made
out of ribbon as well; the feet of ribbon required for the perfect bow is equal
to the cubic feet of volume of the present. Don't ask how they tie the bow,
though; they'll never tell.

For example:

- A present with dimensions 2x3x4 requires 2+2+3+3 = 10 feet of ribbon to wrap
  the present plus 2*3*4 = 24 feet of ribbon for the bow, for a total of 34
  feet.

- A present with dimensions 1x1x10 requires 1+1+1+1 = 4 feet of ribbon to wrap
  the present plus 1*1*10 = 10 feet of ribbon for the bow, for a total of 14
  feet.

How many total feet of ribbon should they order?

"""


def get_paper_amount(length, width, height):
    """Determines the amount of wrapping paper needed for a present.

    Parameters
    ----------
    length : int
        The present's length.

    width : int
        The present's width.

    height : int
        The present's height.

    Returns
    -------
    amount : int
        The amount of wrapping paper needed for the present.

    """
    # Determine the main areas.
    base_area = length * width
    side_area = height * width
    face_area = length * height

    # Get the area of smallest size.
    smallest_area = min(base_area, side_area, face_area)

    # Determine the amount of wrapping paper needed.
    amount = (2 * base_area) + (2 * side_area) + (2 * face_area) + smallest_area

    return amount


def get_ribbon_amount(length, width, height):
    """Determines the amount of ribbon needed for a present.

    Parameters
    ----------
    length : int
        The present's length.

    width : int
        The present's width.

    height : int
        The present's height.

    Returns
    -------
    amount : int
        The amount of wrapping paper needed for the present.

    """
    # Get the two smallest components.
    small_A = 0
    small_B = 0
    if length <= width:
        small_A = length

        if width <= height:
            small_B = width
        else:
            small_B = height
    else:
        small_A = width

        if length <= height:
            small_B = length
        else:
            small_B = height

    # Determine the amount of ribbon needed for the wrap and ribbon.
    amount_wrap = (2 * small_A) + (2 * small_B)
    amount_bow = length * width * height

    amount_ribbon = amount_wrap + amount_bow

    return amount_ribbon


def parse_dimension(dimension):
    """Parses the current dimension string into its components.

    Parameters
    ----------
    dimension : string
        The dimension string with the following format: LxWxH.
        Where L, W, and H stand for length, width, height, respectively.

    Returns
    -------
    length : int
        The length component of the dimension.

    width : int
        The width component of the dimension.

    height : int
        The height component of the dimension.
    """
    # Split the dimension string into its components.
    l_str, w_str, h_str = dimension.split("x")

    # Cast each string into its integer representation.
    length = int(l_str)
    width = int(w_str)
    height = int(h_str)

    return length, width, height


def get_total_amount_paper(dimensions):
    """Determine the total amount of wrapping paper needed.

    Parameters
    ----------
    dimensions : list of string
        The list of dimensions of the wrapping paper needed for the presents.

    Returns
    -------
    total : int
        The total amount of wrapping paper needed.
    """
    total_amount = 0

    # Determine the total amount of wrapping paper needed.
    for dimension in dimensions:
        # Remove breaklines.
        dim = dimension.strip()

        # Get the components of the dimension.
        length, width, height = parse_dimension(dim)

        # Get the amount of wrapping paper needed for the current present.
        amount = get_paper_amount(length, width, height)

        # Add the current amount to the total.
        total_amount += amount

    return total_amount


def get_total_amount_ribbon(dimensions):
    """Determine the total amount of wrapping paper needed.

    Parameters
    ----------
    dimensions : list of string
        The list of dimensions of the wrapping paper needed for the presents.

    Returns
    -------
    total : int
        The total amount of wrapping paper needed.
    """
    total_amount = 0

    # Determine the total amount of wrapping paper needed.
    for dimension in dimensions:
        # Remove breaklines.
        dim = dimension.strip()

        # Get the components of the dimension.
        length, width, height = parse_dimension(dim)

        # Get the amount of wrapping paper needed for the current present.
        amount = get_ribbon_amount(length, width, height)

        # Add the current amount to the total.
        total_amount += amount

    return total_amount


if __name__ == "__main__":
    # Read the input file, and process its contents.
    input_file = open("input.txt", "r")
    inputs = input_file.readlines()

    print("--- First Part ---")
    total_paper = get_total_amount_paper(inputs)

    print("Total wrapping paper needed: ", total_paper)

    print("--- Second Part ---")
    total_ribbon = get_total_amount_ribbon(inputs)

    print("Total wrapping paper needed: ", total_ribbon)
