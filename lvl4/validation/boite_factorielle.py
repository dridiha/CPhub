#!/usr/bin/env python3
import sys
sys.setrecursionlimit(3000)
def sum(L1, L2):
    if len(L1) >= len(L2):
        return list(map(lambda x,y: x + y, L1[:len(L2)], L2)) + L1[len(L2):]
    else:
        return list(map(lambda x,y: x + y, L1, L2[: len(L1)])) + L2[len(L1):]

def search(nb, arr):

    if nb == 1:
        arr[1] = [1]
        return arr[1]

    if nb not in arr.keys():
        a, b = nb // 2, nb - (nb // 2)
        L1 = list.copy(search(a, arr))
        L2 = list.copy(search(b, arr))
        result = sum(L1, L2)
        for i in range(len(result)):
            
            if (result[i] // (i + 2) > 0):
                if (i + 1 >= len(result)):
                    result.append(result[i] // (i + 2))
                    result[i] %= (i + 2) 
                
                else:
                    result[i], result[i + 1] = result[i] % (i + 2), result[i + 1] + result[i] // (i + 2)
            
        arr[nb] = result
    
    return arr[nb]

def main():
    nb = int(input())
    arr = {}
    search(nb, arr)
    #print(arr)
    print(len(arr[nb]))
    print(*arr[nb])
    

main()





