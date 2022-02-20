import sys
input = sys.stdin.readline

number_of_order = int(input())
stack = []

for _ in range(number_of_order):
    command = int(input())
    if command == 0:
        stack.pop()

    else:
        stack.append(command)

print(sum(stack))
