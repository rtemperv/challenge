from time import time

from code.printer_queue import Task


class RegularTask(Task):
    def __init__(self):
        super().__init__(5)
        self.start_time = time()

    def start(self):
        print("Regular task %s started after %s s queue time" % (self.id, time() - self.start_time))

    def stop(self):
        print("Regular task %s stopped" % self.id)

    def do_work(self):
        super().do_work()
