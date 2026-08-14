"""
Problem : List Comprehensions

Link : https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true

Task :Let's learn about list comprehensions! You are given three integers x,y and z representing the dimensions of a cuboid along with an integer n.
Print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of i+j+k  is not equal to n.
Here,0<=i<=x, 0<=j<=y, 0<=k,=zx . Please use list comprehensions rather than multiple loops, as a learning exercise.

Input Format

Four integers  x,y,z and n, each on a separate line.

Constraints

Print the list in lexicographic increasing order.

Sample Input 0

1
1
1
2
Sample Output 0

[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
"""
if __name__ == '__main__':
    x = int(input()) # for single line data entry as requested in the question
    y = int(input())
    z = int(input())
    n = int(input())
"""
since question spesifically asked list comprehension we use this format
new_list = [expression for item in iterable if condition] since our question required 3 dimenrsion we used 3 dimension i,j,k
list comprehension allow us to write nested loop in a single line and we filter on wanted result with  if statement
"""
cordinates = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k !=n]
print(cordinates)


'''' if we did not used list comprehension code will look like this
coordinates = []
for i in range(x + 1):
    for j in range(y + 1):
        for k in range(z + 1):
            if i + j + k != n:
                coordinates.append([i, j, k])

'''
