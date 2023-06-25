
def push(stack,item):
    stack.append(item)
    print("Pushed "+str(item)+" in the stack")

def isempty(stack):
    return len(stack)==0

def pop(stack):
    if isempty(stack):
        return "stack empty"
    return stack.pop()
    
def showstack(stack):
    print("Elements of stack are")
    for i in stack:
        print(i)
        
stack=list()
push(stack,1)
push(stack,2)
push(stack,3)
showstack(stack)
pop(stack)
showstack(stack)
