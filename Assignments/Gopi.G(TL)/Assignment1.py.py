#1.Python Program to check prime number

num = int(input("Enter a number: "))

flag = False

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break

if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")

Output:
    Enter a number: 5
    5 is a prime number

#-------------------------------------------------------------------------------------#


# 2.Python program to print odd number in a given range

start = int(input("Enter the start of range:"))
end = int(input("Enter the end of range:"))
 
while(start<=end):
    if start% 2 != 0:
        print(start)
    start+=1
    
Output:
   Enter the start of range:1
   Enter the end of range:10
   1 3 5 7 9
   
#----------------------------------------------------------------------------------#
    
# 3.python program to print prime numbers

def isPrime(n):
  if(n==1 or n==0):
    return False
    
  for i in range(2,n):
    if(n%i==0):
      return False
    
  return True
  
N = int(input("Enter limit"));
for i in range(1,N+1):
  if(isPrime(i)):
    print(i,end=" ")
    

Output:
    Enter limit34
    2 3 5 7 11 13 17 19 23 29 31 

#----------------------------------------------------------------------------#    
    
#4.Python program to print Fibonacci number
def Fibonacci(n):
   
    if n < 0:
        print("Incorrect input")

    elif n == 0:
        return 0
 
    elif n == 1 or n == 2:
        return 1
 
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
num=int(input("enter number"))
print(Fibonacci(num))


Output:
    enter number9
    34
