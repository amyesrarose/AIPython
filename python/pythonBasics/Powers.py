"""
Problem : Python Powers

Link : https://www.hackerrank.com/challenges/python-power-mod-power/problem?isFullScreen=true

Task :
You are given three integers: a, b, and m. Print two lines.
On the first line, print the result of pow(a,b). On the second line, print the result of pow(a,b,m).

Input Format
The first line contains a, the second line contains b, and the third line contains m.
"""
if __name__ == '__main__':

    a = int(input()) # create 3 different input as mentioned in the question
    b = int(input())
    m = int(input())

    print(pow(a,b)) # prints a power of b. "pow" is a built in funtion
    print(pow(a,b,m)) # prints result of (a **b) % m  using built in method
