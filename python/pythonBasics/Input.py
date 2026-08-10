"""
Problem : Input()
Link : https://www.hackerrank.com/challenges/input/problem?isFullScreen=true
Task :

You are given a polynomial P of a single indeterminate (or variable), x .
You are also given the values of x and k. Your task is to verify if .

Constraints
All coefficients of polynomial P are integers.
 and x are y also integers.

Input Format

The first line contains the space separated values of x and k.
The second line contains the polynomial P.

Output Format

Print True if P(x) == k. Otherwise, print False.

"""
var = input() # Reading user input

x= int(var[0]) #first chracter will be x we need to get first index to get x
k= int(var[2]) # second number  will be in index 2 since valuaes are space separated.

for i in range(k,1,-1): # To calculate polinomial value we need loop. will beging in k reduce to 1

    container = i**i # to calculate polinamial 
    i=i+1 # Python does not have increamenr so we add to increment the i value

if container == k: #enters if  k equals to polinomial value we calculated
    print("True")   #prints "True" when container and k has same value
else:
    print("False") #prints "False" when container and k are different