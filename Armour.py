def IdxVal(Line, D):
    TotalValue = 0
    StartingIndex = 0
    for v in range(0, len(Line)): # checks the Line to choose the best starting index v
        Sum = 0 
        i = v
        if (v + D - 1) < len(Line):
            while i <= (v + D - 1):
                Sum = Sum + Line[i]
                i = i + 1
        else:
            for m in range(i, len(Line)):
                 Sum = Sum + Line[m]
        if Sum > TotalValue:
            TotalValue = Sum
            StartingIndex = v + 1# index begins with 0 while count begins with 1
    return(StartingIndex, TotalValue)

N = int(input('Enter the number of wares in the line '))
Line = []
Line = input('Enter the value of each ware in the line ').split()
for v in range(0, len(Line)):
    Line[v] = int(Line[v])

T = int(input('Enter T ')) # possibilities for attention span
Spans = []
for i in range(0, T):
    D = int(input('Enter the possible number of the items examined '))
    Spans.append(D)

for i in range(0, len(Spans)):
    a,b = IdxVal(Line, Spans[i])
    print(a,b)
