'''https://programmers.co.kr/learn/courses/30/lessons/12948
프로그래머스 모바일은 개인정보 보호를 위해 고지서를 보낼 때 고객들의 전화번호의 일부를 가립니다.
전화번호가 문자열 phone_number로 주어졌을 때, 전화번호의 뒷 4자리를 제외한 나머지 숫자를 전부 *으로 가린 문자열을 리턴하는 함수, solution을 완성해주세요.

제한 조건
s는 길이 4 이상, 20이하인 문자열입니다.

예시
input "01033334444" output "*******4444"
input "027778888"   output "*****8888"
'''

def solution(phone_number):
    answer = "*" * len(phone_number[:-4]) + phone_number[-4:]
    return answer

print(solution("027778888"))

'''
정규식을 써볼까도 싶었지만 닭 잡는데 소 잡는 느낌이라 패스
'''