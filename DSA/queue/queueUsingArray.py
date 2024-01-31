# Author: Akshay Verma
# GitHub: https://github.com/Akshay-Verma-CS
# Date of Creation: January 23, 2024

#the algorithm is referred from geekforgeeks.org

from typing import Any

class Queue:

    __front: int
    __rear: int 
    __count: int
    __queue: list[Any]
    __capacity: int

    def __init__(self,capacity: int) -> None:
        self.__front = 0
        self.__rear = capacity - 1
        self.__count = 0
        self.__queue = [None]*capacity
        self.__capacity = capacity

    def isFull(self) -> bool:
        return self.__count == self.__capacity
    
    def isEmpty(self):
        return self.__count == 0

    def enqueue(self,data:Any) -> None:
        if self.isFull():
            print("cannot enqueue as queue is full")
        else:
            self.__rear = (self.__rear + 1) % self.__capacity
            self.__queue[self.__rear] = data
            self.__count+=1
            print(f"successfully enqueued {data}")

    def dequeue(self) -> None:
        if self.isEmpty():
            print("No element to dequeue")
        else:
            self.__front = (self.__front + 1) % self.__capacity
            self.__count-=1
    
    def getFront(self) -> Any | None:
        return self.__queue[self.__front]
    
    def getRear(self) -> Any | None:
        return self.__queue[self.__rear]
    
