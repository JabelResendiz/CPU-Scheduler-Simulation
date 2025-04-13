from  basic_struct import Process,Event
from abc import ABC, abstractmethod

class IScheduling(ABC):
    
    def __init__(self):
        #self.process_queue = []         # Queue to store the processes (priority_queue)
        self.processes = []             # List to hold all processes
        self.current_time =0            # Tracks the current time during the scheduling
        self.completed_processes = []   # List to store processes once they finish execution
        self.event_queue = []           # Event queue for discrete event simulation

    @abstractmethod
    def add_process(self, process: Process):
        pass

    @abstractmethod
    def process_event(self, event: Event):
        pass

    @abstractmethod
    def handle_arrival(self, process: Process):
        pass

    @abstractmethod
    def handle_completion(self, process: Process):
        pass

    @abstractmethod
    def run(self):
        pass

    # @abstractmethod
    # def statistics(self):
    #     pass