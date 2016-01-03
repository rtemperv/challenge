

def from_base_to_decimal(s, base):

    convert_sequence = "0123456789ABCDEFGHIJ"

    reversed_string = reversed(s.upper())

    total = 0

    for position, character in enumerate(reversed_string):
        index = convert_sequence.index(character)

        if index == -1 or (base - 1) < index:
            raise RuntimeError('blaat')

        total += (base ** position) * index

    return total


def from_decimal_to_base(i, base):
    total = ""

    convert_sequence = "0123456789ABCDEFGHIJ"

    while i != 0:
        remainder = int(i % base)
        i //= base
        total += convert_sequence[remainder]

    return total[::-1]

