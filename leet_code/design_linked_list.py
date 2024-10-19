class Node:
    def __init__(self,val=None,nextnode=None):
        self.val=val
        self.next=nextnode
class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index<0 or index>=self.size:
            return -1
        i=0
        current=self.head
        while i<=index:
            if i==index:
                return current.val
            current=current.next
            i+=1
    def addAtHead(self, val: int) -> None:
        current=Node(val)
        current.next=self.head
        self.head=current
        self.size+=1

    def addAtTail(self, val: int) -> None:
        if self.head==None:
            self.head=Node(val)
            self.size+=1
            return
        current=self.head
        while current.next:
                current= current.next
        current.next=Node(val)
        self.size+=1

    def addAtIndex(self, index: int, val: int) -> None:
        if index==self.size:
            self.addAtTail(val)
            return
        if index > self.size or index<0:
            return
        if index==0:
            self.addAtHead(val)
            return
        i=0
        current=self.head
        while i<index:
            if i==index-1:
                c=Node(val)
                c.next=current.next
                current.next=c
                self.size+=1
                return
            current=current.next
            i+=1

    def deleteAtIndex(self, index: int) -> None:
        if index>=self.size or index<0:
            return
        if index==0:
            self.head=self.head.next
            self.size-=1
            return
        i=0
        current=self.head
        while i<=index:
            if i==index-1:
                c=current.next.next
                current.next=c
                self.size-=1
                return
            current=current.next
            i+=1
        return