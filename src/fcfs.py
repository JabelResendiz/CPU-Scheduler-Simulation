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


# # Inicializamos los procesos
# procesos = [
#     Proceso("P1", 0, 4),
#     Proceso("P2", 1, 3),
#     Proceso("P3", 2, 1),
#     Proceso("P4", 3, 2),
#     Proceso("P5", 4, 5),
# ]

# # Cola de eventos (min-heap)
# eventos = []
# for p in procesos:
#     heapq.heappush(eventos, Evento(p.arrival_time, "ARRIVAL", p))

# ready_queue = []
# tiempo_actual = 0
# cpu_ocupada = False
# uso_cpu_total = 0

# # Simulador
# while eventos:
#     evento = heapq.heappop(eventos)
#     tiempo_actual = evento.time

#     if evento.tipo == "ARRIVAL":
#         ready_queue.append(evento.proceso)
#         if not cpu_ocupada:
#             next_proc = ready_queue.pop(0)
#             next_proc.start_time = tiempo_actual
#             end_time = tiempo_actual + next_proc.burst_time
#             next_proc.end_time = end_time
#             heapq.heappush(eventos, Evento(end_time, "END", next_proc))
#             cpu_ocupada = True
#             uso_cpu_total += next_proc.burst_time

#     elif evento.tipo == "END":
#         cpu_ocupada = False
#         if ready_queue:
#             next_proc = ready_queue.pop(0)
#             next_proc.start_time = tiempo_actual
#             end_time = tiempo_actual + next_proc.burst_time
#             next_proc.end_time = end_time
#             heapq.heappush(eventos, Evento(end_time, "END", next_proc))
#             cpu_ocupada = True
#             uso_cpu_total += next_proc.burst_time

# # Métricas finales
# print("\nResultados:")
# espera_total = 0
# retorno_total = 0
# for p in procesos:
#     espera = p.start_time - p.arrival_time
#     retorno = p.end_time - p.arrival_time
#     espera_total += espera
#     retorno_total += retorno
#     print(f"{p.pid}: Espera = {espera}, Retorno = {retorno}")

# print(f"\nTiempo total: {tiempo_actual}")
# print(f"Uso de CPU: {uso_cpu_total}")
# print(f"Porcentaje de uso de CPU: {uso_cpu_total / tiempo_actual * 100:.2f}%")
# print(f"Tiempo promedio de espera: {espera_total / len(procesos):.2f}")
# print(f"Tiempo promedio de retorno: {retorno_total / len(procesos):.2f}")
