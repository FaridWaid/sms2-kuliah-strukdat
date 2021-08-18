class Node:
    #constructor
    def __init__(self,item):
        self.data=item
        self.next=None
    #get_set
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self,item):
        self.data=item
    def setNext(self,pt):
        self.next=pt



n1=Node(21)
print(n1.getData())
print(n1.getNext())

n2=Node(10)
print(n2.getData())
print(n2.getNext())
n2.setNext(n1)
print(n2.getNext())
