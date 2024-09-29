
# README for Assignment 6

This repository includes the implementation of **Selection Algorithms** and **Elementary Data Structures**. Below are the steps to run the code, along with a summary of the algorithms and data structures covered in this assignment.

## Part 1: Selection Algorithms

### Description
In Part 1, we implemented two important algorithms for selecting the \(k^{th}\) smallest element in an array:
1. **Median of Medians Algorithm**: A deterministic algorithm ensuring worst-case linear time complexity (O(n)) for selecting the median.
2. **Quickselect Algorithm**: A randomized algorithm that provides expected linear time complexity in average cases but can degrade to O(n²) in the worst case.

### Files
- **Ass 6 Part 1.py**: This script contains the implementation of both the **deterministic** and **randomized** selection algorithms. It also includes a benchmarking function to compare the runtime performance of both algorithms on various input arrays.

### How to Run
1. Install Python 3.
2. Download or clone this repository.
3. Navigate to the directory in your terminal or command prompt.
4. Run the file `Ass 6 Part 1.py` by using the following command:
    ```bash
    python Ass 6 Part 1.py
    ```

### Summary of Findings
- **Quickselect** is faster on average but may suffer from poor performance in worst-case scenarios (reverse-sorted arrays).
- **Median of Medians** guarantees worst-case linear time, making it more reliable in situations where worst-case performance matters.

The benchmarking results demonstrate that Quickselect generally performs better with random inputs, while Median of Medians shows consistent performance across all input types.

---

## Part 2: Elementary Data Structures

### Description
Part 2 focuses on implementing and analyzing the performance of basic data structures, including:
- **Array and Matrices**: Arrays for sequential data storage and matrices for two-dimensional data handling.
- **Stacks**: A LIFO (Last-In-First-Out) data structure.
- **Queues**: A FIFO (First-In-First-Out) data structure.
- **Linked Lists**: Singly linked lists for dynamic memory management.
- **Rooted Trees**: Trees for representing hierarchical data.

### Files
- **Ass 6 Part 2.py**: This script contains the implementation of all the data structures listed above, along with examples demonstrating their use.

### How to Run
1. Ensure Python 3 is installed on your system.
2. Download or clone this repository.
3. Navigate to the directory in your terminal.
4. Execute the `Ass 6 Part 2.py` file using this command:
    ```bash
    python Ass 6 Part 2.py
    ```

### Summary of Findings
- **Arrays** provide O(1) time complexity for access but are inefficient for insertions and deletions (O(n) in the worst case).
- **Stacks and Queues** offer efficient O(1) time complexity for insertions and deletions due to their LIFO and FIFO nature.
- **Linked Lists** are useful for dynamic memory allocation, allowing O(1) insertions and deletions but suffering from O(n) time for access.
- **Rooted Trees** are essential for representing hierarchical data and are commonly used in algorithms like search trees, file systems, and decision-making processes.

Each data structure has its own set of trade-offs, and choosing the right one depends on the specific use case.

---

## Conclusion
This repository provides a comprehensive exploration of selection algorithms and elementary data structures. Each part covers the implementation, performance analysis, and practical applications of these algorithms and structures. By following the steps above, you can run the code and observe the behavior of these fundamental concepts in action.

Feel free to fork this repository to add improvements or experiment with different data structures and algorithms.

