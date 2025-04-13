from basic_struct import Process
from fcfs import FCFS
from sjf import SJF
from roundRobin import RoundRobin
from srtf import SRTF
from mlfq import MLFQScheduler
import numpy as np


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
        results = {}
        for scheduler_name, scheduler in [
            ("MLFQ", self.mlfq_scheduler),
            ("RoundRobin", self.round_robin_scheduler),
            ("SRTF", self.srtf_scheduler)
        ]:
            turnaround = [p.turnaround_time for p in scheduler.completed_processes]
            waiting = [p.waiting_time for p in scheduler.completed_processes]
            results[scheduler_name] = {
                'avg_turnaround_time': np.mean(turnaround) if turnaround else 0,
                'avg_waiting_time': np.mean(waiting) if waiting else 0,
                'processes': len(scheduler.completed_processes)
            }
        return results


# Parámetros de la simulación
arrival_rate = 3  # Número promedio de procesos que llegan por segundo (λ)
execution_rate = 2  # Tiempo promedio de ejecución de los procesos en segundos (μ)
closing_time = 100  # Tiempo de cierre (fin de la simulación)


