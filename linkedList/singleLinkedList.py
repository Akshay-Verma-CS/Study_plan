class Node:

    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def getRearNode(self):
        if self.head == None: return self.head
        pointer: Node = self.head
        while pointer.next != None:
            pointer = pointer.next
        return pointer
    
    def searchVal(self,val):
        pointer:Node = self.head
        while pointer.data != val:
            # check if we have reached the end of linkedList and still not found val
            if pointer.next == None:
                return None
            pointer = pointer.next
        return pointer

    def insertAtFront(self,data):
        newNode: Node = Node(data)
        newNode.next = self.head
        self.head = newNode

    def insertAtRear(self,data):
        newNode: Node = Node(data)
        rearNode: Node = self.getRearNode()
        if rearNode == None:
            self.head = newNode
            return
        rearNode.next = newNode
    
    def insertAfterVal(self,data,val):
        newNode: Node = Node(data)
        pointer: Node | None = self.searchVal(val)
        if pointer == None:
            print(f"{val} not found")
            return
        newNode.next = pointer.next
        pointer.next = newNode

    def popFront(self):
        if self.head == None:
            print("empty linkedList, nothing to pop")
        val = self.head.data
        self.head = self.head.next
        return val
    
    def popRear(self):
        if self.head == None:
            print("empty linkedList, nothing to pop")
        pointer: Node = self.head
        while pointer.next != None:
            previousNode: Node = pointer
            pointer = pointer.next
        previousNode.next = None
        return pointer.data
    
    def delVal(self,val):
        if self.head == None:
            print("empty linkedList, nothing to delete")
        pointer: Node  = self.head
        while pointer.data != val:
            previousNode : Node = pointer
            pointer = pointer.next
        previousNode.next = pointer.next

    def printList(self):
        if self.head == None:
            print("empty linkedList")
            return
        pointer: Node = self.head
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





        


        
        
        

        