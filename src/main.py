
from simulation import CpuSchedulerSimulation
from analysis.plots import plot_and_save_metrics
import numpy as np
import os



def run_experiments():
    # Configuración
    arrival_rates = [0.3, 0.7, 0.9]   # λ (ρ = λ/μ)
    execution_rate = 1.0              # μ fijo
    closing_time = 1000               # Tiempo de simulación
    n_runs = 200                      # Réplicas por configuración

    all_results = []
    
    for λ in arrival_rates:
        print(f"Running experiments for λ = {λ}...")
        results=[]
        for _ in range(n_runs):
        
            sim = CpuSchedulerSimulation(λ, execution_rate, closing_time)
            sim.run_event()

            result = sim.statistics()
            results.append(result["SRTF"])
        
    
        all_results.append({
                "arrival_rate": λ,
                "rho": λ / execution_rate,
                "results": results
        })
    
    return all_results

if __name__ == "__main__":



    data = run_experiments()
    
    plot_and_save_metrics(data)
    