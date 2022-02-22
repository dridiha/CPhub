#! /usr/bin/env python3

# method using Trees
# it does not resolve the problem in france ioi

# class Node:
#     def __init__(self, parent, data):
#         self.parent = parent
#         self.data = data
#         self.children = []

# def createTree(codes, root):
#     children_nodes = list(filter(lambda x: x[1] == root.data, codes))
#     for child in children_nodes:
#         root.children.append(Node(root, child[0]))
#     for child in root.children:
#         createTree(codes, child)
    

# def traverse(root, search_codes, tmp, paths, path):
#     # paths = [[] for _ in range(Nbcodes)]
#     if len(root.children) > 0:
#         for child in root.children:
            
#             path.append(child.data)
#             if child.data in tmp:
#                 paths[search_codes.index(child.data)] += path
#                 tmp.pop(tmp.index(child.data))   
#             else:
#                 traverse(child, search_codes, tmp, paths, path)
            
#             if len(path) > 0:
#                 path.pop()
                
            
# def main():
#     # nombre des recipients 
#     N = int(input())
#     codes = list(map(lambda x: int(x), input().split(" ")))
#     Nbcodes = int(input())
#     search_codes = list(map(lambda x: int(x), input().split(" ")))
#     codes = [(i, x) for i,x in enumerate(codes, 1)]
#     root = Node(None, 0)
#     createTree(codes, root)
#     paths = [[] for _ in range(Nbcodes)]
#     traverse(root, search_codes, list.copy(search_codes), paths, [])
#     for element in paths:
#         print(*element)

def search(codes, code):
    path = [code]
    while (codes[code - 1] != 0):
        path = [codes[code - 1]] + path
        code = codes[code -1]
    print(*path)


def main():
    N = int(input())
    codes = list(map(lambda x: int(x), input().split(" ")))
    Nbcodes = int(input())
    search_codes = list(map(lambda x: int(x), input().split(" ")))
    for code in search_codes:
        search(codes, code)
    

    
main()


    

