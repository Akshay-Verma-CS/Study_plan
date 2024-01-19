# Algorithm Complexity Chart

Below is a chart that lists the time and space complexity for several popular algorithms in computer science.

| Algorithm                    | Best Time Complexity | Average Time Complexity | Worst Time Complexity | Space Complexity |
|------------------------------|----------------------|-------------------------|-----------------------|------------------|
| **Sorting Algorithms**       |                      |                         |                       |                  |
| Bubble Sort                  | O(n)                 | O(n^2)                  | O(n^2)                | O(1)             |
| Insertion Sort               | O(n)                 | O(n^2)                  | O(n^2)                | O(1)             |
| Selection Sort               | O(n^2)               | O(n^2)                  | O(n^2)                | O(1)             |
| Merge Sort                   | O(n log n)           | O(n log n)              | O(n log n)            | O(n)             |
| Quick Sort                   | O(n log n)           | O(n log n)              | O(n^2)                | O(log n)         |
| Heap Sort                    | O(n log n)           | O(n log n)              | O(n log n)            | O(1)             |
| **Search Algorithms**        |                      |                         |                       |                  |
| Linear Search                | O(1)                 | O(n)                    | O(n)                  | O(1)             |
| Binary Search                | O(1)                 | O(log n)                | O(log n)              | O(1)             |
| **Graph Algorithms**         |                      |                         |                       |                  |
| Breadth-First Search (BFS)   | O(V + E)             | O(V + E)                | O(V + E)              | O(V)             |
| Depth-First Search (DFS)     | O(V + E)             | O(V + E)                | O(V + E)              | O(V)             |
| Dijkstra's Algorithm         | O(V^2)               | O((V+E) log V)          | O((V+E) log V)        | O(V)             |
| **Data Structure Operations**|                      |                         |                       |                  |
| Binary Heap (Insert/Delete)  | O(log n)             | O(log n)                | O(log n)              | O(n)             |
| Balanced Binary Tree Search  | O(log n)             | O(log n)                | O(log n)              | O(n)             |
| Hash Table (Insert/Search)   | O(1)                 | O(1)                    | O(n)                  | O(n)             |

Note: V represents the number of vertices and E represents the number of edges in a graph.

## Explanation of Each Algorithm

### Sorting Algorithms
- **Bubble Sort**: A simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order.
- **Insertion Sort**: Builds the final sorted array one item at a time, with the assumption that the first element is already sorted.
- **Selection Sort**: Divides the input list into two parts: a sorted sublist of items which is built up from left to right and a sublist of the remaining unsorted items.
- **Merge Sort**: A divide and conquer algorithm that divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves.
- **Quick Sort**: Selects a 'pivot' element from the array and partitions the other elements into two sub-arrays, according to whether they are less than or greater than the pivot.
- **Heap Sort**: Builds a heap from the input data and then repeatedly extracts the maximum element from the heap and rebuilds the heap.

### Search Algorithms
- **Linear Search**: A method for finding a target value within a list by checking each element sequentially.
- **Binary Search**: Searches a sorted array by repeatedly dividing the search interval in half, beginning with the whole array.

### Graph Algorithms
- **Breadth-First Search (BFS)**: An algorithm for traversing or searching tree or graph data structures, starting from the root node and exploring all of the neighbor nodes at the present depth before moving on to nodes at the next depth level.
- **Depth-First Search (DFS)**: An algorithm for traversing or searching tree or graph data structures in which it starts at the root node and explores as far as possible along each branch before backtracking.
- **Dijkstra's Algorithm**: An algorithm for finding the shortest paths between nodes in a graph, which may represent, for example, road networks.

### Data Structure Operations
- **Binary Heap Operations**: Insertion and deletion operations in a binary heap data structure, which is a complete binary tree that satisfies the heap property.
- **Balanced Binary Tree Search**: Searching for an element in a balanced binary tree like an AVL tree or a Red-Black tree, where the tree maintains its height to be logarithmic of the number of elements.
- **Hash Table Operations**: Insertion and search operations in a hash table, which is a data structure that implements an associative array abstract data type, a structure that can map keys to values.

---

Remember that the time complexity is a way to describe how an algorithm's runtime increases as the size of the input increases, and the space complexity describes how much additional memory the algorithm needs.
