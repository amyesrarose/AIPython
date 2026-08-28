"""
Problem : Tuple
Link : https://www.hackerrank.com/challenges/python-tuples/problem?isFullScreen=true
Level : Easy
Task :
Given an integer,n, and n space-separated integers as input, create a tuple,t, of those n integers. Then compute and print the result of hash(t).

Input Format
The first line contains an integer,n, denoting the number of elements in the tuple.
The second line contains n space-separated integers describing the elements in tuple  t.

Output Format
Print the result of hash(t).

Sample Input 
2
1 2

Sample Output 
3713081631934410656


"""
if __name__ == '__main__' : 
     n= int(input()) #reading user input
     integer_list = map(int, input().split()) #reading user input and storing integer_list
     integer_tuple = tuple(integer_list) # casting to tuple data types
     print(hash(integer_tuple)) #question require to get hash value built in method hash() bring the value and printing