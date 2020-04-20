# -*- coding: utf-8 -*-

def findMinAndMax(L):
    if not L:
        return None, None
    else:
        max = L[0]
        min = L[0]
        for i in L:
            if i < min:
                min = i
            if i > max:
                max = i
    return max, min


if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
