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

        while self.event_queue or self.ready_queue:
            
            if not self.event_queue and self.ready_queue:
                self.execute_next()
            
            elif self.event_queue and (not self.ready_queue or self.event_queue[0].time <= self.current_time):
                event = heapq.heappop(self.event_queue)
                self.current_time = max (self.current_time, event.time)
                self.process_event(event)
            
            else:
                self.execute_next()

    def execute_next(self):
        if self.ready_queue:
            _,process = heapq.heappop(self.ready_queue)
            process.start_time = self.current_time
            process.end_time = self.current_time+ process.burst_time
            process.waiting_time = process.start_time - process.arrival_time
            process.turnaround_time = process.end_time - process.arrival_time 
            self.current_time = process.end_time
            completion_event = Event(process.end_time, 'COMPLETION',process)
            heapq.heappush(self.event_queue, completion_event)

    def process_event(self, event: Event):
        if event.event_type == 'ARRIVAL':
            heapq.heappush(self.ready_queue, (event.process.burst_time, event.process))
        elif event.event_type == 'COMPLETION':
            self.handle_completion(event.process)
        
    def handle_arrival(self, process: Process):

        
    def handle_completion(self, process: Process):
        self.completed_processes.append(process)
        