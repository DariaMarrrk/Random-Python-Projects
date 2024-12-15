ans = int(input("expected output: "))
inputs = []
paths = {} #key = the result, value = array of two inputs that produced this result
global original_inputs
original_inputs = []

i = int(input("enter the inputs: "))
while i != 0:
    if i not in inputs:
        inputs.append(i)
        original_inputs.append(i)
    i = int(input())

def operation(x, y):
    return(x+y)

Found = False
adding_to = inputs[len(inputs)-1] #the number currently adding to
while not Found:
    i = 0
    while i < inputs.index(adding_to):
        output = operation(adding_to, inputs[i])
        paths.update({output: [adding_to, inputs[i]]})
        if output == ans:
            Found = True
            break
        else:
            if output not in inputs:
                inputs.append(output)
        i += 1
    adding_to = inputs[inputs.index(adding_to)+1]

path_to_ans = {}

def trace(paths, ans, path_to_ans):
    looking_into = paths.get(ans)
    path_to_ans.update({ans: looking_into})
    if looking_into[0] in original_inputs and looking_into[1] in original_inputs:
        return(str(path_to_ans))
    else:
        if looking_into[0] not in original_inputs:
            trace(paths, looking_into[0], path_to_ans)
        if looking_into[1] not in original_inputs:
            trace(paths, looking_into[1], path_to_ans)
            
trace(paths, ans, path_to_ans)      
print(path_to_ans)
