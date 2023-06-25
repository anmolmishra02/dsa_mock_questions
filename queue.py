
def enqueue(queue,item):
    queue.append(item)
    print("Pushed "+str(item)+" in the queue")

def isempty(queue):
    return len(queue)==0

def dequeue(queue):
    if isempty(queue):
        return "queue empty"
    element=queue.pop(0)
    return element
    
def display(queue):
    print("Elements of queue are")
    print(queue)
        
queue=list()
enqueue(queue,1)
enqueue(queue,2)
enqueue(queue,3)
display(queue)
dequeue(queue)
display(queue)
