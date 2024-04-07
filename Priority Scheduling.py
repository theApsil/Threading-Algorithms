class Process:
    def __init__(self, pid, arrival_time, burst_time, priority):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.remaining_time = burst_time


def priority_scheduling(processes):
    processes.sort(
        key=lambda x: (x.arrival_time, -x.priority))  # сортируем процессы по времени поступления и убыванию приоритета
    total_processes = len(processes)
    current_time = 0
    turnaround_time = 0
    completed_processes = 0
    ready_queue = []

    while completed_processes < total_processes:
        for process in processes:
            if process.arrival_time <= current_time and process not in ready_queue:
                ready_queue.append(process)

        if len(ready_queue) == 0:
            current_time += 1
            continue

        ready_queue.sort(key=lambda x: x.priority)
        current_process = ready_queue[0]
        ready_queue.pop(0)

        turnaround_time += current_time + current_process.remaining_time - current_process.arrival_time
        current_time += current_process.remaining_time
        current_process.remaining_time = 0
        completed_processes += 1

    average_turnaround_time = turnaround_time / total_processes
    return average_turnaround_time


if __name__ == "__main__":
    processes = [
        Process(1, 3, 8, 0),
        Process(2, 5, 4, 1),
        Process(3, 0, 4, 2),
        Process(4, 2, 2, 4),
        Process(5, 4, 3, 3)
    ]

    avg_turnaround_time = priority_scheduling(processes)
    print("Задание 1 -> Среднее время между стартом процесса и его завершением при использовании Priority Scheduling:",
          avg_turnaround_time)
