"""https://programmers.co.kr/learn/courses/30/lessons/70129?language=python3
0과 1로 이루어진 어떤 문자열 x에 대한 이진 변환을 다음과 같이 정의합니다.

x의 모든 0을 제거합니다.
x의 길이를 c라고 하면, x를 "c를 2진법으로 표현한 문자열"로 바꿉니다.
예를 들어, x = "0111010"이라면, x에 이진 변환을 가하면 x = "0111010" -> "1111" -> "100" 이 됩니다.

0과 1로 이루어진 문자열 s가 매개변수로 주어집니다. 
s가 "1"이 될 때까지 계속해서 s에 이진 변환을 가했을 때, 
이진 변환의 횟수와 변환 과정에서 제거된 모든 0의 개수를 각각 배열에 담아 return 하도록 solution 함수를 완성해주세요.

제한사항
s의 길이는 1 이상 150,000 이하입니다.
s에는 '1'이 최소 하나 이상 포함되어 있습니다.
"""


def first_solution(s):
    func, zero = 0, 0

    while s != "1":
        new_s = s.count("1")
        zero += len(s) - new_s
        s = bin(new_s)[2:]
        func += 1

    return [func, zero]

# 첫 번째 재귀함수
def s_binary(s_change, func_count, zero_count):
    if s_change == "1":
        return [func_count, zero_count]

    ss = ""

    for i in s_change:
        if i == "0":
            zero_count += 1
        else:
            ss += i

    ss = bin(len(ss))[2:]
    func_count += 1

    return s_binary(ss, func_count, zero_count)

# 두 번째 재귀함수
def s_recursion(s_change, func_count, zero_count):
    if s_change == "1":
        return [func_count, zero_count]

    func_count += 1
    zero_count += s_change.count("0")
    s_change = bin(len(s_change) - s_change.count("0"))[2:]

    return s_recursion(s_change, func_count, zero_count)


def solution(s):
    # answer = s_binary(s, 0, 0)
    answer = s_recursion(s, 0, 0)
    return answer


s = "110010101001"

print(solution(s))
# print(other_solution(s))
