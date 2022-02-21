#! /usr/bin/env python3
def reverse_string(m):
    rev = ""
    i = 0
    while i < len(m):
        if (m[i] == 'd'):
            rev = m[i+1: i+3] + rev
            rev = m[i] + rev
            i += 3
        else:
            rev = m[i] + rev
            i += 1
    return rev
        
def print_string(m):
    i = 0
    while i < len(m):
        if (m[i] == 'd'):
            print(m[i+1: i+3])
            i += 3
        else:
            print(m[i])
            i += 1

def search(nb):
    if nb == 1:
        return '1'
    else:
        m1 = '1'
        m2 = '21'
        
        for i in range(3, nb + 1):
            if i >= 10:
                m2, m1 = m1 + 'd' + str(i) + reverse_string(m1) + m2, m2
            else:
                m2, m1 = m1 + str(i) + reverse_string(m1) + m2, m2 
            
            

        return m2

# def search(nb):
#     if nb == 1:
#         return [1]
#     else:
#         T = []
#         T.append([1])
#         T.append([2, 1])
#         for i in range(2, nb):
#             F = list.copy(T[0])
#             F.reverse()
#             T[1], T[0] = T[0] + [i + 1] + F + T[1], T[1]
            

#         return T[1]

def main():
    nb = int(input())
    result = search(nb)
    print_string(result)

    # for x in result:
    #     print(x)
   

main()