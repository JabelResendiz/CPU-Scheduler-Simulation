from basic_struct import Process
from fcfs import FCFS
from sjf import SJF
from roundRobin import RoundRobin

if __name__ =="__main__":
    
    # scheduler = FCFS()

    # processes = [
    #     Process("P1", 0, 4),
    #     Process("P2", 1, 3),
    #     Process("P3", 2, 1),
    #     Process("P4", 3, 2),
    #     Process("P5", 4, 5),
    # ]

    # # Add them to the scheduler
    # for p in processes:
    #     scheduler.add_process(p)

    # # Run the scheduler
    # scheduler.run()

    # print("Execution Results (FCFS):\n")
    # for p in scheduler.completed_processes:
    #     print(f"Process {p.pid}: Start = {p.start_time}, End = {p.end_time}, Arrival = {p.arrival_time}, Burst = {p.burst_time}")
    #     print(f"  -> Waiting Time: {p.waiting_time}, Turnaround Time: {p.turnaround_time}\n")
    



    # processes = [
    #     Process("P1", 0, 6),  
    #     Process("P2", 1, 8),
    #     Process("P3", 2, 7),
    #     Process("P4", 3, 3),
    #     Process("P5", 89, 4),
    # ]
    
    # sjf_scheduler = SJF()
    
    # for process in processes:
    #     sjf_scheduler.add_process(process)
    
    # sjf_scheduler.run()

    # print("Execution Results (SJF):")
    # for process in sjf_scheduler.completed_processes:
    #     print(f"Process {process.pid}: Start = {process.start_time}, End = {process.end_time}, Arrival = {process.arrival_time}, Burst = {process.burst_time}")
    #     print(f"  -> Waiting Time: {process.waiting_time}, Turnaround Time: {process.turnaround_time}\n")

    



    processes = [
        Process("P1", 0, 6),  
        Process("P2", 1, 8),
        Process("P3", 2, 7),
        Process("P4", 3, 3),
        Process("P5", 8, 10),
    ]


    round_scheduler = RoundRobin(3)

    for process in processes:
        round_scheduler.add_process(process)
    
    round_scheduler.run()

    print("Execution Results ():")
    for process in round_scheduler.completed_processes:
        print(f"Process {process.pid}: Start = {process.start_time}, End = {process.end_time}, Arrival = {process.arrival_time}, Burst = {process.burst_time}")
        print(f"  -> Waiting Time: {process.waiting_time}, Turnaround Time: {process.turnaround_time}\n")
