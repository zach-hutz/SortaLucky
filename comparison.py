import random
import time
import matplotlib.pyplot as plt

def is_ordered(num_list):
    if len(num_list) < 2:
        return True
    for i in range(len(num_list) - 1):
        if num_list[i] > num_list[i + 1]:
            return False
    return True

def bogo_sort(num_list):
    attempts = 0
    start_time = time.time()
    while not is_ordered(num_list):
        random.shuffle(num_list)
        attempts += 1
    end_time = time.time()
    return attempts, end_time - start_time  # attempts and duration

def sorta_lucky_sort(original_list):
    def is_list_ordered(lst):
        return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))

    def sort_process(lst):
        total_attempts = 0  # Initialize the attempt counter
        sorted_sublists = []
        while lst:
            if len(lst) == 1:
                sorted_sublists.append(lst)
                break

            # Sort the first two elements
            pair = lst[:2]
            while not is_list_ordered(pair):
                random.shuffle(pair)
                total_attempts += 1  # Count this shuffle as an attempt

            sorted_sublists.append(pair)
            print("Sorted sublists:", sorted_sublists)
            lst = lst[2:]

        # Merge the sorted sublists
        merged = [item for sublist in sorted_sublists for item in sublist]

        # Now, we need to ensure the merged list is fully sorted
        while not is_list_ordered(merged):
            random.shuffle(merged)
            total_attempts += 1  # Count this shuffle as an attempt

        return merged, total_attempts

    # Record the start time
    start_time = time.time()

    # Perform the sorting and get the number of attempts
    sorted_list, attempts = sort_process(original_list.copy())

    # Record the end time
    end_time = time.time()

    return attempts, end_time - start_time, sorted_list  # attempts, duration, and the sorted list

def compare_sorts(list_size, num_trials):
    results = {
        'bogo': {'attempts': [], 'times': []},
        'sorta_lucky': {'attempts': [], 'times': []}
    }

    for _ in range(num_trials):
        list_x = list(range(1, list_size + 1))
        random.shuffle(list_x)

        # Bogo sort
        attempts, duration = bogo_sort(list_x.copy())
        results['bogo']['attempts'].append(attempts)
        results['bogo']['times'].append(duration)

        # SortaLucky sort
        attempts, duration, _ = sorta_lucky_sort(list_x.copy())
        results['sorta_lucky']['attempts'].append(attempts)
        results['sorta_lucky']['times'].append(duration)

    return results

def run_scalability_test(max_list_size, num_trials):
    list_sizes = range(2, max_list_size + 1)  # Testing list sizes from 2 to max_list_size
    bogo_results = {'attempts': [], 'times': []}
    sorta_lucky_results = {'attempts': [], 'times': []}

    for size in list_sizes:
        print(f"Testing list size: {size}")  # So you can observe the progress

        # Get average attempts and time for each list size by running num_trials for each
        results = compare_sorts(size, num_trials)

        # Store the average results for this list size
        bogo_results['attempts'].append(sum(results['bogo']['attempts']) / num_trials)
        bogo_results['times'].append(sum(results['bogo']['times']) / num_trials)

        sorta_lucky_results['attempts'].append(sum(results['sorta_lucky']['attempts']) / num_trials)
        sorta_lucky_results['times'].append(sum(results['sorta_lucky']['times']) / num_trials)

    # Once all data is collected, plot the results
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)  # subplot for attempts
    plt.plot(list_sizes, bogo_results['attempts'], marker='o', label='Bogo Sort')
    plt.plot(list_sizes, sorta_lucky_results['attempts'], marker='o', label='SortaLucky Sort')
    plt.xlabel('List Size')
    plt.ylabel('Average Number of Attempts')
    plt.title('Scalability: Attempts')
    plt.legend()
    plt.grid(True)

    plt.subplot(1, 2, 2)  # subplot for time
    plt.plot(list_sizes, bogo_results['times'], marker='o', label='Bogo Sort')
    plt.plot(list_sizes, sorta_lucky_results['times'], marker='o', label='SortaLucky Sort')
    plt.xlabel('List Size')
    plt.ylabel('Average Time (seconds)')
    plt.title('Scalability: Time')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()

def main():
    list_size = 9
    num_trials = 5
    results = compare_sorts(list_size, num_trials)

    # Printing the average results
    print('Bogo Sort - Average attempts:', sum(results['bogo']['attempts']) / num_trials)
    print('Bogo Sort - Average time:', sum(results['bogo']['times']) / num_trials)
    print('SortaLucky Sort - Average attempts:', sum(results['sorta_lucky']['attempts']) / num_trials)
    print('SortaLucky Sort - Average time:', sum(results['sorta_lucky']['times']) / num_trials)

    print("Starting scalability test...")
    run_scalability_test(list_size, num_trials)

if __name__ == "__main__":
    main()
