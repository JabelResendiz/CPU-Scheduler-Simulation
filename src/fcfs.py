import heapq
from basic_struct import Process,Event
from scheduling import Scheduling

class FCFS(Scheduling):
    def __init__(self):
        super().__init__()

    def add_process(self, process: Process):

        self.processes.append(process)

        arrival_event = Event(process.arrival_time,'ARRIVAL',process)

        heapq.heappush(self.event_queue,arrival_event)
            
    def run(self):

        while self.event_queue:

            event = heapq.heappop(self.event_queue)

            self.process_event(event)

    def process_event(self, event: Event):

        if event.event_type == 'ARRIVAL':
            self.handle_arrival(event.process)

        elif event.event_type == 'COMPLETION':
            self.handle_completion(event.process)

    def handle_arrival(self, process: Process):

        self.current_time = max (self.current_time, process.arrival_time)

        process.start_time = self.current_time

        process.end_time = self.current_time + process.burst_time

        self.current_time += process.burst_time

        completion_event = Event(process.end_time,'COMPLETION',process)

        heapq.heappush(self.event_queue,completion_event)

    def handle_completion(self, process: Process):
        
        process.waiting_time = process.start_time - process.arrival_time
        process.turnaround_time = process.end_time - process.arrival_time
        self.completed_processes.append(process)        

