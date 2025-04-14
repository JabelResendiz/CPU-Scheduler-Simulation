from  basic_struct import Process,Event
from abc import ABC, abstractmethod
from typing import List
class IScheduling(ABC):
    
    def __init__(self):
        #self.process_queue = []         # Queue to store the processes (priority_queue)
        self.processes:List[Process] = []             # List to hold all processes
        self.current_time =0            # Tracks the current time during the scheduling
        self.completed_processes:List[Process] = []   # List to store processes once they finish execution
        self.event_queue:List[Event] = []           # Event queue for discrete event simulation
        self.queue_length_log = []
        
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
    # def reset(self):
    #     self.processes.clear()
    #     self.completed_processes.clear()
    #     self.event_queue.clear()
    #     self.current_time=0

