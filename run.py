from testrunner import TestRunner
from chapter_1.run import runner
import sys


def main():
    print("Running tests... \n")
    r = TestRunner({
        "1": runner
    })

    r.run_match(sys.argv[1:])

if __name__ == '__main__':
    main()