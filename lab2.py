# Non-Preemptive SJF Scheduling
# All processes arrive at the same time (time 0):

n=int(input("\nEnter number of processes:"))
processes=[]
for i in range(n):
        burst_time=int(input(f"Enter burst time for process p{i+1}:"))
        processes.append({
            "pid":f"p{i+1}",
            "burst_time":burst_time
        })
# Sort by burst time
# Python's sort is stable, so if two burst times are the same,
# their original order is preserved (FCFS)
processes.sort(key=lambda x:x["burst_time"])

#calculate waiting time and turnaround time
waiting_time=0
total_waiting_time=0
total_turnaround_time=0
for process in processes:
    process["waiting_time"]=waiting_time
    process["turnaround_time"]=process["waiting_time"]+process["burst_time"]
    
    total_waiting_time+=process["waiting_time"]
    total_turnaround_time+=process["turnaround_time"]

    waiting_time+=process["burst_time"]

#display scheduling results
print("\nSJF Scheduling Order:")
for process in processes:
    print(process["pid"],end="")
print()
print("\nProcess\tBurst Time\tWaiting Time\tTurnaround Time")
for process in processes:
    print(f"{process['pid']}\t{process['burst_time']}\t\t{process['waiting_time']}\t\t{process['turnaround_time']}")

# Display averages
average_waiting_time = total_waiting_time / n
average_turnaround_time = total_turnaround_time / n

print(f"\nAverage Waiting Time = {average_waiting_time:.2f}")
print(f"Average Turnaround Time = {average_turnaround_time:.2f}")