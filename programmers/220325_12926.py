"""https://programmers.co.kr/learn/courses/30/lessons/12926
어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식을 시저 암호라고 합니다. 
예를 들어 "AB"는 1만큼 밀면 "BC"가 되고, 3만큼 밀면 "DE"가 됩니다. "z"는 1만큼 밀면 "a"가 됩니다. 
문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수, solution을 완성해 보세요.

제한 조건
공백은 아무리 밀어도 공백입니다.
s는 알파벳 소문자, 대문자, 공백으로만 이루어져 있습니다.
s의 길이는 8000이하입니다.
n은 1 이상, 25이하인 자연수입니다.
"""
from utils import time_check


@time_check
def solution(s, n):
    answer = ''

    for i in s:
        if ord(i) in range(65,91 - n):
            answer += chr(ord(i) + n)
        elif ord(i) in range(91 - n, 91):
            answer += chr(ord(i) + n - 26)
        elif ord(i) in range(91,123 - n):
            answer += chr(ord(i) + n)
        elif ord(i) in range(123 - n,123):
            answer += chr(ord(i) + n - 26)
        else: answer += i

    return answer

s = 'dgsioagjoi pwr uewoiu oidpuoijoigje w oij oij foisdj foif ofsdlkgjfiowerugoiprejgkdfjlkj dslkfjweoi toipweutio weuori jewoifjoiwjoptweiotdksjfoipwuetopiqwtoidksjflk  f oij oiwej ptoi jewqoiewoi ksdjli' * 40
print(solution(s, 5))
print(len(s))

# for i in s:
    # print(f'{i}를 ascii 변환하면 = {ord(i)}')