# 当我们的返回值为bool时，直接可以把if中的 condition 作为 返回值 来处理
def can_win_nim(n):#用时：44ms
    if n % 4 == 0:
        return False
    else:
        return True

def can_win_nim(n): # 用时：40 ms
    return n%4 !=0
