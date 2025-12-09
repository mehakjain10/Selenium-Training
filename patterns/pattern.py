'''
PATTERN 1

*
**
***
'''

# n = 3
# for i in range(n):
#     for j in range(n):
#         if (j<=i):
#             print("*", end='')
#         else:
#             print(" ", end='')
#     print()
#
# for i in range(n):
#     for j in range(i+1):
#         print("*", end='')
#     print()

'''
PATTERN 2

  *
 **
***

'''

# n = 3
# for i in range(n):
#     for j in range(n):
#         if i+j >=n-1:
#             print("*", end='')
#         else:
#             print(" ", end='')
#     print()

'''
PATTERN 3

***
**
*

'''




'''
PATTERN 4

hollow rectangle

'''

# n = 5
# for i in range(n):
#     for j in range(n):
#         if i == 0 or j == 0 or i == n - 1 or j == n - 1:
#             print("*", end='')
#         else:
#             print(" ", end='')
#     print()

'''
PATTERN 5

hollow triangle

'''

# n = 5
# for i in range(n):
#     for j in range(n):
#         if j == 0 or i == j or i == n-1:
#             print("*", end='')
#         else:
#             print(" ", end='')
#     print()

'''
PATTERN 6

inverted hollow

'''

# n = 9
# for i in range(n):
#     for j in range(n):
#         if i == n-1 or j == n-1 or i + j == n-1:
#             print("*", end='')
#         else:
#             print(" ", end='')
#     print()

'''
PATTERN 7

pyramid 

  *
 ***
*****

'''

# n = 5
# for i in range(1, n+1):
#     for j in range(1, 2*n):
#         if i+j>=n+1 and j-i<=n-1 or i==n:
#             print("*", end='')
#         else:
#             print(" ", end='')
#     print()

'''
PATTERN 8

upside down pyramid

'''

n = 5
for i in range(1, n+1):
    for j in range(1, 2*n):
        if i+j<=2*n and i==j or i==1:
            print("*", end='')
        else:
            print(" ", end='')
    print()