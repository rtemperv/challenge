from abc import ABCMeta, abstractmethod


class Task(metaclass=ABCMeta):

    id_counter = 1

    def __init__(self, work_units):
        self.work_units = work_units
        self.work_done = 0
        self.id = Task.id_counter
        Task.id_counter += 1

    @abstractmethod
    def do_work(self):
        self.work_done += 1

    @property
    def work_left(self):
        return self.work_units - self.work_done

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass
