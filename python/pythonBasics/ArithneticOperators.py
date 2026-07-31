"""

The provided code stub reads two integers from STDIN, a and b. Add code to print three lines where:
The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.

"""
 # User input required, please enter 2 numbers

if __name__ == '__main__':
    a=int(input()) # store user's input as int 
    b=int(input())
   

    sum = a+b
    subs = a-b
    product = a*b

    print(sum,subs,product, sep= "\n") # sep="\n" display each parameter in difeerent line