"""https://programmers.co.kr/learn/courses/30/lessons/12949
2차원 행렬 arr1과 arr2를 입력 받아, arr1에 arr2를 곱한 결과를 반환하는 함수, solution을 완성해주세요.

제한 조건
행렬 arr1, arr2의 행과 열의 길이는 2 이상 100 이하입니다.
행렬 arr1, arr2의 원소는 -10 이상 20 이하인 자연수입니다.
곱할 수 있는 배열만 주어집니다.
"""


def solution(arr1, arr2):
    answer = []

    for arr1_row in arr1:
        print(f'arr1_row = {arr1_row}')
        answer_row = []
        for arr2_col in zip(*arr2):
            print(f'arr2_col = {arr2_col}')
            answer_index = []
            for i in zip(arr1_row, arr2_col):
                answer_index.append(i[0] * i[1])
            answer_index = sum(answer_index)
            answer_row.append(answer_index)
        answer.append(answer_row)

    return answer

def another_solution(A, B):
    return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]

    