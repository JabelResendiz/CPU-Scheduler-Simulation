import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

def plot_and_save_metrics(all_results, output_dir="./"):
    lambda_values = []
    mean_waiting_times = []
    mean_turnaround_times = []
    mean_queue_sizes = []  # Nueva lista para el tamaño promedio de la cola
    ci_waiting = []
    ci_turnaround = []
    ci_queue_size = []  # Nueva lista para el intervalo de confianza del tamaño de la cola

    for result_group in all_results:
        λ = result_group["arrival_rate"]
        lambda_values.append(λ)

        waiting_times = [r["avg_waiting_time"] for r in result_group["results"]]
        turnaround_times = [r["avg_turnaround_time"] for r in result_group["results"]]
        queue_sizes = [r["avg_queue_size"] for r in result_group["results"]]  # Recoger los tamaños de cola

        # Media
        mean_w = np.mean(waiting_times)
        mean_t = np.mean(turnaround_times)
        mean_q = np.mean(queue_sizes)  # Promedio del tamaño de la cola

        # Intervalo de confianza 95%
        ci_w = stats.t.interval(0.95, len(waiting_times)-1, loc=mean_w, scale=stats.sem(waiting_times))
        ci_t = stats.t.interval(0.95, len(turnaround_times)-1, loc=mean_t, scale=stats.sem(turnaround_times))
        ci_q = stats.t.interval(0.95, len(queue_sizes)-1, loc=mean_q, scale=stats.sem(queue_sizes))  # Intervalo de confianza para cola

        mean_waiting_times.append(mean_w)
        mean_turnaround_times.append(mean_t)
        mean_queue_sizes.append(mean_q)  # Agregar promedio del tamaño de la cola
        ci_waiting.append((ci_w[1] - ci_w[0]) / 2)
        ci_turnaround.append((ci_t[1] - ci_t[0]) / 2)
        ci_queue_size.append((ci_q[1] - ci_q[0]) / 2)  # Agregar intervalo de confianza para cola

    # --- Gráfico de tiempo de espera ---
    plt.figure(figsize=(10, 6))
    plt.errorbar(lambda_values, mean_waiting_times, yerr=ci_waiting, fmt='-o', capsize=5, color='blue', label='Avg Waiting Time')
    plt.xlabel('Tasa de llegada (λ)')
    plt.ylabel('Tiempo de espera promedio')
    plt.title('Tiempo de espera promedio vs λ (con IC 95%) - SRTF')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"{output_dir}/tiempo_espera_vs_lambda.png", dpi=300)
    plt.close()

    # --- Gráfico de tiempo de retorno ---
    plt.figure(figsize=(10, 6))
    plt.errorbar(lambda_values, mean_turnaround_times, yerr=ci_turnaround, fmt='-o', capsize=5, color='green', label='Avg Turnaround Time')
    plt.xlabel('Tasa de llegada (λ)')
    plt.ylabel('Tiempo de retorno promedio')
    plt.title('Tiempo de retorno promedio vs λ (con IC 95%) - SRTF')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"{output_dir}/tiempo_retorno_vs_lambda.png", dpi=300)
    plt.close()

    # --- Gráfico de tamaño de la cola promedio ---
    plt.figure(figsize=(10, 6))
    plt.errorbar(lambda_values, mean_queue_sizes, yerr=ci_queue_size, fmt='-o', capsize=5, color='orange', label='Avg Queue Size')
    plt.xlabel('Tasa de llegada (λ)')
    plt.ylabel('Tamaño de cola promedio')
    plt.title('Tamaño de cola promedio vs λ (con IC 95%) - SRTF')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"{output_dir}/tamano_cola_vs_lambda.png", dpi=300)
    plt.close()



def plot_algorithm_comparison(all_results_srtf, all_results_fcfs, output_dir="./"):
    lambda_values = []
    srtf_waiting = []
    fcfs_waiting = []
    srtf_ci = []
    fcfs_ci = []

    for srtf_group, fcfs_group in zip(all_results_srtf, all_results_fcfs):
        λ = srtf_group["arrival_rate"]
        lambda_values.append(λ)
        
        # SRTF
        srtf_times = [r["avg_waiting_time"] for r in srtf_group["results"]]
        srtf_waiting.append(np.mean(srtf_times))
        ci = stats.t.interval(0.95, len(srtf_times)-1, loc=np.mean(srtf_times), scale=stats.sem(srtf_times))
        srtf_ci.append((ci[1] - ci[0])/2)
        
        # FCFS
        fcfs_times = [r["avg_waiting_time"] for r in fcfs_group["results"]]
        fcfs_waiting.append(np.mean(fcfs_times))
        ci = stats.t.interval(0.95, len(fcfs_times)-1, loc=np.mean(fcfs_times), scale=stats.sem(fcfs_times))
        fcfs_ci.append((ci[1] - ci[0])/2)

    plt.figure(figsize=(12, 6))
    plt.errorbar(lambda_values, srtf_waiting, yerr=srtf_ci, fmt='-o', label='SRTF', capsize=5)
    plt.errorbar(lambda_values, fcfs_waiting, yerr=fcfs_ci, fmt='-s', label='FCFS', capsize=5)
    
    plt.xlabel('Tasa de llegada (λ)')
    plt.ylabel('Tiempo de espera promedio')
    plt.title('Comparación de SRTF vs FCFS: Tiempo de espera vs λ')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"{output_dir}/comparacion_srtf_vs_fcfs.png", dpi=300)
    plt.close()


def plot_context_switches(all_results, output_dir="./"):
    lambda_values = []
    mean_switches = []
    ci_switches = []

    for result_group in all_results:
        λ = result_group["arrival_rate"]
        lambda_values.append(λ)
        
        switches = [r["context_switches"] for r in result_group["results"]]
        mean = np.mean(switches)
        ci = stats.t.interval(0.95, len(switches)-1, loc=mean, scale=stats.sem(switches))
        
        mean_switches.append(mean)
        ci_switches.append((ci[1] - ci[0])/2)

    plt.figure(figsize=(10, 6))
    plt.errorbar(lambda_values, mean_switches, yerr=ci_switches, fmt='-o', color='red', capsize=5)
    
    plt.xlabel('Tasa de llegada (λ)')
    plt.ylabel('Número promedio de cambios de contexto')
    plt.title('Cambios de contexto en SRTF vs λ (con IC 95%)')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/context_switches_vs_lambda.png", dpi=300)
    plt.close()


def plot_execution_timeline(simulation, output_dir="./"):
    plt.figure(figsize=(14, 6))
    
    for process in simulation.srtf_scheduler.completed_processes: 
        plt.plot([process.arrival_time, process.start_time], 
                 [process.pid, process.pid], 
                 'k--', alpha=0.5)
        plt.plot([process.start_time, process.end_time], 
                 [process.pid, process.pid], 
                 linewidth=3, 
                 color='green' if process.remaining_time == 0 else 'blue')
        plt.plot(process.arrival_time, process.pid, 'ko', markersize=4)
        plt.plot(process.start_time, process.pid, '>', color='green')
        plt.plot(process.end_time, process.pid, 'x', color='red')
    
    plt.title('Timeline de Ejecución - SRTF')
    plt.xlabel('Tiempo')
    plt.ylabel('ID de Proceso')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/timeline_ejecucion_srtf.png", dpi=300)
    plt.close()