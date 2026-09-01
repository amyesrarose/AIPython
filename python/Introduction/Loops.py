"""""
Problem : Loops
Link  : https://www.hackerrank.com/challenges/python-loops/problem?isFullScreen=true
Level : Easy
Task  :
The provided code stub reads an integer, n, from STDIN. For all non-negative integers i<n, print i**2.
The list of non-negative integers that are less than n=3 is [0,1,2,3]. Print the square of each number on a separate line.

0
1
4
9
"""
if __name__ == '__main__':
    n= int(input())
    number_list = []

    for i in range(n): # beginning from 0 to n-1, as range is exclusive of the last number
        number_list.append(i) #each number is added to the list 

    power_value = 2 # to get square  of each number
    squared_steps =[] # to stored squared values of each number

    for num in number_list: # to get each number in the list and perform the operation of squaring
        result = num ** power_value # get square of  each number  in number list
        squared_steps.append(result)# adding each number in squared_steps
    print(*squared_steps, sep="\n") # * is used to unpack the list and display each number in a new line as requested in the question
