# #pattern for descending  5-1 left alignment
# n = int(input("Enter number of rows:"))
# for i in range(n,0,-1):
#     for j in range(i,0,-1):
#         print(j, end=" ")
#     print()

#pattern for asscending  5-1 left alignment
n = int(input("Enter number of rows:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j, end=" ")
    print()
