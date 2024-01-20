# Author: Akshay Verma
# GitHub: https://github.com/Akshay-Verma-CS
# Date of Creation: January 21, 2024

from typing import Any

class Node:

    _data: Any 

    def __init__(self,data) -> None:
        self._data: Any = data
        self._prev: Node | None = None
        self._next: Node | None = None


class DoubleLinkedList:

    _head: Node | None

    def __init__(self) -> None:
        self._head = None

    """
    this method will be used to traverse the array, if data is true it will traverse upto that else will traverse whole list,
    if print is true it will print traversed data 
    """
    def traverse(self,data = None, print = False) -> Node | None:
        pointer: Node | None = self._head
        while pointer.next != None or pointer.data != data:
            if print == True: print(pointer.data)
            pointer = pointer._next
        if data != None and pointer._next == None and pointer._data != data:
            print(f"{val} not found in doubleLinkedList")
            return None
        return pointer


    def insertAtFront(self,data: Any) -> None:
        newNode: Node = Node(data)
        self._head._prev = newNode
        newNode._next = self._head
        self._head = newNode

    def insertAtRear(self,data:Any) -> None:
        newNode: Node = Node(data)
        if self._head == None: self._head = newNode
        rearNode: Node = self.traverse()
        newNode._prev = rearNode
        rearNode._next = newNode
    
    def insertAfterVal(self,data: Any,val: Any) -> None:
        newNode: Node = Node(data)
        node: Node | None = self.traverse(data=val)
        if node == None: return
        newNode._next = node._next
        newNode._prev = node
        node._next = newNode

    def popFront(self) -> Any:
        if self._head == None:
            print("empty doubleLinkedList")
        data: Any = self._head._data
        self._head = self._head._next
        return data
    
    def popRear(self) -> Any:
        if self._head == None:
            print("empty doubleLinkedList")
        rearNode: Node = self.traverse()
        data: Any = rearNode._data
        rearNode._prev._next = None
        return data
    
    def popVal(self,val: Any) -> Any:
        if self._head == None:
            print("empty doubleLinkedList")
        desiredNode: Node = self.traverse(data=val)
        desiredNode._prev._next = desiredNode._next
        desiredNode._next._prev = desiredNode._prev
        return desiredNode._data
    
    def printList(self) -> None:
        self.traverse(print=True)

    def searchVal(self,val) -> Node | None:
        return self.traverse(data=val)
    
    def appendList(self, list: Any) -> None:
        rearNode: Node = self.traverse()
        list._next = list
        list._prev = rearNode


        

        

    



    