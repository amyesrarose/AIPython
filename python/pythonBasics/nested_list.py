"""
Problem : Nested Lists
Link : https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true
Level : Easy
Task :
Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

Example : records = [["chi",20.0],["beta",50.0], ["alpha"],50.0]

The ordered list of scores is [20.0,50.0], so the second lowest score is [50.0] . There are two students with that score: ["beta","alpha"]. Ordered alphabetically, the names are printed as:
alpha
beta

Input Format

The first line contains an integer, N,2N the number of students.
The  subsequent lines describe each student over 2 lines.
- The first line contains a student's name.
- The second line contains their grade.

Constraints

2<=N<= 5
There will always be one or more students having the second lowest grade.

Output Format
Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, order their names alphabetically and print each one on a new l

Sample Input

5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

Sample Output

Berry
Harry

"""

if __name__ == '__main__':
    students = [] # creating list to hold name and score pairs as list
    for _ in range(int(input())):
        name = input() #reading name
        score = float(input()) #reading score
        students.append([name,score]) # adding name and score in the list
    no_dup_list = sorted(list(set(score for name,score in students))) #casting to set to remove duplicates
    #casting to list since set is not ordered
    # sorted() sort the list lowest to highest
    second_low= no_dup_list[1]# reading index one to get second lowest value
    second_low_students= sorted([name for name,score in students if score ==second_low]) # iterating through list of students
    # to get names of the students who has second lowest value since set removed duplicate values and putting in sorted() to get alphabetical order
    print(*second_low_students, sep="\n") #unpacking and putting each value in new line for required format