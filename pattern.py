#to A+ with repetation of A in triangle pattern 
# n = int (input("Enter no. of rows : "))
# for i in range(n):
#     for j in range(i):
#         print(chr(65+j),end= " ")
#     print()

#to print from A without repeating A
# n = int (input("Enter no. of rows : "))
# num=0
# for i in range(n):
#     for j in range(i):
#         print(chr(65+num),end= " ")
#         num+=1
#     print()   

#to make a pyramid 
n = int(input("Enter a number : "))
for i in range(n):
    print(' '*(n-i+1),end = " ")
    for j in range (2*i+1):
        print(chr(65+j),end = " ")
    print()