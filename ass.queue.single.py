class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class queue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.count=0
    
    def isempty(self):
        return self.count==0
    
    def enqueue(self,data):
        print(data,"has moved in the queue")
        n=node(data)
        if self.isempty():
            self.front=n
        else:
            self.rear.next=n
        self.rear=n
        self.count+=1
        
    def dequeue(self):
        print(self.front.data,"has removed from the queue")
        if self.count==1:
            self.front=None
            self.rear=None
        else:
            self.front=self.front.next
        self.count-=1
    
    def get_front(self):
        print(self.front.data,"is in the front")
    
    def get_rear(self):
        print(self.rear.data,"is in the rear")
    
    def size(self):
        print(self.count,"is the size")
mylist=queue()
mylist.isempty()
mylist.enqueue(10)
mylist.enqueue(20)
mylist.dequeue()
mylist.size()
