"""
Problem : Swap Case
Link : https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true
Level : Easy
Task :
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

For Example:
Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2  

Function Description
Complete the swap_case function in the editor below. 

swap_case has the following parameters:
 string s: the string to modify

 Returns
string: the modified string

Input Format
A single line containing a string .

Constraints
0< len(s)<=1000

Sample Input 0
HackerRank.com presents "Pythonist 2".

Sample Output 0
hACKERrANK.COM PRESENTS "pYTHONIST 2".
"""

def swap_case(s): # given funtion from question 
    return s.swapcase()  # I just called built in swapcase() method

if __name__ == '__main__': # main class  is given in the question
    s = input() # reads user input
    result = swap_case(s) # swap_case("input") method is called and return is rtored in result
    print(result) # result is printed.
    