import random

# Name: Sorta Lucky Sort
# Author: Zach Hutton

def sorta_lucky_sort(original_list):
    """
Sort a list using a sorta lucky sorting algorithm.

Args:
    original_list (List): The original list to be sorted.

Returns:
    tuple: A tuple containing the sorted list and the number of attempts made during the sorting process.

Raises:
    None

Examples:
    >>> sorta_lucky_sort([4, 2, 1, 3])
    ([1, 2, 3, 4], 3)

    >>> sorta_lucky_sort([5, 3, 1, 4, 2])
    ([1, 2, 3, 4, 5], 6)
"""

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
            lst = lst[2:]

        # Merge the sorted sublists
        merged = [item for sublist in sorted_sublists for item in sublist]

        # Now, we need to ensure the merged list is fully sorted
        while not is_list_ordered(merged):
            random.shuffle(merged)
            total_attempts += 1  # Count this shuffle as an attempt

        return merged, total_attempts

    # Perform the sorting and get the number of attempts
    sorted_list, attempts = sort_process(original_list.copy())

    return sorted_list, attempts  # Returns the sorted list and the number of attempts

# Examples
print(sorta_lucky_sort([4, 2, 1, 3]))
print(sorta_lucky_sort([5, 3, 1, 4, 2]))