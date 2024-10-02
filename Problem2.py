from collections import deque

def time_to_print(n, m, priorities):
    queue = deque([(priority, index) for index, priority in enumerate(priorities)])
    count = 0

    while queue:
        job = queue.popleft()
        # Check if there is any job with higher priority in the queue
        if any(job[0] < other_job[0] for other_job in queue):
            queue.append(job)  # Re-add the job to the end of the queue
        else:
            count += 1  # The job is printed
            if job[1] == m:  # If this job is the target job
                return count

def main():
    # Read input from a file
    with open('input2.txt', 'r') as file:
        data = file.readlines()

    results = []

    for i in range(0, len(data), 2):
        n, m = map(int, data[i].split())
        priorities = list(map(int, data[i + 1].split()))
        result = time_to_print(n, m, priorities)
        results.append(result)

    for result in results:
        print(result)

if __name__ == "__main__":
    main()
