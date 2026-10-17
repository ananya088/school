# ==================================================
# TOPIC 9: PATTERN PROGRAMS IN PYTHON
# ==================================================

# 1. Pattern Programs
# Definition:
# Pattern programs are used to print numbers, stars,
# or other characters in a particular shape using loops.

# Important:
# The outer loop controls the rows.
# The inner loop controls the items printed in each row.


# ==================================================
# 2. Square Star Pattern
# ==================================================

# Definition:
# A square pattern prints the same number of stars in each row.

# Example:
for i in range(4):
    for j in range(4):
        print("*", end=" ")
    print()

# Output:
# * * * *
# * * * *
# * * * *
# * * * *

# Explanation:
# The outer loop runs 4 times.
# The inner loop prints 4 stars in each row.
# print() moves to the next line.


# ==================================================
# 3. Right-Angled Triangle Star Pattern
# ==================================================

# Definition:
# A triangle pattern prints an increasing number of stars
# in each row.

# Example:
for i in range(1, 5):
    for j in range(i):
        print("*", end=" ")
    print()

# Output:
# *
# * *
# * * *
# * * * *

# Explanation:
# The number of stars increases by one in each row.


# ==================================================
# 4. Inverted Triangle Star Pattern
# ==================================================

# Definition:
# An inverted triangle prints fewer stars in each row.

# Example:
for i in range(4, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

# Output:
# * * * *
# * * *
# * *
# *


# ==================================================
# 5. Number Triangle Pattern
# ==================================================

# Definition:
# A number triangle prints increasing numbers in each row.

# Example:
for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Output:
# 1
# 1 2
# 1 2 3
# 1 2 3 4


# ==================================================
# 6. Repeated Number Triangle
# ==================================================

# Definition:
# Each row prints the row number repeatedly.

# Example:
for i in range(1, 5):
    for j in range(i):
        print(i, end=" ")
    print()

# Output:
# 1
# 2 2
# 3 3 3
# 4 4 4 4


# ==================================================
# 7. Increasing Number Pattern
# ==================================================

# Definition:
# This pattern prints consecutive numbers in each row.

# Example:
num = 1

for i in range(1, 5):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

# Output:
# 1
# 2 3
# 4 5 6
# 7 8 9 10


# ==================================================
# 8. Inverted Number Triangle
# ==================================================

# Definition:
# This pattern prints decreasing numbers of items per row.

# Example:
for i in range(4, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Output:
# 1 2 3 4
# 1 2 3
# 1 2
# 1


# ==================================================
# 9. Right-Aligned Triangle
# ==================================================

# Definition:
# A right-aligned triangle uses spaces before the stars.

# Example:
for i in range(1, 5):
    print("  " * (4 - i) + "* " * i)

# Output:
#       *
#     * *
#   * * *
# * * * *

# Explanation:
# Spaces decrease as the number of stars increases.


# ==================================================
# 10. Pyramid Star Pattern
# ==================================================

# Definition:
# A pyramid pattern prints stars in a centered shape.

# Example:
for i in range(1, 5):
    print(" " * (4 - i) + "* " * i)

# Output:
#    *
#   * *
#  * * *
# * * * *

# Explanation:
# Spaces are printed before the stars to create the shape.


# ==================================================
# 11. Diamond Star Pattern
# ==================================================

# Definition:
# A diamond pattern combines an increasing and a decreasing
# star pattern.

# Example:
n = 4

for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)

for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "* " * i)

# Output:
#    *
#   * *
#  * * *
# * * * *
#  * * *
#   * *
#    *


# ==================================================
# 12. Important Points to Remember
# ==================================================

# 1. Pattern programs commonly use nested loops.
# 2. The outer loop controls the rows.
# 3. The inner loop controls the items in each row.
# 4. end=" " prints items on the same line.
# 5. print() moves to the next line.
# 6. range(1, 5) produces 1, 2, 3, 4.
# 7. Spaces can be used to align patterns.


# ==================================================
# 13. Practical Questions
# ==================================================

# Easy:
# 1. Print a square pattern of 5 rows and 5 columns.
for i in range(5):
    for j in range(5):
        print("*",end=" ")
    print()    
# 2. Print a right-angled triangle using stars.
for i in range(1,6):
    for j in range(i):
        print("*",end=" ")
    print()    
# 3. Print a triangle using numbers.
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()    

# Medium:
# 4. Print an inverted star triangle.
for i in range(5,0,-1):
    for j in range(i):
        print("*",end=" ")
        print()
# 5. Print a repeated-number triangle.
for i in range(1,6):
    for j in range(i):
        print(i,end=" ")
    print()    
# 6. Print an increasing number pattern.
for i in range(1,6):
    for j in range(i):
        print(num,end=" ")
        num+=1
    print()
# Hard:
# 7. Print a right-aligned star triangle.
for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end=" ")
    for k in range(i):
        print("*", end=" ")
    print()
# 8. Print a pyramid star pattern.
for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()
# 9. Print a diamond star pattern.
for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()

for i in range(4, 0, -1):
    for j in range(5 - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()


# ----------------------------------------------------------------------------------------
# for i in range(4):
#     for j in range(4):
#         print("1",end="")
#     print()                       

# -------------------------------------------


# for i in range(1,6):
#     for j in range(i):
#         print("*",end="")
#     print() 
  
#  ------------------------------------

# for i in range(5):
#     for j in range(10):
#         print("*",end="")
#     print()     

# ---------------------------------- 
#    
# for i in range(6,-1,-1):
#     for j in range(i):
#         print("*",end="")
#     print() 
# -----------------------------------

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()
# ----------------------------------------

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i,end="")
#     print()    
# # -------------------------------------

# for i in range(6,-1,-1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()
# ----------------------------------

# for i in range(1,6):
#     for j in range(1,i+1): 
#         print(chr(j+64),end=" ")
#     print()   
# ---------------------------
# for i in range(6,-1,-1):
#     for j in range(1,i+1):
#         print(chr(j+64),end=" ")
#     print()    