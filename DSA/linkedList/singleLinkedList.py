# Author: Akshay Verma
# GitHub: https://github.com/Akshay-Verma-CS
# Date of Creation: January 21, 2024

from typing import Any
class Node:

    def __init__(self,data):
        self.data: Any = data
        self.next: Node | None = None


class LinkedList:

    _head: Node | None

    def __init__(self) -> None:
        self._head: Node | None = None

    def getRearNode(self) -> Node:
        if self._head == None: return self._head
        pointer: Node = self._head
        while pointer.next != None:
            pointer = pointer.next
        return pointer
    
    def searchVal(self,val) -> Node:
        pointer:Node = self._head
        while pointer.data != val:
            # check if we have reached the end of linkedList and still not found val
            if pointer.next == None:
                return None
            pointer = pointer.next
        return pointer

    def insertAtFront(self,data) -> None:
        newNode: Node = Node(data)
        newNode.next = self._head
        self._head = newNode

    def insertAtRear(self,data) -> None:
        newNode: Node = Node(data)
        rearNode: Node = self.getRearNode()
        if rearNode == None:
            self._head = newNode
            return
        rearNode.next = newNode
    
    def insertAfterVal(self,data,val) -> None:
        newNode: Node = Node(data)
        pointer: Node | None = self.searchVal(val)
        if pointer == None:
            print(f"{val} not found")
            return
        newNode.next = pointer.next
        pointer.next = newNode

    def popFront(self) -> Any:
        if self._head == None:
            print("empty linkedList, nothing to pop")
        val = self._head.data
        self._head = self._head.next
        return val
    
    def popRear(self) -> Any:
        if self._head == None:
            print("empty linkedList, nothing to pop")
        pointer: Node = self._head
        while pointer.next != None:
            previousNode: Node = pointer
            pointer = pointer.next
        previousNode.next = None
        return pointer.data
    
    def delVal(self,val) -> None:
        if self._head == None:
            print("empty linkedList, nothing to delete")
        pointer: Node  = self._head
        while pointer.data != val:
            previousNode : Node = pointer
            pointer = pointer.next
        previousNode.next = pointer.next

    def printList(self) -> None:
        if self._head == None:
            print("empty linkedList")
            return
        pointer: Node | None = self._head
        while True:
            print(pointer.data,end=" ")
            pointer = pointer.next
            if pointer == None:
                break


# driver code to test list
            
sll : LinkedList = LinkedList()

# print Empty linked list 
sll.printList()

# add newNode
sll.insertAtRear(3)

# add at front
sll.insertAtFront(1)

sll.insertAtRear(4)

sll.insertAfterVal(2,1)

# checking insertFunctions should return 1 2 3 4
sll.printList()


#del rear Node , should print 4
print(f"deleted rear node - {sll.popRear()}")
#del front Node , should print 1
print(f"deleted front node - {sll.popFront()}")
# del 3 , will print del val None because delVal has return type void
print(f"del val {sll.delVal(3)}")

#should print 2
sll.printList()





        


        
        
        

        