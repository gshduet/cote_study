'''https://programmers.co.kr/learn/courses/30/lessons/12954
함수 solution은 정수 x와 자연수 n을 입력 받아, x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴해야 합니다. 
다음 제한 조건을 보고, 조건을 만족하는 함수, solution을 완성해주세요.

제한조건
x는 -10000000 이상, 10000000 이하인 정수입니다.
n은 1000 이하인 자연수입니다.

예시
x = 2, n = 5. answer = [2,4,6,8,10]
x = 4, n = 3. answer = [4, 8, 12]
x = -4, n = 2. answer = [-4, -8]
'''

def solution(x, n):
    answer = []
    for i in range(1, n+1):
        answer.append(i * x)
    return answer


def solution(x, n):
    answer = [i * x for i in range(1, n+1)]
    return answer


print(solution(2, 5))
