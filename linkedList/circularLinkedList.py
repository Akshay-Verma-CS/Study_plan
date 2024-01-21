# Author: Akshay Verma
# GitHub: https://github.com/Akshay-Verma-CS
# Date of Creation: January 21, 2024

from typing import Any

class Node:

    _data: Any

    def __init__(self,data) -> None:
        self._data = data
        self._next: Node | None = None

    
class CircularLinkedList:

    _head: Node | None

    def __init__(self) -> None:
        self._head = None

    def traverse(self,data = None, print = True, prev = False) -> list[Node] | Node | None:
        if self._head == None:
            print("empty circularLinkedList")
            return
        pointer: Node | None = self._head
        while pointer._next != self._head or pointer._data != data:
            if print == True: print(pointer._data,end=" ")
            prev: Node = pointer
            pointer = pointer._next
        if data != None and pointer._data != data:
            print(f"{data} not found in circularLinkedList")
            return
        if prev == True:
            return prev,pointer
        return pointer
    
    def insertAtFront(self,data) -> None:
        newNode: Node = Node(data)
        if self._head == None:
            self._head = newNode
            return
        newNode._next = self._head
        self._head = newNode
    
    def insertAtRear(self,data) -> None:
        newNode: Node = Node(data)
        if self._head == None:
            self._head == newNode
            return
        rearNode: Node = self.traverse()
        newNode._next = rearNode._next
        rearNode._next = newNode

    def insertAfterVal(self,data) -> None:
        newNode: Node = Node(data)
        desiredNode: Node = self.traverse(data = data)
        newNode._next = desiredNode._next
        desiredNode._next = newNode

    def popFront(self,data) -> Any | None:
        if self._head == None:
            print("empty circularLinkedList")
            return
        rearNode: Node = self.traverse()
        rearNode._next = self._head._next
        val: Any = self._head._data
        self._head = self._head._next
        return val

    def popRear(self,data) -> Any | None:
        if self._head == None:
            print("empty circularLinkedList")
            return
        prevNode,rearNode: Node = self.traverse(prev = True)
        val = rearNode._data
        prevNode._next = rearNode._next
        self._head = rearNode._next
        return val

    def popVal(self,data) -> Any | None:
        if self._head == None:
            print("empty circularLinkedList")
            return
        prevNode,desiredNode: Node = self.traverse(data = data, prev = True)
        val = desiredNode._data
        prevNode._next = desiredNode._next
        if desiredNode == self._head:
            self._head = desiredNode._next
        return val
    
    def printList(self) -> None:
        self.traverse(print=True)

        





    
        