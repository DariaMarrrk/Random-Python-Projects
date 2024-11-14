def NAND(x, y): # x and y are arrays
    out = []
    for i in range(16):   
        out.append(not (x[i] and y[i]))
    return(out)
    
a = [0 for i in range(8)]
for i in range (8):
    a.append(1)
b = [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1]
c = [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1]
d = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]

ans = [1 for i in range(15)]
ans.append(0)

inputs = [a, b, c, d]

Found = False
adding_to = inputs[len(inputs)-1] #starting with the last element and adding it to the previous ones
while not Found:
    i = 0
    print(adding_to, inputs[i])
    while i < inputs.index(adding_to):
        output = NAND(adding_to, inputs[i])
        if output == ans:
            Found = True
            print("found")
            break
        else:
            if output not in inputs:
                inputs.append(output)
        i += 1
    adding_to = inputs[inputs.index(adding_to)+1]


#how to trace back???
