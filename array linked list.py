def PrintLL():
    index = StartPointer
    while index != -1:
        print(DataArray[index])
        index = PointArray[index]

def AddItem(item):
    global EndPointer, StartPointer
    
    DataArray.append(item)
    
    if EndPointer == 0: # the list is empty
        Placed = True
        PointerArray.append(-1) #since the only element in DataArray is the first and the last element
        EndPointer += 1
    else:
         Placed = False
         index = StartPointer
    
    while Placed == False and index != -1:
        if item < DataArray[index]:
            if index == StartPointer: #then we're adding to the beginning since the new data is smaller than the original smallest (on StartPointer)
                PointerArray.append(StartPointer) #old start pointer now points at the old smallest data; its index in P.A. corresponds to new smallest element's index in D.A.
                StartPointer = DataArray.index(item) #the new smallest data's index in D.A. now becomes StartPointer
                Placed = True
            else: #we're adding to the middle
                PointerArray.append(previous_index)
                PointerArray[previous_index] = EndPointer
                EndPointer += 1
                Placed = True
        else:
            previous_index = index
            "index =  ??????

    if not Placed:
        PointerArray[PointerArray.index(-1)] = DataArray.index(item) #adding the item to the end
        PointerArray.append(-1)

#def DeleteItem:
    
        
global DataArray
DataArray = [] #stores data in order of input/entry; each item's index corresponds to the index in PointerArray containing next pointer
global PointerArray
PointerArray = [-1] #stores pointers that point at the index in DataArray on which the next item in LL is located
global StartPointer
StartPointer = 0 #represents an index in DataArray on which the smallest (first) element of the LL is stored
global EndPointer
EndPointer = 0 #points at the index in DataArray that the next element to be filled in would have 

for i in range(1, 9): # 8 times
    data = int(input("Enter data "))
    if data == '-1':
        break
    else:
        AddItem(data)

PrintLL()
