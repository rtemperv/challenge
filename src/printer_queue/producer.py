from threading import Thread
from time import sleep

from code.printer_queue import RegularTask
from random import randint


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