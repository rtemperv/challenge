# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect
from datetime import datetime
from functools import partial

from src.structures.queue import Queue

class Salary:
    def howMuch(self, arrival, departure, wage):

        time_converter = lambda x: datetime.strptime(x, '%H:%M:%S')

        arrival = map(time_converter, arrival)
        departure = map(time_converter, departure)

        q = Queue(zip(arrival, departure))

        evening = datetime.strptime('18:00:00', '%H:%M:%S')
        morning = datetime.strptime('06:00:00', '%H:%M:%S')

        night_shifts = []
        day_shifts = []

        while not q.is_empty():
            arr, dep = q.dequeue()

            if arr < morning and dep < morning:
                night_shifts.append((arr, dep))

            elif arr < morning <= dep:
                night_shifts.append((arr, morning))
                q.enqueue((morning, dep))

            elif morning <= arr < evening and morning <= dep < evening:
                day_shifts.append((arr, dep))

            elif arr < evening <= dep:
                day_shifts.append((arr, evening))
                q.enqueue((evening, dep))

            else:
                night_shifts.append((arr, dep))

        pay = 0
        pay += wage * sum(list(map(self.calculate_time_difference, day_shifts)))
        pay += wage * sum(list(map(self.calculate_time_difference, night_shifts))) * 1.5

        return pay

    def calculate_time_difference(self, times):
        arr, dep = times
        delta = dep - arr

        return delta.seconds/3600



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

def do_test(arrival, departure, wage, __expected):
    startTime = time.time()
    instance = Salary()
    exception = None
    try:
        __result = instance.howMuch(arrival, departure, wage);
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
    sys.stdout.write("Salary (300 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("Salary.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            arrival = []
            for i in range(0, int(f.readline())):
                arrival.append(f.readline().rstrip())
            arrival = tuple(arrival)
            departure = []
            for i in range(0, int(f.readline())):
                departure.append(f.readline().rstrip())
            departure = tuple(departure)
            wage = int(f.readline().rstrip())
            f.readline()
            __answer = int(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(arrival, departure, wage, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1454700485
    PT, TT = (T / 60.0, 75.0)
    points = 300 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
