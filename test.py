# def xorFinder(arr2d,n,m):
#     a = 0
#     for i in range(n):
#         for j in range(m):
#             a = a^arr2d[i][j]
#     return a



# def xorCalculator(arr2d,n,m):
#     xorList = []
#     for i in range(n):
#         for j in range(m):
#             xorList.append(xorFinder(arr2d,i,j))
#     print(xorList)
#     return xorList

# def kthmaxfinder(xorlist,k):
#     xorlist.sort()
#     return xorlist[k]

# testCase = int(input())

# for i in range(testCase):
#     n,m = map(int,input().split(" "))
#     arr2d = [] 
#     for j in range(n):
#         arr2d.append(list(map(int,input().split(" "))))
#     k = int(input())
#     print(kthmaxfinder(xorCalculator(arr2d,n,m),k))


# testCase = int(input())

# for i in range(testCase):
#     buildList = list(map(int,input().split(" ")))
#     print(buildList)

# lst = filter(lambda x:x%5==0,[x**2 for x in range(1,11) if x%2==1])
# print(lst[0])


