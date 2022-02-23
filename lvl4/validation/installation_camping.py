#! /usr/bin/env python3

def methode_naive(matrice):
    n = len(matrice)
    m = len(matrice[0])
    taille = min(m, n)
    
    while taille > 0:
        for i in range(n):
            if matrice[i].count(0) >= taille and (n - i + 1 >= taille):
                for j in range(m):
                    if matrice[i][j] == 0 and matrice[i][j:j + taille] == [0 for _ in range(taille)] and (m - j +1) >= taille:
                        k = i + 1
                        while (k < i + taille and matrice[k][j:j + taille] == [0 for _ in range(taille)]):
                            k += 1
                        if k >= i + taille:
                            return taille

                
        taille -= 1
    return taille

def extraction_colonne(matrice, k, borneinf, bornesup):
    L = []
    for i in range(len(matrice)):
        for j in range(len(matrice[0])):
            if (i <= bornesup and i >= borneinf and j == k):
                L.append(matrice[i][j])
    return L



def methode_naive_bis(matrice):
    n = len(matrice)
    m = len(matrice[0])
    L = []
    for i in range(n):
        for j in range(m):
            if matrice[i][j] == 0:
                L.append((i, j))
    taille = 1
    while (len(L) != 1 and taille <= min(n, m)):
        taille += 1
        sl = set()
        for element in L:
            i, j = element
            tmp = [0 for _ in range(taille)]
            if (i + taille - 1 < n and j + taille <= m):
                if (matrice[i + taille - 1][j:j + taille] == tmp
                    and extraction_colonne(matrice, j + taille - 1, i, i + taille -1) == tmp):
                    
                    sl.add((i,j))

        L = list(sl)
    return taille

def methode_optimisee(matrice):
    n = len(matrice)
    m = len(matrice[0])
    test = False
    max_length = 0

    for i in range(n):
        for j in range(m):
            if (j == 0 or i == 0):
                if (matrice[i][j] == 0):
                    matrice[i][j] = 1
                    test = True
                    
                else:
                    matrice[i][j] = 0 
            if j > 0 and i > 0 and matrice[i][j] == 0:
                matrice[i][j] = min(matrice[i][j-1], matrice[i-1][j], matrice[i-1][j-1]) + 1
                if matrice[i][j] > max_length:
                    max_length = matrice[i][j]
            elif j > 0 and i > 0 and matrice[i][j] != 0:
                matrice[i][j] = 0
    
    if (max_length == 0 and test):
        return 1
    return max_length


def main():

    l = input()
    l = l.split(" ")
    n = int(l[0])
    m = int(l[1])
    matrice = []
    for i in range(n):
        l = input()
        l = l.split(" ")
        matrice.append(list(map(lambda x: int(x), l)))
    
    
    print(methode_optimisee(matrice))
    

main()
