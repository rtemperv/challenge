# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class BombSweeper:
    def winPercentage(self, board):
        status_board = [self.status_square(board, x, y) for x in range(len(board[0])) for y in range(len(board))]

        bomb_squares = len(list(filter(lambda x: x == -1, status_board)))
        ok_squares = len(list(filter(lambda x: x == 1, status_board)))

        return ok_squares*100 / (ok_squares + bomb_squares)

    def status_square(self, board, x, y):

        if board[y][x] == "B":
            return -1

        if y > 0 and board[y-1][x] == "B":
            return 0

        if x > 0 and board[y][x-1] == "B":
            return 0

        if x < len(board[0]) - 1 and board[y][x+1] == "B":
            return 0

        if y < len(board) - 1 and board[y+1][x] == "B":
            return 0

        if y > 0 and x > 0 and board[y-1][x-1] == "B":
            return 0

        if y < len(board) - 1 and x > 0 and board[y+1][x-1] == "B":
            return 0

        if y < len(board) - 1 and x < len(board[0]) - 1 and board[y+1][x+1] == "B":
            return 0

        if y > 0 and x < len(board[0]) - 1 and board[y-1][x+1] == "B":
            return 0

        return 1

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

def do_test(board, __expected):
    startTime = time.time()
    instance = BombSweeper()
    exception = None
    try:
        __result = instance.winPercentage(board);
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
    sys.stdout.write("BombSweeper (300 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("BombSweeper.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            board = []
            for i in range(0, int(f.readline())):
                board.append(f.readline().rstrip())
            board = tuple(board)
            f.readline()
            __answer = float(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(board, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1455655083
    PT, TT = (T / 60.0, 75.0)
    points = 300 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
