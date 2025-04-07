
import heapq
from basic_struct import Process,Event
from scheduling import Scheduling

class RoundRobin(Scheduling):
    def __init__(self,quantum):
        super().__int__()
        self.quantum = quantum
        self.ready_queue = []
    
    def add_process(self, process: Process):
        self.processes.append(process)
        arrival_event = Event(process.arrival_time,'ARRIVAL',process)
        heapq.heappush(self.event_queue,arrival_event)
    
    def run(self):
        while self.event_queue:
            event = heapq.heappop(self.event_queue)
            self.current_time = event.time
            self.process_event(event)
    
    def process_event(self, event: Event):
        if event.event_type == 'ARRIVAL':
            self.handle_arrival(event.process)
        elif event.event_type == 'COMPLETION':
            self.handle_completion(event.process)
    
    def handle_arrival(self, process: Process):
        self.ready_queue.append(process)
        self.schedule_next_process()
    
    def handle_completion(self, process: Process):
        
        process.turnaround_time = self.current_time - process.arrival_time

        process.waiting_time = process.turnaround_time - process.burst_time

        self.completed_processes.append(process)

        self.schedule_next_process()
    
    def schedule_next_process(self):

        if not self.ready_queue:
            return 

        process = self.ready_queue.pop(0)
        time_slice = min(self.quantum, process.burst_time)

        if process.start_time is None:
            process.start_time = self.current_time
        
        process.burst_time -= time_slice
        completion_time = self.current_time + time_slice

        if process.burst_time > 0:
            heapq.heappush(self.event_queue, Event(completion_time , 'COMPLETION', process))
            self.ready_queue.append(process)
        
        else:
            process.end_time = completion_time
            heapq.heappush(self.event_queue, Event(completion_time,'COMPLETION',process))