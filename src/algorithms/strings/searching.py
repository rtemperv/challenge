def knuth_morris_pratt(word: str, text: str) -> int:
    """
    Finds if the word is contained in the text
    Time complexity: O(m+n)
    """

    # Build partial match table (previous index to fall back to when there is no match)
    index = 2
    current_pos = 0
    partial_match = [None] * len(word)
    partial_match[0] = -1
    partial_match[1] = 0

    while index < len(word):
        if word[index-1] == word[current_pos]:
            partial_match[index] = current_pos + 1
            index += 1
            current_pos += 1

        elif current_pos > 0:
            current_pos = partial_match[current_pos]

        else:
            partial_match[index] = 0
            index += 1

    # Iterate over the corpus
    current_pos = 0
    index = 0

    while index < len(text) and current_pos < len(word):
        if text[index] == word[current_pos]:
            index += 1
            current_pos += 1
        else:
            if partial_match[current_pos] > -1:
                current_pos = partial_match[current_pos]
            else:
                current_pos = 0
                index += 1


    # We found a match
    if len(word) == current_pos:
        return index - len(word)

    return -1
