"""
Link : https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true
Problem : If-Else
Given an integer,n, perform the following conditional actions:
If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird
 

"""
def find_weird_or_not(n) : # writing if funtion to make a decision/ setting up to rules
      if n % 2 == 1 :  # selects all Odd numbers
        print("Weird")
      elif n>=2 and n<=5: # = add inclusivity
        print("Not Weird")
      elif n>=6 and n<=20:
        print("Weird")
      elif n>20 :
        print("Not Weird")       

if __name__ == '__main__':
    userinput= input ("Please enter value: ").strip() # removes unwanted characters in the string

    if userinput :
        n= int(userinput) # casting input to integer
        find_weird_or_not(n) #call the  funtion



   