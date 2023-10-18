# SortaLucky Sort Algorithm

SortaLucky is a unique sorting algorithm that combines deterministic and non-deterministic elements for sorting a list of items. It partially shuffles the list, sorts elements in small segments, and progressively builds a fully sorted list. This repository contains the implementation of SortaLucky, along with a comparison script that contrasts its performance with that of Bogo Sort.

## Features

- **Innovative Approach:** SortaLucky introduces randomness in sorting pairs and strategically merges these pairs, offering a balance between complete randomness and traditional deterministic sorting.
- **Performance Analysis:** The repository includes a script for comparing SortaLucky's performance with the well-known Bogo Sort algorithm.

## Files in this Repository

- `sorta_lucky.py` - Contains the implementation of the SortaLucky algorithm.
- `comparison.py` - A script that compares the performance of SortaLucky with Bogo Sort, using various list sizes and providing visual data through plots.

## Usage

### Running SortaLucky

To use the SortaLucky algorithm, you need to import the function from the `sorta_lucky.py` script and then call it with a list you want to sort. Here's an example:

```python
from sorta_lucky import sorta_lucky_sort

my_list = [4, 2, 3, 1]
sorted_list, attempts = sorta_lucky_sort(my_list)

print(f"Sorted List: {sorted_list}")
print(f"Number of Attempts: {attempts}")
```

## Performance Comparison

To compare the performance of SortaLucky with Bogo Sort, run the comparison.py script. This script uses matplotlib to generate plots showing the number of attempts and time taken for each algorithm to sort lists of various sizes.

```
python comparison.py
```

This will execute the comparison script, and you'll see the performance plots on your screen.
