from basic_struct import Process
from fcfs import FCFS

if __name__ =="__main__":
    
    scheduler = FCFS()

    processes = [
        Process("P1", 0, 4),
        Process("P2", 1, 3),
        Process("P3", 2, 1),
        Process("P4", 3, 2),
        Process("P5", 4, 5),
    ]

    # Add them to the scheduler
    for p in processes:
        scheduler.add_process(p)

    # Run the scheduler
    scheduler.run()

    print("Execution Results (FCFS):\n")
    for p in scheduler.completed_processes:
        print(f"Process {p.pid}: Start = {p.start_time}, End = {p.end_time}, Arrival = {p.arrival_time}, Burst = {p.burst_time}")
        print(f"  -> Waiting Time: {p.waiting_time}, Turnaround Time: {p.turnaround_time}\n")
