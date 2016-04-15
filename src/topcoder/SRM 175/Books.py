# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect
from src.algorithms.dynamic.longest_increasing_subsequence import longest_increasing_subsequence


class Books:
    def sortMoves(self, titles):

        return len(titles) - len(longest_increasing_subsequence(titles))

    def longest_increasing_subsequzence(self, items):
        """
        Finds the longest increasing subsequence
        """

        if len(items) <= 1:
            return items

        predecessors = [None] * len(items)
        longest_subsequence = [None] * len(items)
        longest_lenght = 1

        longest_subsequence[0] = 0

        for index in range(1, len(items)):

            item = items[index]
            best_predecessor_index = None

            for position, j in enumerate(longest_subsequence):
                if j is not None and items[j] <= item:
                    best_predecessor_index = position

            if best_predecessor_index is not None:
                predecessors[index] = longest_subsequence[best_predecessor_index]

                longest_lenght = max(longest_lenght, best_predecessor_index + 1)

            current_tail_index = longest_subsequence[best_predecessor_index] if best_predecessor_index else 0
            current_tail = items[current_tail_index] if current_tail_index else None
            if current_tail is None or current_tail > item:
                longest_subsequence[best_predecessor_index + 1] = index

        longest_list = []
        current_index = longest_subsequence[longest_lenght - 1]

        while True:
            longest_list.append(items[current_index])
            current_index = predecessors[current_index]
            if current_index is None:
                break

        return longest_list


# CUT begin
# TEST CODE FOR PYTHON {{{
import sys, time, math

def tc_equal(expected, received):
    try:
        _t = type(expected)
        received = _t(received)
        if _t == list or _t == tuple:
            if len(expected) != len(received): return False
            return all(tc_equal(e, r) for (e, r) in zip(expected, received))
        elif _t == float:
            eps = 1e-9
            d = abs(received - expected)
            return not math.isnan(received) and not math.isnan(expected) and d <= eps * max(1.0, abs(expected))
        else:
            return expected == received
    except:
        return False

def pretty_str(x):
    if type(x) == str:
        return '"%s"' % x
    elif type(x) == tuple:
        return '(%s)' % (','.join( (pretty_str(y) for y in x) ) )
    else:
        return str(x)

def do_test(titles, __expected):
    startTime = time.time()
    instance = Books()
    exception = None
    try:
        __result = instance.sortMoves(titles);
    except:
        import traceback
        exception = traceback.format_exc()
    elapsed = time.time() - startTime   # in sec

    if exception is not None:
        sys.stdout.write("RUNTIME ERROR: \n")
        sys.stdout.write(exception + "\n")
        return 0

    if tc_equal(__expected, __result):
        sys.stdout.write("PASSED! " + ("(%.3f seconds)" % elapsed) + "\n")
        return 1
    else:
        sys.stdout.write("FAILED! " + ("(%.3f seconds)" % elapsed) + "\n")
        sys.stdout.write("           Expected: " + pretty_str(__expected) + "\n")
        sys.stdout.write("           Received: " + pretty_str(__result) + "\n")
        return 0

def run_tests():
    sys.stdout.write("Books (450 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("Books.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            titles = []
            for i in range(0, int(f.readline())):
                titles.append(f.readline().rstrip())
            titles = tuple(titles)
            f.readline()
            __answer = int(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(titles, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1458314632
    PT, TT = (T / 60.0, 75.0)
    points = 450 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
