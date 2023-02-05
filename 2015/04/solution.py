"""Day 4: The Ideal Stocking Stuffer

First Part:

Santa needs help mining some AdventCoins (very similar to bitcoins) to use as
gifts for all the economically forward-thinking little girls and boys.

To do this, he needs to find MD5 hashes which, in hexadecimal, start with at
least five zeroes. The input to the MD5 hash is some secret key (your puzzle
input, given below) followed by a number in decimal. To mine AdventCoins, you
must find Santa the lowest positive number (no leading zeroes: 1, 2, 3, ...)
that produces such a hash.

For example:

- If your secret key is abcdef, the answer is 609043, because the MD5 hash of
  abcdef609043 starts with five zeroes (000001dbbfa...), and it is the lowest
  such number to do so.

- If your secret key is pqrstuv, the lowest number it combines with to make an
  MD5 hash starting with five zeroes is 1048970; that is, the MD5 hash of
  pqrstuv1048970 looks like 000006136ef....

Second Part:

Now find one that starts with six zeroes.

"""
import hashlib


def find_key_value(key_str, k):
    """Finds the value for which the hash has k leading zeroes in the hash.

    Parameters
    ----------
    key_str : str
        The key string.

    k : int
        The amount of leading zeroes the hash must have.

    Returns
    -------
    value : int
        The value that, when combined with the key and hashed with MD5, produces
        a hash with k leading zeroes.
    """
    # Traverse all the natural numbers to find the desired value.
    i = 1
    while True:
        # Build the key with the value.
        key = key_str + str(i)

        # Get the MD5 hash of the key.
        h = hashlib.md5(bytes(key, "utf-8")).hexdigest()

        # Check if the first k bytes of the hash are zero.
        are_zeros = True
        for j in range(k):
            are_zeros = are_zeros and h[j] == "0"

        # If the first k bytes are zero, return the value, otherwise check
        # for the next natural.
        if are_zeros:
            return i
        else:
            i += 1


if __name__ == "__main__":
    # Read the input file, and process its contents.
    input_file = open("input.txt", "r")
    inputs = input_file.readlines()

    print("--- First Part ---")
    for i in inputs:
        # Remove breakline.
        key = i.strip()

        # Determine the desired value.
        value = find_key_value(key, 5)

        print("Desired value:", value)

    print("--- Second Part ---")
    for i in inputs:
        # Remove breakline.
        key = i.strip()

        # Determine the desired value.
        value = find_key_value(key, 6)

        print("Desired value:", value)
