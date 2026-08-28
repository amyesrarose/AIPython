"""
Problem :Capitalized
Link :https://www.hackerrank.com/challenges/capitalize/problem?isFullScreen=true
Level : Easy
Task : 
You are asked to ensure that the first and last names of people begin with a capital letter in their passports.
 For example, alison heck should be capitalised correctly as Alison Heck.

Given a full name, your task is to capitalize the name appropriately.

Input Format
A single line of input containing the full name,S.

Constraints
0<len(S)<1000
The string consists of alphanumeric characters and spaces.

Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.

Output Format
Print the capitalized string, S.

Sample Input
chris alan

Sample Output
Chris Alan
"""

def solve(s):
 words = s.split(" ") # separating  from white space so each word can be found
 #stored in words list
 capitalized_str = [word.capitalize() for word in words] # loop through each word in list and capitalized each word
 return ' '.join(capitalized_str) # join,combines each word together with a space 

if __name__ == "__main__": # class
    s = input() # reading user input
    result = solve(s) # calls solve(input) mmethod and returns result and stores as result
    print(result) # prints result to console

