""""
Link  : https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=trueProblem : Python If-Else
Level : Easy
Task  :
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer e.
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above.
Iterate through each command in order and perform the corresponding operation on your list.

Input Format
The first line contains an integer, n, denoting the number of commands.
Each line i of the n subsequent lines contains one of the commands described above.

Constraints
The elements added to the list must be integers.
Output Format
For each command of type print, print the list on a new line.

Sample Input 
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
Sample Output 0

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
"""""
if __name__ == '__main__':
    N = int(input())# reading how many line of data will be inserted
    values = [] # creating empty list to hold data as list
    for _ in range(N): #looping through each element in N
        line = input().split() #divide each input by empty space in it and store as a list to be able reach by index
        action = line[0] #first index (0) will show what action to be taking
        if action =="print":# this if statement here to determine to action to take
            print(values)        
        elif action == "sort":
            values.sort()
        elif action == "pop":
            values.pop()
        elif action == "reverse":
            values.reverse()
        elif action == "append":# when action is append
            val = int(line[1]) # index 1 will bring which value to put here  and cast to int to prevent data typr related failuare
            values.append(val)
        elif action == "insert":
            index = int(line[1])# after insert command index will be read in index one and store as integer
            val = int(line[2])# index 2 will show the value to read
            values.insert(index,val) # insert method will put val to given index
        elif action == "remove":
            val = int(line[1])
            values.remove(val)
