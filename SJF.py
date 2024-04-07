class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time


def sjf(processes):
    processes.sort(
        key=lambda x: (x.arrival_time, x.burst_time))
    total_processes = len(processes)
    current_time = 0
    waiting_time = 0

    for process in processes:
        current_time = max(current_time, process.arrival_time)
        waiting_time += current_time - process.arrival_time
        current_time += process.burst_time

    average_waiting_time = waiting_time / total_processes
    return average_waiting_time


if __name__ == "__main__":
    processes = [
        Process(1, 1, 1),
        Process(2, 4, 3),
        Process(3, 2, 4),
        Process(4, 3, 2),
        Process(5, 0, 7)
    ]

    avg_waiting_time = sjf(processes)
    print("Задание 3 -> Среднее время ожидания процесса (waiting time) при использовании SJF:", avg_waiting_time)
