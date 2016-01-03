import re


class TestRunner:
    def __init__(self, subtasks):
        self.test_cases = subtasks

    def run_match(self, regexes):

        if len(regexes) == 0:
            matched_keys = self.test_cases.keys()
        else:
            matched_keys = filter(lambda x: re.match(regexes[0], x) is not None, self.test_cases.keys())

        for key in matched_keys:
            if isinstance(self.test_cases[key], TestRunner):
                print("# Chapter %s" % key)
                self.test_cases[key].run_match(regexes[1:])
            else:
                print("### Exercise %s" % key)
                self.test_cases[key]()
