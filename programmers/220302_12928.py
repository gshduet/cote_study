'''https://programmers.co.kr/learn/courses/30/lessons/12928
정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.

제한 사항
n은 0 이상 3000이하인 정수입니다.
'''
answer = []
for i in range(1,1000):
    if 999 % i == 0 :
        answer.append(i)

print(answer)