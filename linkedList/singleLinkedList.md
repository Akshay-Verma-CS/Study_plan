
# Singly Linked List in Python

## Definition
A singly linked list is a linear data structure that consists of a sequence of elements, each pointing to the next. It is characterized by its efficiency in insertion and deletion operations.

## Basic Operations
1. **Insertion**: 
   - **At Head**: Adds a new node at the beginning of the list.
   - **At Tail**: Appends a new node at the end of the list.
   - **After a Node**: Inserts a new node after a specified node.
   - **Before a Node**: Inserts a new node before a specified node.

2. **Deletion**: 
   - **From the Head**: Removes the first node of the list.
   - **From the Tail**: Removes the last node of the list.
   - **Specific Node**: Deletes a node with a specific value.

3. **Traversal**:
   - Singly linked lists can only be traversed in one direction, from the head to the tail.

## Python Implementation
My Python implementation consists of two classes: `Node` and `LinkedList`.

- `Node` class represents the nodes in the linked list, with a `data` attribute for value storage and a `next` attribute pointing to the next node.

- `LinkedList` class manages the linked list operations such as insertion (`insertAtFront`, `insertAtRear`), searching (`searchVal`), deletion (`delVal`), and traversal (`printList`).

### Methods Explanation
- `getRearNode`: Finds the last node in the list.
- `searchVal`: Searches for a node with the specified value.
- `insertAtFront`: Adds a new node at the beginning of the list.
- `insertAtRear`: Appends a new node at the end of the list.
- `insertAfterVal`: Inserts a new node after a node with a specific value.
- `popFront`: Removes and returns the first node's value.
- `popRear`: Removes and returns the last node's value.
- `delVal`: Deletes a node with a specific value.
- `printList`: Prints the values of all nodes in the list.