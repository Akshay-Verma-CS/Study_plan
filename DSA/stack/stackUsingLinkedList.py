# Author: Akshay Verma
# GitHub: https://github.com/Akshay-Verma-CS
# Date of Creation: January 21, 2024

from typing import Any

class Node:

    __data: Any
    
    def __init__(self,data: Any) -> None:
        self.__data = data
        self.__next: Node | None = None

class SimpleLinkedList:

    __head: Node | None

    def __init__(self) -> None:
        self.__head = None

    def insertAtFront(self,data: Any) -> None:
        newNode: Node = Node(data)
        newNode.__next = self.__head
        self.__head = newNode

    def popAtFront(self):
        val = self.__head.__data
        self.__head = self.__head.__next
        return val
    
    def getFrontElement(self) -> Any:
        if self.__head == None: return 
        return self.__head.__data
        


class Stack:

    __size: int
    __current_size: int
    __dynamic: bool
    __list: SimpleLinkedList

    def __init__(self,size,dynamic = False) -> None:
        self.__size = size
        self.__current_size = 0
        self.__dynamic = dynamic
        self.__list = SimpleLinkedList()

    def isEmpty(self) -> bool:
        if self.__current_size == 0:
            print("stack is empty")
            return True
        return False
    
    def push(self,data: Any) -> None:
        if self.__current_size == self.__size:
            if self.__dynamic:
                self.__size = 2 * self.__size
            else:
                print("stack overflow")
                return
        self.__list.insertAtFront(data)
        self.__current_size+=1

    def pop(self) -> Any | None:
        if self.isEmpty(): return
        self.__current_size-=1 
        return self.__list.popAtFront()
    
    def top(self) -> Any | None:
        if self.isEmpty(): return
        return self.__list.getFrontElement()
    
    def size(self) -> int:
        return self.__size

        
