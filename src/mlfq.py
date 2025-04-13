import heapq
from collections import deque
from basic_struct import Process, Event
from scheduling import IScheduling

class MLFQScheduler(IScheduling):
    def __init__(self, quantums):
        super().__init__()
        self.quantums = quantums  
        self.queues = [deque() for _ in quantums] + [deque()]  
        self.running_process = None
        self.process_levels = {}  

    def add_process(self, process: Process):
        self.processes.append(process)
        self.process_levels[process.pid] = 0 
        arrival_event = Event(process.arrival_time, 'ARRIVAL', process)
        heapq.heappush(self.event_queue, arrival_event)

    def run(self):
        while self.event_queue:
            event = heapq.heappop(self.event_queue)
            self.current_time = event.time
            self.process_event(event)

    def process_event(self, event: Event):
        if event.event_type == 'ARRIVAL':
            self.handle_arrival(event.process)
        elif event.event_type == 'TIME_SLICE_EXPIRED':
            self.handle_time_slice_expired(event.process)
        elif event.event_type == 'COMPLETION':
            self.handle_completion(event.process)

    def handle_arrival(self, process: Process):
        self.queues[0].append(process)
        self.try_schedule_next()

    def handle_time_slice_expired(self, process: Process):
        self.running_process = None
        level = self.process_levels[process.pid]
        if level + 1 < len(self.queues):
            self.process_levels[process.pid] += 1  
        self.queues[self.process_levels[process.pid]].append(process)
        self.try_schedule_next()

    def handle_completion(self, process: Process):
        self.running_process = None
        process.end_time = self.current_time
        process.turnaround_time = process.end_time - process.arrival_time
        process.waiting_time = process.turnaround_time - process.burst_time
        self.completed_processes.append(process)
        self.try_schedule_next()

    def try_schedule_next(self):
        if self.running_process:
            return 

        for level, queue in enumerate(self.queues):
            if queue:
                process = queue.popleft()
                self.running_process = process
                if process.start_time is None:
                    process.start_time = self.current_time

                if level < len(self.quantums): 
                    quantum = self.quantums[level]
                    time_slice = min(quantum, process.remaining_time)
                else:  
                    time_slice = process.remaining_time

                process.remaining_time -= time_slice

                if process.remaining_time == 0:
                    event_type = 'COMPLETION'
                else:
                    event_type = 'TIME_SLICE_EXPIRED'

                heapq.heappush(self.event_queue, Event(self.current_time + time_slice, event_type, process))
                break
