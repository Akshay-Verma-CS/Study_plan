# Author: Akshay Verma
# GitHub: https://github.com/Akshay-Verma-CS
# Date of Creation: January 23, 2024

from typing import Any

class Node:

    __data:Any

    def __init__(self,data: Any) -> None:
        self.__data = data
        self.__next: Node | None = None

class Queue:

    __head: Node | None
    __capacity: int
    __count: int
    __front: Any | None
    __rear: Any | None

    def __init__(self,capacity: int) -> None:
        self.__head == None
        self.__capacity = capacity
        self.__count = 0

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
    
    def isEmpty(self) ->  bool:
        return self.__head == None
    
    def isFull(self) -> bool:
        return self.__count == 0
    
    def enqueue(self,data: Any) -> None:
        if self.isFull():
            print("queue is full")
        newNode: Node = Node(data)
        rearNode: Node | None = self.traverse()
        if rearNode == None:
            self.__head = newNode
            newNode.__next = self.__head
            self.__rear = self.__front = newNode.__data
        else:
            rearNode.__next = newNode
            newNode.__next = self.__head
            self.__head = newNode
            self.__rear
    
    def dequeue(self) -> None:
        pass