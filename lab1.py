def fcfs_scheduling():
    n = int(input("\nEnter the number of processes: "))
 
    processes = []
    print("\nEnter burst time for each process:")
    for i in range(n):
        burst = int(input(f"  Burst time for Process P{i + 1}: "))
        processes.append({
            "pid": f"P{i + 1}",
            "arrival": 0,       # All arrive at time 0 (non-preemptive assumption)
            "burst": burst,
        })
        processes.sort(key=lambda p: p["arrival"])
 
    current_time = 0
    for p in processes:
        # Start execution (no preemption, so wait if CPU is busy)
        if current_time < p["arrival"]:
            current_time = p["arrival"]
 
        p["start"]       = current_time
        p["finish"]      = current_time + p["burst"]
        p["turnaround"]  = p["finish"]  - p["arrival"]
        p["waiting"]     = p["turnaround"] - p["burst"]
 
        current_time = p["finish"]
 
    # --- Results Table ---
    print("\n" + "=" * 72)
    print(f"{'Process':<10}{'Arrival':>10}{'Burst':>10}{'Start':>10}"
          f"{'Finish':>10}{'Waiting':>10}{'Turnaround':>12}")
    print("-" * 72)
 
    total_waiting    = 0
    total_turnaround = 0
 
    for p in processes:
        print(f"{p['pid']:<10}{p['arrival']:>10}{p['burst']:>10}"
              f"{p['start']:>10}{p['finish']:>10}"
              f"{p['waiting']:>10}{p['turnaround']:>12}")
        total_waiting    += p["waiting"]
        total_turnaround += p["turnaround"]
 
    print("=" * 72)
 
    avg_waiting    = total_waiting    / n
    avg_turnaround = total_turnaround / n
 
    print(f"\n  Average Waiting Time    : {avg_waiting:.2f}")
    print(f"  Average Turnaround Time : {avg_turnaround:.2f}")
 
    # --- Gantt Chart ---
    print("\n--- Gantt Chart ---")
    bar = "|"
    timeline = " "
    for p in processes:
        width = max(p["burst"] * 2, len(p["pid"]) + 2)
        bar      += f" {p['pid']:^{width}} |"
        timeline += f"{p['start']:<{width + 2}}"
    timeline += str(processes[-1]["finish"])
 
    print(bar)
    print(timeline)
    print()
 
 
if __name__ == "__main__":
    fcfs_scheduling()