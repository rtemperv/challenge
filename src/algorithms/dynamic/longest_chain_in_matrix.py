
def find_longest_chain_in_matrix(matrix, n):

    longest_from_here = [[0 for _ in range(n)] for _ in range(n)]

    def recurse(i , j):

        if longest_from_here[i][j] > 0:
            return longest_from_here[i][j]

        longest = 1

        for x in (-1, 0, 1):
            for y in (-1, 0, 1):

                if x == 0 and y == 0:
                    continue

                if x + j >= n or x + j < 0 or y + i >= n or y + i < 0:
                    continue

                if matrix[y + i][x + j] > matrix[i][j]:
                    result = recurse(y + i, x + j)
                    longest = max(longest, result + 1)
        longest_from_here[i][j] = longest
        return longest

    return max((recurse(i, j) for i in range(n) for j in range(n)))

