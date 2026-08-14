"""
Problem : String split and join
Link : https://www.hackerrank.com/challenges/python-string-split-and-join/problem?isFullScreen=true
Level : Easy
Task : 
In Python, a string can be split on a delimiter.

Example:
>>> a = "this is a string"
>>> a = a.split(" ") # a is converted to a list of strings. 
>>> print a
['this', 'is', 'a', 'string']
Joining a string is simple:

>>> a = "-".join(a)
>>> print a
this-is-a-string 
Task
You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

Function Description
Complete the split_and_join function in the editor below.
split_and_join has the following parameters:
string line: a string of space-separated words

Returns
string: the resulting string

Input Format
The one line contains a string consisting of space separated words.

Sample Input
this is a string  

Sample Output
this-is-a-string
"""
def split_and_join(line): # given method that I add funtions in it
    words = line.split(" ") # speration string from " " and creating string list
    return "-".join(words) # combining each word in lit with "-" and returning

if __name__ == '__main__':
    line = input() # reads user input
    result = split_and_join(line) # method called  and returning stored in result
    print(result) #printing result
  