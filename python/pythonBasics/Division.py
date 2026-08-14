"""
Problem :Python : Division
Link : https://www.hackerrank.com/challenges/python-arithmetic-operators/problem?isFullScreen=true
Level : Easy
Task :
The provided code stub reads two integers, a and b, from STDIN.
Add logic to print two lines. The first line should contain the result of integer division,  a//b . The second line should contain the result of float division,  a/b .

"""
if __name__ == '__main__':
    a = int(input())
    b = int(input())

    div_int = int(a/b) # cast to int result is always whole number
    div_float = a/b # without cast decimal numbers wil be displayed

    print(div_int,div_float, sep="\n") # prints  divInt and DivFloat in different line as requiested in the question