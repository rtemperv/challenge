# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class BichromePainting:

    def isThatPossible(self, board, k):

        size = len(board)

        board = [list(row) for row in board]

        if k > size:
            return -1

        changes = True

        while changes:
            changes = False
            for i in range(size - k + 1):
                for j in range(size - k + 1):
                    w = b = 0
                    for x in range(k):
                        for y in range(k):
                            if board[j + y][i + x] == 'W':
                                w += 1
                            if board[j + y][i + x] == 'B':
                                b += 1
                    if w and b: continue
                    if not w and not b: continue

                    changes = True
                    for x in range(k):
                        for y in range(k):
                            board[j + y][i + x] = '?'

        return 'Possible' if all([board[y][x] == '?' for x in range(size) for y in range(size)]) else 'Impossible'





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

def do_test(board, k, __expected):
    startTime = time.time()
    instance = BichromePainting()
    exception = None
    try:
        __result = instance.isThatPossible(board, k);
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
    sys.stdout.write("BichromePainting (250 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("BichromePainting.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            board = []
            for i in range(0, int(f.readline())):
                board.append(f.readline().rstrip())
            board = tuple(board)
            k = int(f.readline().rstrip())
            f.readline()
            __answer = f.readline().rstrip()

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(board, k, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1454700741
    PT, TT = (T / 60.0, 75.0)
    points = 250 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
