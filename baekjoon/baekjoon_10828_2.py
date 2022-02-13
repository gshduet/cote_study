import sys
input = sys.stdin.readline
 
number_of_order = int(input())
stack           = []
 
def push(value):
    stack.append(value)
 
def pop():
    if not stack:
        return -1
    return stack.pop()
 
def size():
    return len(stack)
 
def empty():
    if not stack:
        return 1
    return 0
 
def top():
    if not stack:
        return -1
    return stack[-1]
 
for _ in range(number_of_order):
    command = input().split()
    if 'push' in command:
        push(command[1])
    elif 'top' in command:
        print(top())
    elif 'size' in command:
        print(size())
    elif 'empty' in command:
        print(empty())
    else:
        print(pop())
