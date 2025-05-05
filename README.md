# CPU-Scheduling-simulator
🔄 FCFS CPU Scheduling Simulator
This project is a command-line based CPU Scheduling Simulator that implements the First-Come-First-Serve (FCFS) scheduling algorithm using both Python and C++. It helps visualize how processes are scheduled by a CPU based on their arrival time and calculates key performance metrics.

📌 Features
User input for process details (Arrival Time and Burst Time)

Calculates:

Start Time

Completion Time

Turnaround Time (TAT)

Waiting Time (WT)

Displays a detailed process table

Shows a text-based Gantt Chart for visual representation

Computes average TAT and WT

🎯 Purpose
This simulator is designed for educational purposes to help students understand the working of FCFS scheduling in Operating Systems and how CPU time is distributed among processes.

🛠️ Tech Used
Python 3.x (for one version)

C++ (for another version)

No external libraries required

📥 Input
Number of processes

For each process:

Arrival Time

Burst Time

📤 Output
Start Time, Completion Time, Turnaround Time, Waiting Time

Average TAT and WT

Gantt Chart representing process execution timeline

📚 How It Works
Processes are sorted by Arrival Time and scheduled one-by-one. If the CPU is idle, it waits until the next process arrives. All time metrics are calculated sequentially, and the final results are shown in a tabular format and a simple Gantt chart.

