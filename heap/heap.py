# Author: Akshay Verma
# GitHub: https://github.com/Akshay-Verma-CS
# Date of Creation: January 30, 2024

# please refer from https://docs.python.org/3/library/heapq.html

# I have decided to use library function because there is no need to waste time when you can implement binary tree

from heapq import heapify,heappop,heappush,nlargest,nsmallest
from typing import Any

class Heap:

    __heap: None | list[int]

    def __init__(self) -> None:
        self.__heap = None

    def heapify(self,arr: list[int]) -> None:
        self.__heap = arr
        heapify(arr)

    def insert(self, val: int) -> None:
        heappush(self.__heap,val)
    
    def delete(self) -> int:
        return heappop(self.__heap)
    
    def getNLargest(self,n: int) -> list[int]:
        return nlargest(n,self.__heap)
    
    def getNSmallest(self,n: int) -> list[int]:
        return nsmallest(n,self.__heap)
    
    def getSmallest(self) -> int:
        return nsmallest(1,self.__heap)[0]
    
    def getLargest(self) -> int:
        return nlargest(1,self.__heap)[0]