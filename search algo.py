ans = int(input("expected output: "))
inputs = []

i = int(input("enter the inputs: "))
while i != 0:
    if i not in inputs:
        inputs.append(i)
    i = int(input())

def operation(x, y):
    return(x-y)

Found = False
adding_to = inputs[len(inputs)-1] 
while not Found:
    i = 0
    print(inputs)
    while i < inputs.index(adding_to):
        print(adding_to, inputs[i])
        output = operation(adding_to, inputs[i])
        if output == ans:
            Found = True
            break
        else:
            if output not in inputs:
                inputs.append(output)
        i += 1
    adding_to = inputs[inputs.index(adding_to)+1]


"""Exceptions with basic arithmetic operations:
addition: if x+y > ans; if x and y are both even and ans is odd
multiplication: if ans is a prime number"""
