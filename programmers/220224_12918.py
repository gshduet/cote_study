'''https://programmers.co.kr/learn/courses/30/lessons/12918
문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수, solution을 완성하세요. 
예를 들어 s가 "a234"이면 False를 리턴하고 "1234"라면 True를 리턴하면 됩니다.

제한 사항
s는 길이 1 이상, 길이 8 이하인 문자열입니다.
'''

def solution1(s):
    arr = list(s)
    arr.sort(reverse=True)
    if not len(arr) == 4 or len(arr) == 6 :
        answer = False
    else :    
        if arr[0] not in list(map(str, range(0,10))):
            answer = False
        else : answer = True
    return answer

def solution2(s):
    arr = list(s)
    arr.sort(reverse=True)
    if not len(arr) == 4 or len(arr) == 6 :
        answer = False
    else :    
        if type(arr[0]) != type(arr[-1]):
            answer = False
        else : answer = True
    return answer


def solution3(s):
    return s.isdigit() and len(s) in (4, 6)

def solution4(s):
    try:
        int(s)

    except:
        return False

    return len(s) == 4 or len(s) == 6 