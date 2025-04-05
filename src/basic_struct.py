# Basic Struct
class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid                      # Unique identifier for each process
        self.arrival_time = arrival_time    # Time when the process arrives
        self.burst_time = burst_time        # Execution time of the process
        self.start_time = None              # Time when the process starts executing (to be set later)
        self.end_time = None                # Time when the process finishes executing (to be set later)
        self.waiting_time = None            # Time the process waits before starting execution
        self.turnaround_time = None         # Total time from arrival to completion

class Event:
    def __init__(self, time, event_type, process):
        self.time = time                    # Time when this event occurs
        self.event_type = event_type        # Type of the event (e.g., 'arrival', 'completion')
        self.process = process              # The process involved in the event

    def __lt__(self, other):
        """Defines how to compare events"""
        return self.time < other.time

