import heapq
from basic_struct import Process, Event
from scheduling import IScheduling

class SRTF(IScheduling):
    def __init__(self):
        super().__init__()
        self.ready_queue = []  # Min-heap by (remaining_time, pid, process)
        self.running_process = None
        

    def add_process(self, process: Process):
        arrival_event = Event(process.arrival_time, 'ARRIVAL', process)
        heapq.heappush(self.event_queue, arrival_event)
        self.processes.append(process)

    def process_event(self, event: Event):
        if event.event_type == 'ARRIVAL':
            process = event.process
            heapq.heappush(self.ready_queue, (process.remaining_time, process.pid, process))
            self.queue_length_log.append((self.current_time, len(self.ready_queue)))  # Log cola tras llegada

            # Check for preemption
            if self.running_process and process.remaining_time < self.running_process.remaining_time:
                heapq.heappush(self.ready_queue, (self.running_process.remaining_time, self.running_process.pid, self.running_process))
                self.running_process = None
                self.queue_length_log.append((self.current_time, len(self.ready_queue)))  # Log cola tras preempción

    def run(self):
        while self.event_queue or self.ready_queue or self.running_process:
            next_event_time = self.event_queue[0].time if self.event_queue else float('inf')

            if not self.running_process:
                if self.ready_queue:
                    _, _, proc = heapq.heappop(self.ready_queue)
                    if proc.start_time is None:
                        proc.start_time = self.current_time
                    self.running_process = proc
                elif self.event_queue:
                    event = heapq.heappop(self.event_queue)
                    self.current_time = max(self.current_time, event.time)
                    self.process_event(event)
                    continue
                else:
                    break 

            time_slice = min(self.running_process.remaining_time, next_event_time - self.current_time)
            self.running_process.remaining_time -= time_slice
            self.current_time += time_slice

            if self.running_process.remaining_time == 0:
                self.running_process.end_time = self.current_time
                self.running_process.turnaround_time = self.running_process.end_time - self.running_process.arrival_time
                self.running_process.waiting_time = self.running_process.turnaround_time - self.running_process.burst_time
                self.completed_processes.append(self.running_process)
                self.running_process = None
                self.queue_length_log.append((self.current_time, len(self.ready_queue)))  # Log tras finalización

            while self.event_queue and self.event_queue[0].time <= self.current_time:
                event = heapq.heappop(self.event_queue)
                self.process_event(event)

            if self.running_process and self.ready_queue:
                next_ready = self.ready_queue[0][2]
                if next_ready.remaining_time < self.running_process.remaining_time:
                    heapq.heappush(self.ready_queue, (self.running_process.remaining_time, self.running_process.pid, self.running_process))
                    self.running_process = None
                    self.queue_length_log.append((self.current_time, len(self.ready_queue)))  # Log preempción
                    
    def handle_arrival(self, process: Process):
        return super().handle_arrival(process)
    
    def handle_completion(self, process: Process):
        return super().handle_completion(process)
    
    def print_results(self):
        super().print_results("SRTF")
        print("Queue size log (time, size):")
        for t, s in self.queue_length_log:
            print(f"Time {t:.2f}: Queue size = {s}")
