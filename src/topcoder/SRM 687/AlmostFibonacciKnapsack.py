# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class AlmostFibonacciKnapsack:

    def __init__(self):
        self.almost_fib_cache = {1: 2, 2: 3}
        self.knapsack_cache = collections.defaultdict(lambda: {})

    def getIndices(self, x):
        return self.recursive_knapsack(x, 1)


    def get_almost_fibonaci_number(self, i):
        """
        Get the fibonaci number a t position i
        """
        if i in self.almost_fib_cache:
            return self.almost_fib_cache[i]

        n = self.get_almost_fibonaci_number(i - 1) + self.get_almost_fibonaci_number(i - 2) - 1
        self.almost_fib_cache[i] = n
        return n

    def recursive_knapsack(self, number, i):

        if number == 0:
            return []

        if number in self.knapsack_cache and i in self.knapsack_cache[number]:
            return self.knapsack_cache[number][i]

        fib_number = self.get_almost_fibonaci_number(i)

        if fib_number > number:
            return None

        elements = self.recursive_knapsack(number - fib_number, i+1)

        if elements is not None:
            return [i] + elements

        return self.recursive_knapsack(number, i + 1)

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

def do_test(x, __expected):
    startTime = time.time()
    instance = AlmostFibonacciKnapsack()
    exception = None
    try:
        __result = instance.getIndices(x);
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
    sys.stdout.write("AlmostFibonacciKnapsack (250 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("AlmostFibonacciKnapsack.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            x = int(f.readline().rstrip())
            f.readline()
            __answer = []
            for i in range(0, int(f.readline())):
                __answer.append(int(f.readline().rstrip()))
            __answer = tuple(__answer)

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(x, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1460717981
    PT, TT = (T / 60.0, 75.0)
    points = 250 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end


a = AlmostFibonacciKnapsack()
print(a.getIndices(453563543))
