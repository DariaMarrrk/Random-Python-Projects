class MyQueue():
    def __init__(self):
        self.QueueArray = [None for i in range(10)] #datatype: integer
        self.__EndPointer = 0 #points at the next one to be filled in (the end of the q), increases after adding new item
        self.__StartPointer = 0 #points at the first one to be taken out (the start of the q), increases after removing item

    def GetStartPointer(self):
        return self.__StartPointer
    def GetEndPointer(self):
        return self.__EndPointer
    def SetStartPointer(self, value):
        self.__StartPointer = value
    def SetEndPointer(self, value):
        self.__EndPointer = value

    def Enqueue(self, item):
        if self.GetEndPointer() == self.GetStartPointer() and self.QueueArray[self.GetStartPointer()] is not None: #or if QueueArray[StartPointer] is None
            print("Queue is full")
        else:
            self.QueueArray[self.GetEndPointer()] = item
            if self.GetEndPointer() == 9:
                self.SetEndPointer(0)
            else:
                self.SetEndPointer(self.GetEndPointer() + 1)

    def Dequeue(self):
        if self.QueueArray[self.GetStartPointer()] == None:
            print("Queue is empty")
        else:
            item = self.QueueArray[self.GetStartPointer()]
            self.QueueArray[self.GetStartPointer()] = None
            if self.GetStartPointer() == 9:
                self.SetStartPointer(0)
            else:
                self.SetStartPointer(self.GetStartPointer() + 1)
            return item
    
    def Print(self):
        for i in self.QueueArray:
            print(i)

Queue = MyQueue()

for i in range(0, 11):
    Queue.Enqueue(i)

for i in range(0, 3):
    print(Queue.Dequeue())

for i in range(17, 21):
    Queue.Enqueue(i)
Queue.Print()
