"""Day 5: Doesn't He Have Intern-Elves For This?

First Part:

Santa needs help figuring out which strings in his text file are naughty or
nice.

A nice string is one with all of the following properties:

- It contains at least three vowels (aeiou only), like aei, xazegov, or
  aeiouaeiouaeiou.

- It contains at least one letter that appears twice in a row, like xx, abcdde
  (dd), or aabbccdd (aa, bb, cc, or dd).

- It does not contain the strings ab, cd, pq, or xy, even if they are part of
  one of the other requirements.

For example:

- ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...),
  a double letter (...dd...), and none of the disallowed substrings.

- aaa is nice because it has at least three vowels and a double letter, even
  though the letters used by different rules overlap.

- jchzalrnumimnmhp is naughty because it has no double letter.

- haegwjzuvuyypxyu is naughty because it contains the string xy.

- dvszwmarrgswjxmb is naughty because it contains only one vowel.

How many strings are nice?

Second Part:

Realizing the error of his ways, Santa has switched to a better model of
determining whether a string is naughty or nice. None of the old rules apply, as
they are all clearly ridiculous.

Now, a nice string is one with all of the following properties:

- It contains a pair of any two letters that appears at least twice in the
  string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like
  aaa (aa, but it overlaps).

- It contains at least one letter which repeats with exactly one letter between
  them, like xyx, abcdefeghi (efe), or even aaa.

For example:

- qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a
  letter that repeats with exactly one letter between them (zxz).

- xxyxx is nice because it has a pair that appears twice and a letter that
  repeats with one between, even though the letters used by each rule overlap.

- uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a
  single letter between them.

- ieodomkazucvgmuy is naughty because it has a repeating letter with one between
  (odo), but no pair that appears twice.

How many strings are nice under these new rules?
"""


def is_nice_string_first_rules(s):
    """Return whether a string is nice or not following the first rules.

    Parameters
    ----------
    s : string
        The string to check.

    Returns
    -------
    is_nice : boolean
        The boolean that indicates if the string is nice or not.
    """
    # Get the length if the string.
    n = len(s)

    # Define the forbidden sub-strings.
    forbidden_substrings = {"ab", "cd", "pq", "xy"}

    # Keep a counter for vowels and the letters that appear twice in a row.
    vowels = 0
    twice = 0

    # Traverse each character in the string in search of the conditions.
    for i in range(n):
        if s[i] in {"a", "e", "i", "o", "u"}:
            vowels += 1

        if i < n - 1:
            if s[i] == s[i + 1]:
                twice += 1

            # Temporal string to check if its forbidden.
            temp = s[i] + s[i + 1]
            if temp in forbidden_substrings:
                return False

    # Check that the string satisfies the conditions.
    return (vowels >= 3) and (twice > 0)


def is_nice_string_second_rules(s):
    """Return whether a string is nice or not following the second rules.

    Parameters
    ----------
    s : string
        The string to check.

    Returns
    -------
    is_nice : boolean
        The boolean that indicates if the string is nice or not.
    """
    # Get the length if the string.
    n = len(s)

    # Pairs of letters found on the string.
    pairs = set()

    # Boolean to check if the string has two pair of letters that repeat in the
    # string and do not overlap.
    first_condition = False

    # Boolean to check if the string contains a letter which repeats with
    # exactly one letter between them.
    second_condition = False

    # Traverse each character in the string in search of the conditions.
    for i in range(n):
        if i < n - 1:
            # Temporal string to add it to the set of pairs.
            temp = s[i] + s[i + 1]

            # If the pair was already in the set, then the first condition is
            # true.
            if temp in pairs:
                first_condition = True
            else:
                pairs.add(temp)

        if i < n - 2:
            # Check that the previous pair does not overlap.
            if s[i] == s[i + 1] and s[i + 1] == s[i + 2]:
                return False

            # Check for the second condition.
            if s[i] == s[i + 2]:
                second_condition = True

    # Check that the string satisfies the conditions.
    return first_condition and second_condition


def count_nice_strings(ls, second_rule):
    """Counts the number of nice strings in a list.

    Parameters
    ----------
    ls : list of strings
        The list of strings.

    second_rule : boolean
        Boolean that indicates if the second rules must be followed.

    Returns
    -------
    num_nice : int
        the number of nice strings in the list.
    """
    # Counter for the number of nice strings.
    num_nice = 0

    # Traverse the list and count the number of nice strings.
    for string in ls:
        # Remove the breakline.
        s = string.strip()

        if second_rule:
            if is_nice_string_second_rules(s):
                num_nice += 1
        else:
            if is_nice_string_first_rules(s):
                num_nice += 1

    return num_nice


if __name__ == "__main__":
    # Read the input file, and process its contents.
    input_file = open("input.txt", "r")
    inputs = input_file.readlines()

    print("--- First Part ---")
    num_nice_strings = count_nice_strings(inputs, False)
    print("Number of nice strings:", num_nice_strings)

    print("--- Second Part ---")
    num_nice_strings = count_nice_strings(inputs, True)
    print("Number of nice strings:", num_nice_strings)
