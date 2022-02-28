#! /usr/bin/env python3
import sys
sys.setrecursionlimit(50000)

def createTreeFromEdges(edges):
    tree = {}
    for v1, v2 in edges:
        tree.setdefault(v1, []).append(v2)
        tree.setdefault(v2, []).append(v1)
        
        
    return tree

def length_subtree(tree, root, visited, arr):
    if root not in visited:
        visited.add(root)
        if root not in arr.keys():
            arr[root] = 0
            for child in tree[root]:
                if child not in visited:
                    arr[root] += length_subtree(tree, child, visited, arr)
            arr[root] += 1
        return arr[root]



def search(edges, length, arr, N):
    for edge in edges:
        if arr[edge[0]] > arr[edge[1]]:
            length.append(min(arr[edge[1]], N - arr[edge[1]]))
        else:
            length.append(min(arr[edge[0]], N - arr[edge[0]]))

    

def main():
    N = int(input())
    edges = [tuple(map(lambda x: int(x), input().split(" "))) for _ in range(N - 1)]
    tree = createTreeFromEdges(edges)
    arr = {}
    visited = set()
    length = []
    length_subtree(tree, edges[0][0], visited, arr)
    search(edges, length, arr, N)
    print(max(length))
    
    
    
main()

