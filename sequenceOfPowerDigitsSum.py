#To make things easier, you always be given k values such that: k > h + 2 * patt_len



def sum_pow_dig_seq(start, n, k):
    cyc_patt_arr = []
    listaNumeros = []
    def sumPowDigSeq (start, n, k):
        nonlocal cyc_patt_arr
        nonlocal listaNumeros
        r1 = 0
        listaNumeros.append(start)

        if k > 0:
            for digit in list(str(start)):
                r1 += int(digit) ** n
            if r1 in listaNumeros and r1 not in cyc_patt_arr:
                cyc_patt_arr.append(r1)
            return sumPowDigSeq(r1,n,k-1)

        patt_len = len(cyc_patt_arr)
        h = len(listaNumeros[:listaNumeros.index(cyc_patt_arr[0])])
        return [h, cyc_patt_arr, patt_len, start]
    return sumPowDigSeq (start, n, k)








print(sum_pow_dig_seq(420,4,30))

#Tests
#test.assert_equals(sum_pow_dig_seq(420, 3, 5), [3, [153], 1, 153])
#sum_pow_dig_seq(420, 4, 30), [12, [13139, 6725, 4338, 4514, 1138, 4179, 9219], 7, 1138]
