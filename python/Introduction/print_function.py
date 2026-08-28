"""
Problem : Print Function
Link : https://www.hackerrank.com/challenges/python-print/problem?isFullScreen=true
Level : Easy
The included code stub will read an integer,n, from STDIN.
Without using any string methods, try to print the following:
123.....n
Note that "..." represents the consecutive values in between.

Example
n=5
Print the string 12345.

"""

if __name__ == '__main__':
    n = int(input())
    cons_values = [] # creating empty list to store each value comes before n

    for i in range(1,n+1): #default  range starts from 0, Question ask output to begin  from 1  and with the printed number ,
        # since stop does not get printed n+1 is added to see n in the output
        cons_values.append(i) # looping through each number and adding to container

    print(*cons_values, sep="") #unpack the  list and display each number sidebyside without comma or space   