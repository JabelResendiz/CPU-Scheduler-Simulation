from basic_struct import Process
from fcfs import FCFS
from roundRobin import RoundRobin
from srtf import SRTF
from mlfq import MLFQScheduler
from scheduling import IScheduling
from typing import List,Tuple
import numpy as np
import matplotlib.pyplot as plt
import csv
import os


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

        # Algoritmos usados para definir mis clases aca
        self.mlfq_scheduler = MLFQScheduler(quantums=[.04,.08,.12])
        self.round_robin_scheduler = RoundRobin(quantum = .4)
        self.srtf_scheduler = SRTF()
        self.fcfs_scheduler = FCFS()

        self.schedulers: List[Tuple[str,IScheduling]] = [
            ("MLFQ", self.mlfq_scheduler),
            ("RoundRobin", self.round_robin_scheduler),
            ("SRTF", self.srtf_scheduler),
            ("FCFS", self.fcfs_scheduler)
        ]

        self.colors = {
            "MLFQ": 'purple',
            "RoundRobin": 'orange',
            "SRTF": 'green',
            "FCFS": 'blue'
        }


    def next_arrival(self):
        return self.rng.exponential(1/self.arrival_rate)
    
    def next_execution_time(self):
        return self.rng.exponential(1/self.execution_rate)


    

    def schedule_arriving(self):

        while self.time <= self.closing_time:
            
            arrival_time = self.time + self.next_arrival()
            execution_time = self.next_execution_time()

            pid= self.n_processes

            for _,scheduler in self.schedulers:
                p = Process(pid, arrival_time, execution_time)
                scheduler.add_process(p)

            self.n_processes += 1
            self.time = arrival_time
    
    def run_event(self):
        
        self.schedule_arriving()

        for _, scheduler in self.schedulers:
            scheduler.run()
            
        
    

    def statistics(self):
        results = {}
        for scheduler_name, scheduler in self.schedulers:
            turnaround = [p.turnaround_time for p in scheduler.completed_processes]
            waiting = [p.waiting_time for p in scheduler.completed_processes]
            results[scheduler_name] = {
                'avg_turnaround_time': np.mean(turnaround) if turnaround else 0,
                'avg_waiting_time': np.mean(waiting) if waiting else 0,
                'processes': len(scheduler.completed_processes),
                'waiting_times': waiting,
                'turnaround_times': turnaround,
                'avg_queue_size': sum(size for _,size in scheduler.queue_length_log) / len(scheduler.queue_length_log)
                                    if len(scheduler.queue_length_log) >0  else 0
            }
        return results

    def print_results(self):

        for scheduler_name, scheduler in self.schedulers:
            print(f"\n=== {scheduler_name} ===")
            print("PID | Arrival | Burst | Start | End | Turnaround | Waiting")
            for p in sorted(scheduler.completed_processes, key=lambda x: x.pid):
                print(f"{p.pid:3} | {p.arrival_time:7.1f} | {p.burst_time:5} | {p.start_time:5} | {p.end_time:3} | {p.turnaround_time:10.1f} | {p.waiting_time:7.1f}")
            avg_turnaround = sum(p.turnaround_time for p in scheduler.completed_processes) / len(scheduler.completed_processes)
            avg_waiting = sum(p.waiting_time for p in scheduler.completed_processes) / len(scheduler.completed_processes)
            print(f"Average Turnaround Time: {avg_turnaround:.2f}")
            print(f"Average Waiting Time: {avg_waiting:.2f}")


    def export_results_to_csv(self, output_folder="results"):
        os.makedirs(output_folder, exist_ok=True)

        for scheduler_name, scheduler in self.schedulers:
            filename = f"{output_folder}/{scheduler_name}_results.csv"
            with open(filename, mode='w', newline='') as file:
                writer = csv.writer(file)

                # Escribir encabezado
                writer.writerow(["PID", "Arrival", "Burst", "Start", "End", "Turnaround", "Waiting"])

                # Escribir datos por proceso
                for p in sorted(scheduler.completed_processes, key=lambda x: x.pid):
                    writer.writerow([
                        p.pid,
                        round(p.arrival_time, 1),
                        p.burst_time,
                        p.start_time,
                        p.end_time,
                        round(p.turnaround_time, 1),
                        round(p.waiting_time, 1)
                    ])

                # Escribir estadísticas
                if scheduler.completed_processes:
                    avg_turnaround = sum(p.turnaround_time for p in scheduler.completed_processes) / len(scheduler.completed_processes)
                    avg_waiting = sum(p.waiting_time for p in scheduler.completed_processes) / len(scheduler.completed_processes)
                    writer.writerow([])
                    writer.writerow(["Average Turnaround Time", f"{avg_turnaround:.2f}"])
                    writer.writerow(["Average Waiting Time", f"{avg_waiting:.2f}"])

        print(f"\n✅ Results exported to CSV in '{output_folder}/'")

        
    def plot_timelines(self):


        for scheduler_name, scheduler in self.schedulers:
            plt.figure(figsize=(14, 6))
            processes = scheduler.completed_processes
            processes.sort(key=lambda p: p.pid)

            for process in processes:
                pid = process.pid
                arrival = process.arrival_time
                start = process.start_time
                end = process.end_time

                y = pid

                plt.plot([arrival, start], [y, y], color='gray', linestyle='--', alpha=0.5)
                plt.plot([start, end], [y, y], color=self.colors.get(scheduler_name, 'black'), linewidth=3)
                plt.plot(arrival, y, 'ko', markersize=4)
                plt.plot(start, y, '>', color='green')
                plt.plot(end, y, 'x', color='red')

            plt.title(f"CPU Scheduling Timeline - {scheduler_name}")
            plt.xlabel("Time")
            plt.ylabel("Process ID")
            plt.grid(True, alpha=0.3)
            plt.tight_layout()
            plt.show()



