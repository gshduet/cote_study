import sys
input = sys.stdin.readline

number_of_order = int(input())
queue           = []

for _ in range(number_of_order):
    command = input().split()
    
    if command[0] == 'push':
        queue.append(int(command[1]))

    elif command[0] == 'pop':
        if len(queue) != 0: 
            print(queue.pop(0))

        else: print(-1)

    elif command[0] == 'size':
        print(len(queue))

    elif command[0] == 'empty':
        if len(queue) != 0: 
            print(0)

        else: print(1)
        
    elif command[0] == 'front':
        if len(queue) != 0: 
            print(queue[0])

        else: print(-1)

    elif command[0] == 'back':
        if len(queue) != 0: 
            print(queue[-1])
            
        else: print(-1)


'''
def push(value):
    queue.append(value)
 
def pop():
    if not queue:
        return -1
    return queue.pop(0)
 
def size():
    return len(queue)
 
def empty():
    if not queue:
        return 1
    return 0
 
def front():
    if not queue:
        return -1
    return queue[0]

def back():
    if not queue:
        return -1
    return queue[-1]
'''