#! /usr/bin/env python3
import sys
sys.setrecursionlimit(3000)
max_length = 0
# method using Tree

class Node:
    def __init__(self, parent, data, level):
        self.parent = parent
        self.data = data
        self.level = level
        self.children = []



def createTree(codes, root):
    global max_length
    children_nodes = list(filter(lambda x: x[1] == root.data, codes))
    if root.level > max_length:
        max_length = root.level
    for child in children_nodes:
        root.children.append(Node(root, child[0], root.level + 1))
    for child in root.children:
        createTree(codes, child)


# other one

def search_naive(codes):
    max_length = 0
    for i in range(len(codes)):
        code = i + 1
        path = [code]
        while (codes[code - 1] != 0):
            path = [codes[code - 1]] + path
            code = codes[code -1]
        if max_length < len(path):
            max_length = len(path)
    return max_length

# dynamic programming
def search(codes, arr, node):
    if node not in arr.keys():
        arr[node] = search(codes, arr, codes[node - 1]) + 1

    return arr[node]

def main():
    N = int(input())
    codes = list(map(lambda x: int(x), input().split(" ")))

    arr = {0:0}
    
    for code in codes:
        search(codes, arr, code)
    print(max(arr.values()) + 1)

main()
