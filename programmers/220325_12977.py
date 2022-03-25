"""https://programmers.co.kr/learn/courses/30/lessons/12977
주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다.
숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.

제한사항
nums에 들어있는 숫자의 개수는 3개 이상 50개 이하입니다.
nums의 각 원소는 1 이상 1,000 이하의 자연수이며, 중복된 숫자가 들어있지 않습니다.
"""
from utils import time_check


@time_check
def check_divisor_01(nums):
    divisors = []
    for i in range(1, nums+1):
        if nums % i == 0:
            divisors.append(i)
    return divisors


@time_check
def check_divisor_02(nums):
    divisors = []
    for i in range(1, int((nums**1/2)+1)):
        if nums % i == 0:
            divisors.append(i)
            divisors.append(int(nums/i))
    return divisors


nums = 10000

print(check_divisor_01(nums))
print(check_divisor_02(nums))
