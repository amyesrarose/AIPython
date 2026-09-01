"""
Problem : Mutations
Link : https://www.hackerrank.com/challenges/python-mutations/problem?isFullScreen=true
Level : Easy
Task : 
Read a given string, change the character at a given index and then print the modified string.

Function Description
Complete the mutate_string function in the editor below.

mutate_string has the following parameters:
 string string: the string to change
 int position: the index to insert the character at
 string character: the character to insert

Returns
string: the altered string
Input Format

The first line contains a string, string.
The next line contains an integer position, the index location and a string character, separated by a space.

Sample Input

STDIN           Function
-----           --------
abracadabra     s = 'abracadabra'
5 k             position = 5, character = 'k'
"""
def mutate_string(string,position,character): # empty funtion given
    new_string = string[:position]+character+string[position+1:] #slicing sctrinh wit [:position] and level out the given position  and adding removed character into it
    return new_string # returning new_ string as result

if __name__ == '__main__': # This part given in the question and organizes user input
    s =input()
    i,c = input().split()
    s_new = mutate_string(s,int(i),c)
    print(s_new)