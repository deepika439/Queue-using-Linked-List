class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
    
    def enqueue(self):
        size=int(input("Enter size"))
        for i in range(size):
            data=int(input())
            newnode=Node(data)
            if self.front is None and self.rear is None:
                self.front=self.rear=newnode
            else:
                self.rear.next=newnode
                self.rear=newnode

    def dequeue(self):
        if self.front is None and self.rear is None:
            print("Queue is empty")
        else:
            print(f"{self.front.data}is deleted")
            self.front = self.front.next

    def peek(self):
        if self.front is None and self.rear is None:
            print("Queue is Empty")
        else:
            print(f"The front element is {self.front.data}")

    def display(self):
        if self.front is None and self.rear is None:
            print("Queue is Empty")
        else:
            temp=self.front
            while temp:
                print(f"Elements in Queue{temp.data}")
                temp=temp.next

obj=Queue()
while True:
    print("\n 1.Enqueue")
    print("2.Dequeue")
    print("3.Display")
    print("4.Peek")
    print("5.Exit")
    choice = int(input("ENTER YOUR CHOICE:"))
    if choice==1:
        obj.enqueue()
    elif choice==2:
        obj.dequeue()
    elif choice==3:
        obj.display()
    elif choice==4:
        obj.peek()
    elif choice==5:
        break
    else:
        print("\n Invalid choice!!")
