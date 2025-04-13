import heapq
from basic_struct import Process, Event
from scheduling import IScheduling
import numpy as np

class RoundRobin(IScheduling):
    def __init__(self, quantum):
        super().__init__()
        self.quantum = quantum
        self.ready_queue = []
        self.running_process = None  

    def add_process(self, process: Process):
        self.processes.append(process)
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
        self.ready_queue.append(process)
        if not self.running_process:
            self.schedule_next_process()

    def handle_time_slice_expired(self, process: Process):
        self.running_process = None
        if process.remaining_time > 0:
            self.ready_queue.append(process)
        self.schedule_next_process()

    def handle_completion(self, process: Process):
        self.running_process = None
        process.end_time = self.current_time
        process.turnaround_time = process.end_time - process.arrival_time
        process.waiting_time = process.turnaround_time - process.burst_time
        self.completed_processes.append(process)
        self.schedule_next_process()

    def schedule_next_process(self):
        if self.running_process or not self.ready_queue:
            return

        process = self.ready_queue.pop(0)
        self.running_process = process

        if process.start_time is None:
            process.start_time = self.current_time

        time_slice = min(self.quantum, process.remaining_time)
        process.remaining_time -= time_slice

        if process.remaining_time == 0:
            heapq.heappush(self.event_queue, Event(self.current_time + time_slice, 'COMPLETION', process))
        else:
            heapq.heappush(self.event_queue, Event(self.current_time + time_slice, 'TIME_SLICE_EXPIRED', process))

    # def statistics(self):

    #     turnaround = [p.turnaround_time for p in self.completed_processes]

    #     waiting = [p.waiting_time for p in self.completed_processes]

    #     return {
    #             'scheduler_name' : "Round Robin (RR)",
    #             'avg_turnaround_time': np.mean(turnaround) if turnaround else 0,
    #             'avg_waiting_time': np.mean(waiting) if waiting else 0,
    #             'processes': len(self.completed_processes)
    #            }
        