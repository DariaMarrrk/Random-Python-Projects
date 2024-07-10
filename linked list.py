class Node():
    def __init__(self, data):
        self.Data = data
        self.Next = -1 #points at the next element

class LinkedList():
    def __init__(self):
        self.MyLL = []
        self.StartPointer = 0 # points at the first element of the list - the smallest number; doesn't have to be indexed 0
        self.EndPointer = 0 #points at the first <Next> that can be filled in; points where <Next> = -1 

    def AddItem(self, data):
           MyNode = Node(data) #add the node with the - 1 index
           index = self.StartPointer
           self.MyLL.append(MyNode)

           if self.EndPointer == 0: #because the first element is empty so the whole array is empty
               Placed = True
           else:
               Placed = False
               
           previous_index = index
        
           while index != -1 and Placed == False:
                if data < self.MyLL[index].Data:
                   if index == self.StartPointer: #then we are adding to the beginning
                       self.MyLL[self.EndPointer].Next = self.StartPointer
                       self.StartPointer = self.EndPointer
                       Placed = True
                   else:
                       self.MyLL[self.EndPointer].Next = self.MyLL[previous_index].Next #set the Next in the node to the previous index
                       self.MyLL[previous_index].Next = self.EndPointer
                       Placed = True
                else:
                   previous_index = index 
                   index = self.MyLL[index].Next
           if not Placed:
               self.MyLL[previous_index].Next = self.EndPointer
               Placed = True
           self.EndPointer += 1
           
    def DeleteItem(self, item):
        Found = False
        index = self.StartPointer
        while index != -1 and Found == False:
            if self.MyLL[index].Data == item:
                Found = True
                if index != self.StartPointer:
                    self.MyLL[previous_index].Next = self.MyLL[index].Next
                else:
                    self.StartPointer = self.MyLL[index].Next
            else:
                previous_index = index
                index = self.MyLL[index].Next
        if not Found:
            print("Item not found")
                
        
    def Print(self):
        for i in range(0, len(self.MyLL)):
            node = (self.MyLL[i].Data, self.MyLL[i].Next)
            print((node))

    def PrintInOrder(self):
        i = self.StartPointer
        while i != -1:
            node = (self.MyLL[i].Data, self.MyLL[i].Next)
            print(node)
            i = self.MyLL[i].Next

MyLinkedList = LinkedList()

for i in range(1, 9): # 8 times
    data = int(input("Enter data "))
    if data == -1:
        break
    else:
        MyLinkedList.AddItem(data) # data is an integer, placed in LL in order

MyLinkedList.PrintInOrder()

MyLinkedList.DeleteItem(int(input("Enter the item to be deleted ")))
MyLinkedList.PrintInOrder()

