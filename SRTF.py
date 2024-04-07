class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time


def srtf(processes):
    processes.sort(key=lambda x: x.arrival_time)
    total_processes = len(processes)
    current_time = 0
    waiting_time = 0
    completed_processes = 0
    ready_queue = []

    while completed_processes < total_processes:
        for process in processes:
            if process.arrival_time <= current_time and process not in ready_queue:
                ready_queue.append(process)

        if len(ready_queue) == 0:
            current_time += 1
            continue

        ready_queue.sort(key=lambda x: x.remaining_time)
        current_process = ready_queue[0]
        ready_queue.pop(0)

        waiting_time += current_time - current_process.arrival_time
        current_time += current_process.remaining_time
        current_process.remaining_time = 0
        completed_processes += 1

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

    avg_waiting_time = srtf(processes)
    print("Задание 2 -> Среднее время ожидания процесса (waiting time) при использовании SRTF:", avg_waiting_time)