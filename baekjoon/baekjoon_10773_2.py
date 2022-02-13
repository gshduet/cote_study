import sys
input = sys.stdin.readline

number_of_order = int(input())
stack           = []

def push(value):
    stack.append(value)

def pop():
    stack.pop()

for _ in range(number_of_order):
    command = int(input())
    
    if command == 0:
        pop()
    
    else: push(command)

print(sum(stack))