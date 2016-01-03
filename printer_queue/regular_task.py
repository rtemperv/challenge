from printer_queue.task import Task
from time import time

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
