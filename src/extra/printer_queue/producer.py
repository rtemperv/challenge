from threading import Thread
from time import sleep

from random import randint
from src.extra.printer_queue.regular_task import RegularTask


class Producer(Thread):
    def __init__(self, print_frequency, queue):
        super().__init__()
        self.print_frequency = print_frequency
        self.queue = queue
        self.running = True

    def run(self):
        while self.running:
            value = randint(0, self.print_frequency)
            if value == self.print_frequency:
                print('Producer with frequency %s created task' % self.print_frequency)
                self.queue.enqueue(RegularTask())
            sleep(1)

    def stop_thread(self):
        self.running = False
