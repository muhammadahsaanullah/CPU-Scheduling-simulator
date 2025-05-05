def fcfs_scheduling(processes):
    processes.sort(key=lambda x: x['arrival'])

    current_time = 0
    for process in processes:
        if current_time < process['arrival']:
            current_time = process['arrival']

        process['start'] = current_time
        process['completion'] = current_time + process['burst']
        process['turnaround'] = process['completion'] - process['arrival']
        process['waiting'] = process['turnaround'] - process['burst']
        current_time = process['completion']


def print_results(processes):
    print("\nFinal Process Table:")
    print(f"{'PID':<10}{'Arrival':<10}{'Burst':<10}{'Start':<10}"
          f"{'CT':<15}{'TAT':<15}{'WT':<10}")
    total_tat = 0
    total_wt = 0

    for p in processes:
        total_tat += p['turnaround']
        total_wt += p['waiting']
        print(f"{p['pid']:<10}{p['arrival']:<10}{p['burst']:<10}{p['start']:<10}"
              f"{p['completion']:<15}{p['turnaround']:<15}{p['waiting']:<10}")

    avg_tat = total_tat / len(processes)
    avg_wt = total_wt / len(processes)
    print(f"\nAverage Turnaround Time: {avg_tat:.2f}")
    print(f"Average Waiting Time: {avg_wt:.2f}")


def main():
    processes = []
    n = int(input("Enter the number of processes: "))

    for i in range(n):
        print(f"\nEnter details for Process {i+1}")
        pid = f"P{i+1}"
        arrival = int(input("Arrival Time: "))
        burst = int(input("Burst Time: "))
        processes.append({
            'pid': pid,
            'arrival': arrival,
            'burst': burst
        })

    fcfs_scheduling(processes)
    print_results(processes)


if __name__ == "__main__":
    main()
