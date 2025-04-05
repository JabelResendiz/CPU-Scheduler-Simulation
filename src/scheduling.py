import heapq
from  basic_struct import Process,Event

class Scheduling:
    
    def __init__(self):
        #self.process_queue = []         # Queue to store the processes (priority_queue)
        self.processes = []             # List to hold all processes
        self.current_time =0            # Tracks the current time during the scheduling
        self.completed_processes = []   # List to store processes once they finish execution
        self.event_queue = []           # Event queue for discrete event simulation

    def add_process (self,process:Process):
        raise NotImplementedError("Subclasess must implement this method")
    
    def process_event(self,event: Event):
        raise NotImplementedError()
    
    def handle_arrival(self,process:Process):
        raise NotImplementedError()
    
    def handle_completion(self,process:Process):
        raise NotImplementedError()
    
    def run(self):
        raise NotImplementedError("Subclasses must implement this method")