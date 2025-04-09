from basic_struct import Process
from fcfs import FCFS
from sjf import SJF
from roundRobin import RoundRobin
from srtf import SRTF
from mlfq import MLFQScheduler
import numpy as np
import heapq


# # --- Simulación---
# np.random.seed(42)
# num_processes = 10
# arrival_rate = 2.0
# burst_mean = 6

# current_arrival = 0
# original_process_list = []

# for pid in range(1, num_processes + 1):
#     inter_arrival = np.random.exponential(scale=arrival_rate)
#     current_arrival += round(inter_arrival, 1)
#     burst_time = max(1, int(np.random.exponential(scale=burst_mean)))
#     original_process_list.append(Process(pid, current_arrival, burst_time))

# def print_results(title, completed_processes):
#     print(f"\n=== {title} ===")
#     print("PID | Arrival | Burst | Start | End | Turnaround | Waiting")
#     for p in sorted(completed_processes, key=lambda x: x.pid):
#         print(f"{p.pid:3} | {p.arrival_time:7.1f} | {p.burst_time:5} | {p.start_time:5} | {p.end_time:3} | {p.turnaround_time:10.1f} | {p.waiting_time:7.1f}")
#     avg_turnaround = sum(p.turnaround_time for p in completed_processes) / num_processes
#     avg_waiting = sum(p.waiting_time for p in completed_processes) / num_processes
#     print(f"Average Turnaround Time: {avg_turnaround:.2f}")
#     print(f"Average Waiting Time: {avg_waiting:.2f}")

# # --- FCFS ---
# scheduler_fcfs = FCFS()
# fcfs_processes = copy.deepcopy(original_process_list)
# for p in fcfs_processes:
#     scheduler_fcfs.add_process(p)
# scheduler_fcfs.run()
# print_results("FCFS", scheduler_fcfs.completed_processes)

# # --- SJF ---
# scheduler_sjf = SJF()
# sjf_processes = copy.deepcopy(original_process_list)
# for p in sjf_processes:
#     scheduler_sjf.add_process(p)
# scheduler_sjf.run()
# print_results("SJF", scheduler_sjf.completed_processes)

# # --- SRTF ---
# scheduler_srtf = SRTF()
# srtf_processes = copy.deepcopy(original_process_list)
# for p in srtf_processes:
#     scheduler_srtf.add_process(p)
# scheduler_srtf.run()
# print_results("SRTF", scheduler_srtf.completed_processes)

# # --- Round Robin ---
# quantum = 18
# scheduler_rr = RoundRobin(quantum)
# rr_processes = copy.deepcopy(original_process_list)
# for p in rr_processes:
#     scheduler_rr.add_process(p)
# scheduler_rr.run()
# print_results(f"Round Robin (q={quantum})", scheduler_rr.completed_processes)

# # --- MLFQ ---
# quantums = [18, 28, 42]
# scheduler_mlfq = MLFQScheduler(quantums)
# mlfq_processes = copy.deepcopy(original_process_list)
# for p in mlfq_processes:
#     scheduler_mlfq.add_process(p)
# scheduler_mlfq.run()
# print_results(f"MLFQ {quantums}", scheduler_mlfq.completed_processes)








# # if __name__ =="__main__":
    
# #     # scheduler = FCFS()

# #     # processes = [
# #     #     Process("P1", 0, 4),
# #     #     Process("P2", 1, 3),
# #     #     Process("P3", 2, 1),
# #     #     Process("P4", 3, 2),
# #     #     Process("P5", 4, 5),
# #     # ]

# #     # # Add them to the scheduler
# #     # for p in processes:
# #     #     scheduler.add_process(p)

# #     # # Run the scheduler
# #     # scheduler.run()

# #     # print("Execution Results (FCFS):\n")
# #     # for p in scheduler.completed_processes:
# #     #     print(f"Process {p.pid}: Start = {p.start_time}, End = {p.end_time}, Arrival = {p.arrival_time}, Burst = {p.burst_time}")
# #     #     print(f"  -> Waiting Time: {p.waiting_time}, Turnaround Time: {p.turnaround_time}\n")
    



# #     # processes = [
# #     #     Process("P1", 0, 6),  
# #     #     Process("P2", 1, 8),
# #     #     Process("P3", 2, 7),
# #     #     Process("P4", 3, 3),
# #     #     Process("P5", 89, 4),
# #     # ]
    
# #     # sjf_scheduler = SJF()
    
# #     # for process in processes:
# #     #     sjf_scheduler.add_process(process)
    
# #     # sjf_scheduler.run()

# #     # print("Execution Results (SJF):")
# #     # for process in sjf_scheduler.completed_processes:
# #     #     print(f"Process {process.pid}: Start = {process.start_time}, End = {process.end_time}, Arrival = {process.arrival_time}, Burst = {process.burst_time}")
# #     #     print(f"  -> Waiting Time: {process.waiting_time}, Turnaround Time: {process.turnaround_time}\n")

    



# #     # processes = [
# #     #     Process("P1", 0, 6),  
# #     #     Process("P2", 1, 8),
# #     #     Process("P3", 2, 7),
# #     #     Process("P4", 3, 3),
# #     #     Process("P5", 8, 10),
# #     # ]


# #     # round_scheduler = RoundRobin(3)

# #     # for process in processes:
# #     #     round_scheduler.add_process(process)
    
# #     # round_scheduler.run()

# #     # print("Execution Results ():")
# #     # for process in round_scheduler.completed_processes:
# #     #     print(f"Process {process.pid}: Start = {process.start_time}, End = {process.end_time}, Arrival = {process.arrival_time}, Burst = {process.burst_time}")
# #     #     print(f"  -> Waiting Time: {process.waiting_time}, Turnaround Time: {process.turnaround_time}\n")

# #     # processes = [
# #     #     Process("P1", 0, 6),  
# #     #     Process("P2", 1, 8),
# #     #     Process("P3", 2, 7),
# #     #     Process("P4", 3, 3),
# #     #     Process("P5", 8, 10),
# #     # ]


# #     # srtf_scheduler = SRTF()

# #     # for process in processes:
# #     #     srtf_scheduler.add_process(process)
    
# #     # srtf_scheduler.run()

# #     # print("Execution Results ():")
# #     # for process in srtf_scheduler.completed_processes:
# #     #     print(f"Process {process.pid}: Start = {process.start_time}, End = {process.end_time}, Arrival = {process.arrival_time}, Burst = {process.burst_time}")
# #     #     print(f"  -> Waiting Time: {process.waiting_time}, Turnaround Time: {process.turnaround_time}\n")


# #     # processes = [
# #     #     Process("P1", 0, 6),
# #     #     Process("P2", 1, 8),
# #     #     Process("P3", 2, 7),
# #     #     Process("P4", 3, 3),
# #     #     Process("P5", 8, 10),
# #     # ]

# #     # scheduler = MLFQScheduler(quantums=[4, 8, 12])
# #     # for p in processes:
# #     #     scheduler.add_process(p)

# #     # scheduler.run()

# #     # print("Execution Results ():")
# #     # for p in scheduler.completed_processes:
# #     #     print(f"Process {p.pid}: Start = {p.start_time}, End = {p.end_time}, Arrival = {p.arrival_time}, Burst = {p.burst_time}")
# #     #     print(f"  -> Waiting Time: {p.waiting_time}, Turnaround Time: {p.turnaround_time}")



    

# #     np.random.seed(42)

# #     num_processes = 10
# #     arrival_rate = 2.0
# #     burst_mean = 6


# #     current_arrival =0
# #     process_list = []

# #     for pid in range(1,num_processes+1):

# #         inter_arrival = np.random.exponential(scale = arrival_rate)

# #         current_arrival+= round(inter_arrival,1)

# #         burst_time = max(1, int(np.random.exponential(scale = burst_mean)))

# #         process =Process( pid, current_arrival,burst_time)

# #         process_list.append(process)

# #     quantums = [4,8,12]

# #     scheduler = MLFQScheduler(quantums)

# #     for process in process_list:
# #         scheduler.add_process(process)
    
# #     scheduler.run()


# #     print("PID | Arrival | Burst | Start | End | Turnaround | Waiting")
# #     for p in sorted(scheduler.completed_processes, key=lambda x: x.pid):
# #         print(f"{p.pid:3} | {p.arrival_time:7.1f} | {p.burst_time:5} | {p.start_time:5} | {p.end_time:3} | {p.turnaround_time:10.1f} | {p.waiting_time:7.1f}")

# #     avg_turnaround = sum(p.turnaround_time for p in scheduler.completed_processes) / num_processes
# #     avg_waiting = sum(p.waiting_time for p in scheduler.completed_processes) / num_processes
# #     print(f"\nAverage Turnaround Time: {avg_turnaround:.2f}")
# #     print(f"Average Waiting Time: {avg_waiting:.2f}")



class CpuSchedulerSimulation:
    """
    Simula un planificador de CPU:
    - Los procesos llegan según una distribución de Poisson.
    - El tiempo de ejecución de los procesos sigue una distribución exponencial.
    """
    def __init__(self, arrival_rate, execution_rate, closing_time):
        # Parámetros
        self.arrival_rate = arrival_rate  # Tasa de llegadas (λ) para la distribución Poisson
        self.execution_rate = execution_rate  # Tasa de ejecución (μ) para la distribución exponencial
        self.closing_time = closing_time  # Hora de cierre para no generar más procesos

        self.rng = np.random.default_rng()  # Generador de números aleatorios
        
        # Estado de la simulación
        self.time = 0
        self.n_processes = 0
        # self.events_queue = []  # Cola de eventos para manejar llegadas y salidas
        # self.events = {'arrival': self.new_arrival, 'departure': self.new_departure}

        # # Variables de simulación
        # self.processes = []  # Lista para almacenar los procesos generados (con llegada y tiempo de ejecución)

        self.mlfq_scheduler = MLFQScheduler(quantums=[4,8,12])
        self.round_robin_scheduler = RoundRobin(quantum = 4)
        self.srtf_scheduler = SRTF()
        self.fcfs_scheduler = FCFS()
        
    def next_arrival(self):
        return self.rng.exponential(1/self.arrival_rate)
    
    def next_execution_time(self):
        return self.rng.exponential(1/self.execution_rate)


    def create_process(self):

        arrival_time = self.time + self.next_arrival()
        execution_time = self.next_execution_time()

        pid= self.n_processes
        process = Process(pid,arrival_time,execution_time)
        self.n_processes +=1

        return process
    
    def schedule_next_event(self):

        if self.time < self.closing_time:
            next_arrival_time = self.time + self.next_arrival()
    
    def new_arrival(self):

        process = self.create_process()
        self.schedule_next_event()
        self.mlfq_scheduler.add_process(process)
        self.round_robin_scheduler.add_process(process)
        self.srtf_scheduler.add_process(process)
    
    def run_event(self):
        self.mlfq_scheduler.run()
        self.round_robin_scheduler.run()
        self.srtf_scheduler.run()
    

    def statistics(self):
        turnaround_time = []
        waiting_time = []

        for scheduler in [self.mlfq_scheduler,self.round_robin_scheduler,self.srtf_scheduler]:
            for process in scheduler.processes:
                turnaround_time.append(process.turnaround_time)
                waiting_time.append(process.waiting_time)

# Parámetros de la simulación
arrival_rate = 3  # Número promedio de procesos que llegan por segundo (λ)
execution_rate = 2  # Tiempo promedio de ejecución de los procesos en segundos (μ)
closing_time = 100  # Tiempo de cierre (fin de la simulación)


