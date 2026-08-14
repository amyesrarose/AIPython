"""
Problem : Find the Runner-Up Score
Link : https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true
Level : Easy
Task :
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

Input Format

The first line contains n. The second line contains an array  A[]  of n integers each separated by a space.

Constraints
2<= n <=10
-100 <= a[i] <=100

Output Format
Print the runner-up score.

Sample Input :
5
2 3 6 6 5
Sample Output :
5

"""
if __name__ == '__main__':
     n = int(input())
     arr = map(int, input().split()) # input  type is given in the question
     unique_arr = sorted(set(arr)) # I cast arr to set to remove duplicates and sorted 
     #set remove duplicate and sort wil pu them in ascending order
     second_largest = unique_arr[-2] # to get  second largest number [-] is used so second indesk from and would come. 
     #If we need the largest  [-1]
     #smalest[1]
     print(second_largest)