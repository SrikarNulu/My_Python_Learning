#------------------->>>>>>>>>>>>>>> DESCRIPTION OF BASIC MATH  <<<<<<<<<<<<<<<<<<<----------------------------
# Counting Digits
# Description: Counting the number of digits in a given number.
# Method: Convert the number to a string and count the length, or use logarithmic properties.

# Reversing a Number
# Description: Reversing the digits of a number.
# Method: Convert the number to a string, reverse the string, and convert it back to an integer.

# Palindrome Number
# Description: Checking if a number reads the same forward and backward.
# Method: Convert the number to a string and check if the string is equal to its reverse.

# Greatest Common Divisor (GCD)
# Description: The largest number that divides two numbers without leaving a remainder.
# Method: Use the Euclidean algorithm.

# Armstrong Number
# Description: A number that is equal to the sum of its own digits each raised to the power of the number of digits.
# Method: Sum the digits each raised to the power of the number of digits and check if it equals the original number.

# Divisors of N
# Description: Finding all the numbers that divide 
# 𝑛
# n without leaving a remainder.
# Method: Iterate from 1 to 
# 𝑛
# n and check divisibility.

# Prime Number
# Description: A number greater than 1 with no divisors other than 1 and itself.
# Method: Check divisibility from 2 to the square root of the number.

# Factorial
# Description: The product of all positive integers up to a given number 
# 𝑛
# n.
# Method: Multiply all integers from 1 to 
# 𝑛
# n.

# Least Common Multiple (LCM)
# Description: The smallest number that is a multiple of two or more numbers.
# Method: Use the relationship 
# LCM
# (
# 𝑎
# ,
# 𝑏
# )
# =
# ∣
# 𝑎
# ⋅
# 𝑏
# ∣
# GCD
# (
# 𝑎
# ,
# 𝑏
# )
# LCM(a,b)= 
# GCD(a,b)
# ∣a⋅b∣
# ​
#  .

# Perfect Number
# Description: A number equal to the sum of its proper divisors (excluding itself).
# Method: Sum all divisors of the number excluding the number itself and check if it equals the original number.

# Sum of Digits
# Description: Adding all the digits of a number.
# Method: Convert the number to a string and sum the integer values of its characters.

# Product of Digits
# Description: Multiplying all the digits of a number.
# Method: Convert the number to a string and multiply the integer values of its characters.

# Sum of First N Natural Numbers
# Description: Calculating the sum of the first 𝑛
# n natural numbers.
# Method: Use the formula 𝑛(𝑛+1)22n(n+1).

# Power of a Number (Exponentiation)
# Description: Calculating (𝑎𝑏a) b  for given numbers 𝑎 a and 𝑏 b.
# Method: Use repeated multiplication or Python’s built-in exponentiation operator **.

# Perfect Square
# Description: A number that is the square of an integer.
# Method: Check if the square root of the number is an integer.

# Fibonacci Sequence
# Description: Generating the sequence where each number is the sum of the two preceding ones.
# Method: Start with 0 and 1 and continue adding the last two numbers to generate the next one.

# Number of Trailing Zeros in Factorial
# Description: Counting the number of trailing zeros in the factorial of a number.
# Method: Count the number of times 5 is a factor in the numbers from 1 to 𝑛 n.

# Binary Representation of a Number
# Description: Converting a number to its binary form.
# Method: Use Python’s built-in bin() function or convert manually by repeatedly dividing by 2.

# Check if a Number is Even or Odd
# Description: Determining if a number is even or odd.
# Method: Check if the number modulo 2 equals 0 (even) or 1 (odd).

# Check if a Number is a Power of Two
# Description: Determining if a number is a power of two.
# Method: Check if there is only one bit set in the binary representation.
# Square Root of a Number
# Description: Calculating the square root of a number.
# Method: Use Python’s built-in math.sqrt() function or an iterative approximation method like Newton's method.

#------------------->>>>>>>>>>>>>>>END>>>>>------- DESCRIPTION OF BASIC MATH  <<<<<<<<<<<<<<<<<<<----------------------------

   

#------->>>>>>>>>>>> BASIC MATH <<<<<<<<<<------------#
# 1)BRUTE FORCE: counting digits #TC- O(log10N+1)  #SC- O(1)
# n=int(input())
# c=0
# while n>0:
#     c+=1
#     n//=10
# print(c)

# OPTIMAL  #TC- O(1)  #SC- O(1)
# from math import *
# n=int(input())
# print(int(log10(n)+1))  


#2)REVERSING A NUMBER #OPTIMAL TC- O(log10N+1)  #SC- O(1)
# n=int(input())
# rev=0
# while n>0:
#     s=n%10
#     rev=rev*10 + s
#     n//=10
# print(rev)    

#3)PALINDROME NUMBER #OPTIMAL TC- O(log10N+1)  #SC- O(1)
# n1=int(input())
# n=n1
# rev=0
# while n>0:
#     s=n%10
#     rev=rev*10 + s
#     n//=10
# if rev==n1:
#     print(True)
# else:
#     print(False)    


#4)<<<<<<<<<<<<<<<---------GREATEST COMMON DIVISOR OR HIGHEST COMMON FACTOR --------->>>>>>>>>>>>>
# Step 1: Initialise a variable gcd to 1. This variable will store the greatest common divisor of the input numbers n1 and n2.

# Step 2: Iterate from 1 to the minimum of n1 and n2.

# We start from 1 because the GCD of any two numbers is at least 1, and it cannot be greater than the smaller of the two numbers.
# Step 3: At each iteration, if i is a common factor of both n1 and n2 update the gcd variable to i. We keep updating gcd as long as we find common factors.

# Step 4: After the iteration, the gcd variable will store the greatest common divisor of n1 and n2. Return this value as the output of the function.
#BRUTE FORCE ------ Time Complexity: O(min(N1, N2)) Space Complexity: O(1)
# n1=int(input())
# n2=int(input())
# gcd=1
# for i in  range(1,min(n1,n2)+1):
#     if n1%i==0 and n2%i==0:
#         gcd=i
# print(gcd)        

#BETTER APPROACH  ----reversal of brute----  Time Complexity: O(min(N1, N2)) Space Complexity: O(1) tc is same but takes less iterations
# n1=int(input())
# n2=int(input())
# gcd=1
# for i in  range(min(n1,n2), 0,-1):
#     if n1%i==0 and n2%i==0:
#         gcd=i
#         break
       
# print(gcd)  

#OPTIMAL APPROACH:  Time Complexity: O(log(min(N1, N2))) -- Space Complexity: O(1) EUCLIDEAN ALGORITHM

# Euclidean Algorithm

'''The Euclidean algorithm is an efficient method for finding the GCD of two integers.
 The algorithm is based on the principle that the GCD of two numbers also divides their difference. Here’s how it works:

## Initial Idea

For two integers `a` and `b`, the GCD of `a` and `b` is the same as the GCD of `b` and `a % b` (where `%` denotes the modulus operation). 
This is because any common divisor of `a` and `b` must also divide the difference `a - b * k` (where `k` is the quotient of `a / b`).

## Algorithm Steps

1. **Start with two numbers,** `a` and `b`.
2. **Replace** `a` with `b` and `b` with `a % b`.
3. **Repeat this process** until `b` becomes 0.
4. **When `b` is 0,** `a` contains the GCD. '''



# a1=int(input())
# b1=int(input())
# a=a1
# b=b1
# while b!=0:
#     a,b=b,a%b
# print(a)
# #LCM = abs(a*b)//gcd(a,b)
# l=abs((a1*b1)//a)
# print(l)

#GCD
# def gcd(a,b):
#     while b!=0:
#         a,b=b,a%b
#     return a
# # a,b=map(int,input().split())
# # print(gcd(a,b))  

# def lcm(a,b):
#     return abs(a*b)//gcd(a,b)
# a,b=map(int,input().split())    
# print(lcm(a,b))

# def gcd(a,b):
#     while a>0 and b>0:
#         if a>b:
#             a=a%b
#         else:
#             b=b%a
#     if a==0:
#         return b
#     else:
#         return a            
# a,b=map(int,input().split())
# print(gcd(a,b))

#5)ARMSTRONG NUMBER 153--- 1^3 + 5^3 + 3^3 =153  then it is armstrong number ---->>>Time Complexity: O(log10N + 1), Space Complexity: O(1)
# import math
# n=int(input())
# n1=n
# c=int(math.log10(n)+1)
# arm=0
# while n>0:
#     s=n%10
#     arm+=s**c
#     n//=10
# if arm==n1:
#     print(True) 
# else:
#     print(False)    
# 
 
#6)DIVISORS OF N 
#BRUTE FORCE ----->>>>>  Time Complexity: O(N), Space Complexity : O(N)
# n=int(input())
# s=[]
# c=0
# for i in range(1,n+1):
#     if n%i==0:
#         s.append(i)
#         c+=1

# print(s, "count is: ",c)

#OPTIMAL --- Time Complexity: O(sqrt(N)), Space Complexity : O(2*sqrt(N))
# import math 
# n=int(input())
# s=[]
# c=0
# Sqrt=int(math.sqrt(n))
# for i in range(1,Sqrt+1):
#     if n%i==0:
#         s.append(i)
#         c+=1
#         if i != n//i:
#             s.append(n//i)
#             c+=1

# print(s, "count is:",c)

#7) PRIME NUMBER 
#BRUTE FORCE  ----  Time Complexity: O(N),Space Complexity : O(1)
# n=int(input())
# c=0
# for i in range(1,n+1):
#     if n%i==0:
#         c+=1
# if c==2:
#     print(True)
# else:
#     print(False) 
# 
#OPTIMAL APPROACH ----  Time Complexity: O(sqrt(N)), Space Complexity : O(1)
# import math
# n=int(input())
# if n>1:
#     for i in range(2,int(math.sqrt(n))+1):
#         if n%i==0:
#             print(False)
#             break
#     else:
#         print(True)       
# else:
#     print(False)

#8)FACTORIAL ---- Time Complexity: O(N), Space Complexity : O(1)
# def factorial(n):
#     result=1
#     for i in range(1,n+1):
#         result=result*i
#     return result    
# n=int(input())
# print(factorial(n))  

#9)LCM ---->>> time complexity: O(log(min(a,b))), Space Complexity : O(1)

# import math
# def lcm(a,b):
#     Gcd=math.gcd(a,b)
#     Lcm=abs ((a*b)//(Gcd) )    
#     return Lcm
# a,b=map(int,input().split())
# print(lcm(a,b)) 

#-------->>>OR<<<<<--------
# import math
# def lcm(a,b):
    
#     return abs((a*b)//(math.gcd(a,b)))    
   
# a,b=map(int,input().split())
# print(lcm(a,b)) 

#10)PERFECT NUMBER
#BRUTE FORCE
# def perfect_number(n):
#     s=0
#     for i in range(1,(n//2)+1):
#         if n%i==0:
#             s+=i
            
#     if s==n:
#         return f"{n} is a Perfect Number"
#     else:
#         return f"{n} is not a Perfect Number"            
# n=int(input())
# print(perfect_number(n))

#OPTIMAL SOLUTION --->>>>>>> time complexity: O(n**0.5), space complexity: O(1)

# import math
# def perfect_number(n):
#     if n<2:
#         return False
#     s=1
#     for i in range(2,int(math.sqrt(n))+1):
#         if n%i==0:
#             s+=i
#             if n//i !=i:
#                 s+=n//i
#     if s==n:
#         return f"{n} is a Perfect Number"
#     else:
#         return f"{n} is not a Perfect Number"            
# n=int(input())
# print(perfect_number(n))

#11)FIBONACCI SEQUENCE  (0,1,1,2,3,5,8,13,21,34,55,89...)  tc: O(n), sc: O(1)
# def fibonacci(n):
#     fib=[]
#     a,b=0,1
#     for i in range(0,n):
#         fib.append(a)
#         print(fib)
#         a,b=b,a+b
#         return fib
# n=int(input())
# print(fibonacci(n))

#13)PRIME FACTORS OF A NUMBER
#Brute Force tc: O(N * root N) sc-o(1) wc:O(n)
# import math
# def isPrime(n):
#     if n<2:
#         return False
#     for i in range(2,int(math.sqrt(n)+1)): 
#         if n%i==0:
#             return False
#     else:
#         return True        

# def primeFact(n):
#     l=[]
#     for i in range(2,n+1):
#         if n%i==0 and isPrime(i) :
#             l.append(i)
#     return l
# n=int(input())
# print(primeFact(n))    
# 

# BETTER APPROACH  tc: O(N**0.5 * 2* N**0.5) sc-o(1) wc:O(K)
# import math
# def isPrime(n):
#     if n<2:
#         return False
#     for i in range(2,int(math.sqrt(n)+1)): 
#         if n%i==0:
#             return False
    
#     return True        

# def primeFact(n):
#     l=[]
#     for i in range(2,int(math.sqrt(n))+1):
#         if n%i==0: 
#             if isPrime(i):
#                 l.append(i)
#             if n//i !=i and isPrime(n//i):
#                 l.append(n//i)
#     if isPrime(n) and n>1:
#         l.append(n)
#     return l    

# n=int(input())
# print(primeFact(n))                         


#IF THE NUMBER HAVE MULTIPLE SAME FACTORS ex: 18- 2*3*3, (3 repeated 2 times, above code doesn't include 3 two times it include only one time below code will work )
#BETTER APPROACH CHANGED VERSION

# import math
# def isPrime(n):
#     if n<2:
#         return False
#     for i in range(2,int(math.sqrt(n)+1)): 
#         if n%i==0:
#             return False
#     return True        

# def primeFact(n):
#     l=[]
#     n1=n
#     for i in range(2,int(math.sqrt(n))+1):
#         while n%i==0:   # Check for multiple factors
#             if isPrime(i):
#                 l.append(i)
#             n//=i   # Reduce n by dividing it by i

#     # If n is still greater than 1, then it must be a prime factor
#     if isPrime(n) and n>1:
#         l.append(n)
#     return l    

# n=int(input())
# print(primeFact(n))                         


#<<<<<<<<-----OPTIMAL-------BEST VERSION------->>>>>>-----SIMPLIFIED APPROACH TO FIND PRIME FACTORS
#Time Complexity: o(root n * log n), Space Complexity:0(log N)
# def primeFactors(n): 
#     l=[]
#     for i in range(2,int(n**0.5)+1):
#         while n%i==0:
#             l.append(i)
#             n//=i
#     if n>1 :
#         l.append(n) 
#     return l   
# n=int(input())
# print(primeFactors(n)) 
# 
#if only single factor as output not multiple ex: 64 2*2*2*2*2*2----->>>output=[2] for above [2,2,2,2,2]
# def primeFactors(n):  
#     l=[]
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             l.append(i)
#             while n%i==0:
#                 n//=i
#     if n>1 :
#         l.append(n) 
#     return l   
# n=int(input())
# print(primeFactors(n)) 

#Power Exponentiation (without pow() and **)
#Time Complexity: o(log n), Space Complexity:0(1)
# def power(x,n):
#     m=n
#     ans=1.0
#     if n<0:
#         n= -n
#     while n>0:
#         if n%2==1:
#             ans*=x
#             n-=1
#         n=n//2
#         x=x*x
#     if m<0:
#         ans=1.0/ans
#     return ans               
# x,n=map(int,input().split())
# print(power(x,n))


#Sieve of Eratosthenes( printing all primes for given n)
#Brute Force ----->>>Time Complexity: o(n* root n), Space Complexity:0(1)
# def isPrime(n):
#     if n<2:
#         return False
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             return False
#     return True           
# def sieve(n):
#     s=[]
#     for i in range(n+1):
#         if isPrime(i):
#             s.append(i)
#     return s        
# n=int(input())
# print(sieve(n))

 
#quadratic equation
# def quad(a,b,c):
#     d=(b**2-4*a*c)
#     sqrt_value=d**0.5
#     if d>0:
#         s1=-b+sqrt_value/2*a
#         s2=-b-sqrt_value/2*a
#         z=s1,s2
#         return list(z)   
#     elif d==0:
#         s1=s2=-b/2*a
#         z=s1,s2
#         return list(z) 
#     else:
#         real=-b/2*a
#         img=sqrt_value/2*a
#         s1=real, img
#         s2=real, -img
#         z=s1,s2
#         return list(z)      
# a,b,c=map(int, input().split())
# print(quad(a,b,c))   

