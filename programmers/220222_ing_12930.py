'''https://programmers.co.kr/learn/courses/30/lessons/12930
문자열 s는 한 개 이상의 단어로 구성되어 있습니다. 각 단어는 하나 이상의 공백문자로 구분되어 있습니다. 
각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, solution을 완성하세요.

제한 사항
문자열 전체의 짝/홀수 인덱스가 아니라, 단어(공백을 기준)별로 짝/홀수 인덱스를 판단해야합니다.
첫 번째 글자는 0번째 인덱스로 보아 짝수번째 알파벳으로 처리해야 합니다.

예시
input "try hello world"     output "TrY HeLlO WoRlD"

"try hello world"는 세 단어 "try", "hello", "world"로 구성되어 있습니다. 
각 단어의 짝수번째 문자를 대문자로, 홀수번째 문자를 소문자로 바꾸면 
"TrY", "HeLlO", "WoRlD"입니다. 

따라서 "TrY HeLlO WoRlD" 를 리턴합니다.
'''


def solution(s):
    arr = list(s.split(' '))
    answer = []

    for word in arr:
        spelling = list(str(word))

        for i in range(len(spelling)):
            if i % 2 == 0:
                answer.append(spelling[i].upper())

            else:
                answer.append(spelling[i].lower())

        answer.append(' ')

    answer = ''.join(answer)
    answer = answer.strip()

    return answer

# arr = list(input().split(' '))
# answer = []
# print(f'arr = {arr}')

# for word in arr:
#     spelling = list(str(word))

#     for i in range(len(spelling)):
#         if i % 2 == 0:
#             answer.append(spelling[i].upper())

#         else :
#             answer.append(spelling[i])

#     answer.append(' ')


print(solution(''))
