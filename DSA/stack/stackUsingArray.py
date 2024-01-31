# Author: Akshay Verma
# GitHub: https://github.com/Akshay-Verma-CS
# Date of Creation: January 21, 2024

from typing import Any

class Stack:

    __size: int
    __arr: list
    __current_size: int
    __dynamic: bool

    def __init__(self,size,dynamic = False) -> None:
        self.__size = size
        self.__current_size = 0
        self.__dynamic = dynamic

    def push(self,data: Any) -> None:
        if self.__current_size == self.__size:
            if self.__dynamic:
                self.___size = 2 * self.___size
            else:
                print("stack overflow")
                return
        self.__arr.append(data)
        self.__current_size+=1
    
    def pop(self) -> Any | None:
        if self.isEmpty(): print("No element to pop")
        else:
            self.__current_size-=1
            return self.__arr.pop()
        
    def top(self) -> Any | None:
        if self.isEmpty(): print("stack is empty")
        else: return self.__arr[-1]
        
    def isEmpty(self) -> bool:
        if self.__current_size == 0: return True
        return False
    
    def size(self) -> int:
        return self.__size

    
        