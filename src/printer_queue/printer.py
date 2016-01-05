import time
from threading import Thread

from code.structures import Queue


class Printer(Thread):
    def __init__(self, queue: Queue):
        super().__init__()
        self.current_task = None
        self.task_queue = queue

    def run(self):
        while True:
            if self.current_task:
                if self.current_task.work_left == 0:
                    self.current_task.stop()
                    self.current_task = None
                else:
                    self.current_task.do_work()
            else:
                print('%s elements in queue' % len(self.task_queue))
                try:
                    self.current_task = self.task_queue.dequeue()
                    self.current_task.start()
                except IndexError:
                    pass

            time.sleep(1)
