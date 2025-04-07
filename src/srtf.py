# import heapq
# from basic_struct import Process, Event
# from scheduling import Scheduling

# class SRTF(Scheduling):

#     def __init__(self):
#         super().__init__()
#         self.ready_queue = []  # Min-heap de (remaining_time, arrival_time, process)
#         self.running_process = None 

#     def add_process(self, process: Process):
#         self.processes.append(process)
#         arrival_event = Event(process.arrival_time, 'ARRIVAL', process)
#         heapq.heappush(self.event_queue, arrival_event)

#     def run(self):

#         event_running = heapq.heappop(self.event_queue)
#         self.running_process = event_running.process

#         arrival_event = Event(self.running_process.waiting_time,'READY',self.running_process)

#         heapq.heappush(self.ready_queue,arrival_event)

#         self.current_time = self.running_process.start_time

#         while self.ready_queue and self.event_queue:
            
#             if not self.event_queue:
#                 first_event = heapq.heappop(self.ready_queue)

#                 self.current_time += first_event.process.waiting_time

#                 continue


#             next_event = heapq.heappop(self.event_queue)
            
#             if not self.ready_queue :

#                 self.running_process = next_event.process

#                 arrival_event = Event(self.running_process.waiting_time,'READY',self.running_process)

#                 heapq.heappush(self.ready_queue,arrival_event)

#                 self.current_time = self.running_process.start_time

#                 continue


#             self.running_process = self.ready_queue[0].process

#             aux= min ( next_event.process.start_time - self.current_time,
#                                                       self.running_process.waiting_time)

#             if aux == self.running_process.waiting_time :

#                 heapq.heappop(self.ready_queue)

#                 self.current_time += aux

#             else:
#                 # aux < self.running_process.waiting_time

#                 self.current_time = next_event.process.start_time

#                 self.running_process.waiting_time -=  aux

            

            
#             # if self.running_process.waiting_time > next_event.process.waiting_time:

#             #     self.running_process = next_event.process

            

        

                
                

#     # def run(self):
#     #     while self.event_queue or self.ready_queue or self.running_process:
#     #         if not self.event_queue and not self.ready_queue:
#     #             break

#     #         # Determinar el siguiente tiempo relevante
#     #         if self.event_queue:
#     #             next_event = self.event_queue[0].time
#     #         else:
#     #             next_event = float('inf')

#     #         if self.running_process:
#     #             finish_time = self.current_time + self.running_process.remaining_time
#     #             if finish_time <= next_event:
#     #                 self.current_time = finish_time
#     #                 self.running_process.end_time = self.current_time
#     #                 self.running_process.turnaround_time = self.current_time - self.running_process.arrival_time
#     #                 self.running_process.waiting_time = self.running_process.turnaround_time - self.running_process.burst_time
#     #                 self.completed_processes.append(self.running_process)
#     #                 self.running_process = None
#     #                 continue

#     #         # Si hay eventos antes de que el proceso actual termine, procesarlos
#     #         event = heapq.heappop(self.event_queue)
#     #         self.current_time = max(self.current_time, event.time)
#     #         self.process_event(event)

#     # def process_event(self, event: Event):
#     #     if event.event_type == 'ARRIVAL':
#     #         process = event.process
#     #         heapq.heappush(self.ready_queue, (process.remaining_time, process.arrival_time, process))
#     #         self.preempt_if_needed()


#     # def preempt_if_needed(self):
#     #     if not self.ready_queue:
#     #         return

#     #     top_process = self.ready_queue[0][2]

#     #     if not self.running_process:
#     #         heapq.heappop(self.ready_queue)
#     #         self.start_process(top_process)
#     #     elif top_process.remaining_time < self.running_process.remaining_time:
#     #         heapq.heappush(self.ready_queue, (self.running_process.remaining_time, self.running_process.arrival_time, self.running_process))
#     #         self.running_process = None
#     #         heapq.heappop(self.ready_queue)
#     #         self.start_process(top_process)

#     # def start_process(self, process: Process):
#     #     if process.start_time is None:
#     #         process.start_time = self.current_time
#     #     self.running_process = process

import heapq
from basic_struct import Process, Event
from scheduling import Scheduling

class SRTF(Scheduling):
    def __init__(self):
        super().__init__()
        self.ready_queue = []  # Min-heap by remaining_time
        self.running_process = None
        self.running_since = None  # To track execution start time for slicing

    def process_event(self, event: Event):
        if event.event_type == 'ARRIVAL':
            process = event.process
            heapq.heappush(self.ready_queue, (process.remaining_time, process))

    def handle_arrival(self, process: Process):
        return super().handle_arrival(process)
    
    def handle_completion(self, process: Process):
        return super().handle_completion(process)
    
    def add_process(self, process: Process):
        arrival_event = Event(process.arrival_time, 'ARRIVAL', process)
        heapq.heappush(self.event_queue, arrival_event)
        self.processes.append(process)
    def run(self):
        while self.event_queue or self.ready_queue or self.running_process:
            # Si no hay proceso corriendo y no hay procesos listos, avanzamos al próximo evento
            if not self.running_process and not self.ready_queue and self.event_queue:
                event = heapq.heappop(self.event_queue)
                self.current_time = max(self.current_time, event.time)
                self.process_event(event)
                continue

            # Ver tiempo del próximo evento
            next_event_time = self.event_queue[0].time if self.event_queue else float('inf')

            # Si hay un proceso corriendo, vemos cuánto tiempo puede ejecutarse
            if self.running_process:
                time_slice = min(self.running_process.remaining_time, next_event_time - self.current_time)

                # Ejecutamos el proceso por el slice correspondiente
                self.running_process.remaining_time -= time_slice
                self.current_time += time_slice

                # Si termina durante este slice
                if self.running_process.remaining_time == 0:
                    self.running_process.end_time = self.current_time
                    self.running_process.turnaround_time = self.running_process.end_time - self.running_process.arrival_time
                    self.running_process.waiting_time = self.running_process.turnaround_time - self.running_process.burst_time
                    self.completed_processes.append(self.running_process)
                    self.running_process = None
            else:
                # Si no hay proceso corriendo, avanzamos hasta el próximo evento
                self.current_time = next_event_time

            # Procesamos eventos que ocurren en este instante
            while self.event_queue and self.event_queue[0].time <= self.current_time:
                event = heapq.heappop(self.event_queue)
                self.process_event(event)

            # Verificamos si hay que interrumpir el proceso actual
            if self.running_process and self.ready_queue:
                next_ready = self.ready_queue[0][1]
                if next_ready.remaining_time < self.running_process.remaining_time:
                    # Interrupción
                    heapq.heappush(self.ready_queue, (self.running_process.remaining_time, self.running_process))
                    self.running_process = None

            # Si no hay proceso corriendo, seleccionamos uno nuevo
            if not self.running_process and self.ready_queue:
                _, proc = heapq.heappop(self.ready_queue)
                if proc.start_time is None:
                    proc.start_time = self.current_time
                self.running_process = proc
