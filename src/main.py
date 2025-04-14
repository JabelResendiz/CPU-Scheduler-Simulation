
from simulation import CpuSchedulerSimulation
import analysis.plots as analysis
import numpy as np
import os



def run_experiments():
    # Configuración
    arrival_rates = [0.3, 0.7, 0.9]   # λ (ρ = λ/μ)
    execution_rate = 1.0              # μ fijo
    closing_time = 1000               # Tiempo de simulación
    n_runs = 200                      # Réplicas por configuración

    all_results_srtf = []
    all_results_rr = []
    all_results_mlfq = []
    all_results_fcfs = []

    for λ in arrival_rates:
        print(f"Running experiments for λ = {λ}...")
        results_srtf=[]
        results_fcfs=[]
        results_rr = []
        results_mlfq = []
        for _ in range(n_runs):
        
            sim = CpuSchedulerSimulation(λ, execution_rate, closing_time)
            sim.run_event()

            result = sim.statistics()
            results_srtf.append(result["SRTF"])
            results_fcfs.append(result["FCFS"])
            results_mlfq.append(result["MLFQ"])
            results_rr.append(result["RoundRobin"])


        all_results_fcfs.append({
                "arrival_rate": λ,
                "rho": λ / execution_rate,
                "results": results_fcfs
        })

        all_results_srtf.append({
                "arrival_rate": λ,
                "rho": λ / execution_rate,
                "results": results_srtf
        })

        all_results_mlfq.append({
                "arrival_rate": λ,
                "rho": λ / execution_rate,
                "results": results_mlfq
        })

        all_results_rr.append({
                "arrival_rate": λ,
                "rho": λ / execution_rate,
                "results": results_rr
        })
    
    return all_results_srtf, all_results_fcfs,all_results_rr,all_results_mlfq

if __name__ == "__main__":

    data_srtf,data_fcfs,data_rr,data_mlfq = run_experiments()
    
    analysis.plot_and_save_metrics(data_srtf)

    # analysis.plot_and_save_metrics(data_rr)
    
    # analysis.plot_and_save_metrics(data_mlfq)
    
    analysis.plot_algorithm_comparison12(data_srtf,data_fcfs,data_rr,data_mlfq)

    analysis.plot_context_switches(data_srtf)

    