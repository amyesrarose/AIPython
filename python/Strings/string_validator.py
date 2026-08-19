"""
Problem : String Validator
Link : https://www.hackerrank.com/challenges/string-validators/problem?isFullScreen=true
Level : Easy
Task : Task

You are given a string S.
Your task is to find out if the string  contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

Input Format
A single line containing a string .

Constraints
0<lend(s)<1000

Output Format

In the first line, print True if S has any alphanumeric characters. Otherwise, print False.
In the second line, print True if S has any alphabetical characters. Otherwise, print False.
In the third line, print True if S has any digits. Otherwise, print False.
In the fourth line, print True if S has any lowercase characters. Otherwise, print False.
In the fifth line, print True if S has any uppercase characters. Otherwise, print False.

Sample Input
qA2

Sample Output
True
True
True
True
True
"""
if __name__ == '__main__':
    s = input()
    has_alpha = has_alnum = has_digit = has_lower = has_upper = False # Assigning each value as False and future codes will chnage then True if they found the characteristic 
    for ch in s: # putting in a loop to visit each character in the string
        if ch.isalnum(): #when found alphanumeric character in string
            has_alnum = True # assigns a True value, if not value will stay False 
        if ch.isalpha():
            has_alpha = True 
        if ch.isdigit():
            has_digit = True  
        if ch.islower():
            has_lower = True   
        if ch.isupper():
            has_upper = True        
    print(has_alnum)  # printing one by one each result
    print(has_alpha)   
    print(has_digit) 
    print(has_lower) 
    print(has_upper)  
    print(has_lower)   