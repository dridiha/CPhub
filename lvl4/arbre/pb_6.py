#! /usr/bin/env python3
import sys
sys.setrecursionlimit(50000)

class Node:
    def __init__(self, parent, data):
        self.parent = parent
        self.data = data
        self.children = []

def createTree(root, edges):
    i = 0
    while i < len(edges):
        if edges[i][0] == root.data:
            root.children.append(Node(root, edges[i][1]))
            edges.pop(i)
        elif edges[i][1] == root.data:
            root.children.append(Node(root, edges[i][0]))
            edges.pop(i)
        else:
            i += 1
    for child in root.children:
        createTree(child, edges)

def length_subTree(root, arr):
    if len(root.children) == 0:
        arr[root.data] = 0
        
    else:
        if root.data not in arr.keys():
            arr[root.data] = 0
            for child in root.children:
                arr[root.data] += length_subTree(child, arr) + 1

    return arr[root.data]

def search(root, arr, length, N):
    if len(root.children) > 0:
        for child in root.children:
            length[(root.data, child.data)] = [N - arr[child.data] - 2, arr[child.data]]
        for child in root.children:
            search(child, arr, length, N)

    

def main():
    N = int(input())
    edges = [tuple(map(lambda x: int(x), input().split(" "))) for _ in range(N - 1)]
    root = Node(None, 0)
    createTree(root, list.copy(edges))
    arr = {}
    length_subTree(root, arr)
    #print(arr)
    length = {}
    search(root, arr, length, N)
    Tab = {}
    print(length)
    for key in length.keys():
        Tab[key] = abs(length[key][0] - length[key][1])
    Tab = sorted(Tab, key=lambda x: Tab[x])
    print(Tab)
    print(N - 1 - length[Tab[0]][0])
    
    

main()

