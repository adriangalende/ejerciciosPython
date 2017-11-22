def is_zero_balanced(arr):
    sum = 0
    existNegative = False
    for i in arr:
        sum += i
        for j in arr:
            if j == ( -i ):
                existNegative = True
                break


    if sum == 0 and existNegative:
        return True
    else:
        return False
