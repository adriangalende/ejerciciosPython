

def solution(number):
    decimalNumberPart = (round(number%1,1))
    if decimalNumberPart <= 0.2:
        return int(number)
    elif decimalNumberPart >= 0.3 and decimalNumberPart <= 0.7:
        return float(int(number) + 0.5)
    else:
        return round(number)



#Test
#Test.assert_equals(solution(4.2), 4)
#Test.assert_equals(solution(4.25), 4.5)
#Test.assert_equals(solution(4.4), 4.5)
#Test.assert_equals(solution(4.6), 4.5)
#Test.assert_equals(solution(4.75), 5)
#Test.assert_equals(solution(4.8), 5)
#def solution(n):
#    fract = n % 1
#    integer = n - fract
#    if fract >= 0.75: fract = 1
#    elif fract < 0.25: fract = 0
#    else: fract = 0.5
#    return integer + fract
