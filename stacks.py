class MyStack:
    def __init__(self):
        self.StackArray = [0 for i in range(10)]
        self.__Pointer = 0
        
    def GetPointer(self):
        return self.__Pointer

    def SetPointer(self, value):
        self.__Pointer = value

    def Pop(self, value):
        if self.GetPointer() == 9:
            print("Stack is full")
        else:
            self.StackArray[self.GetPointer()] = value
            self.SetPointer(self.__Pointer + 1)

        
    def Print(self):
        for i in self.StackArray:
            print(i)

    def Push(self):
        if self.GetPointer() == 0:
            print("Stack is empty")
        else:
            self.SetPointer(self.__Pointer - 1)
            value = self.StackArray[self.GetPointer()]
            self.StackArray[self.GetPointer()] = 0
        return(value)
            
        
Stack1 = MyStack()
Stack2 = MyStack()

for i in range(1, 10):
    Stack1.Pop(i)
Stack1.Pop(300)
Stack1.Print()
for i in range(1, 3):
    print (Stack1.Push())
Stack1.Print()
