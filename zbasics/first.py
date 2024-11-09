# n=[2,3,5,9,34,56]
# a=[]
# for i in n:
#     s=i**2
#     a.append(s)
# print(a)    

# a={int(x) for x in input().split()}
# print(a)

# x=input("enter a list of integers!")
# v=eval(x)
# print(type(v))
# for i in v:
#     print(i**2)


# n="1234"
# y="nul"
# print(f"hi {n} and how are you {y}, it's pleasant to see you {n}")
# print(1234,'res',4444,sep=":")

# x=256
# x1=256
# print(x is x1)
# print(id(x))
# print(id(x1))

#bitwise operators
# a=5
# b=3
# print(a&b,a|b,a^b,~a,a<<2,float(a>>2))  

#strings
# nam=input("Name: ")
# h=0
# for i in nam:
#     print(f"positive index is {h}, negative index is {h-len(nam)}", i)
#     h+=1


# n=input("enter the main string")
# m=input("Enter the substring")

# for i in n:
#     if i==m:
#         s1=n.find("i")
#         print("index is",s1)
        
#     elif i!=m:
#         continue
#     else:
#         print("substring is not found at index")

# s=input("Enter the substring: ")
# # print(s[::-1])
# #print(''.join(reversed(s)))
# i=len(s)-1
# target=""
# while i>=0:
#     target+=s[i]
#     i=i-1
# print(target)    

# s = input("Enter the substring: ")  # Prompts the user to enter a string and stores it in variable s

# # Commented out: These lines are alternative ways to reverse the string
# # print(s[::-1])  # This uses Python slicing to reverse the string and print it
# # print(''.join(reversed(s)))  # This uses the reversed() function and join() to reverse the string and print it

# i = len(s) - 1  # Sets i to the index of the last character in the string s
# target = ""  # Initializes an empty string to hold the reversed string

# # A while loop that runs as long as i is greater than or equal to 0
# while i >= 0:
#     target += s[i]  # Appends the character at index i to the target string
#     i = i - 1  # Decrements i by 1 to move to the previous character in the next iteration

# print(target)  # Prints the reversed string stored in target


#reverse order of words in string
# n=input().split()
# i=len(n)-1
# s=[]
# while i>=0:
#     s.append(n[i])
#     i=i-1
# print(" ".join(s))   

# n = input().split()  # Reads a line of input and splits it into a list of words
# i = len(n) - 1  # Sets i to the index of the last word in the list
# s = []  # Initializes an empty list to hold the words in reverse order

# # A while loop that runs as long as i is greater than or equal to 0
# while i >= 0:
#     s.append(n[i])  # Appends the word at index i to the list s
#     i = i - 1  # Decrements i by 1 to move to the previous word in the next iteration

# print(" ".join(s))  # Joins the words in list s with spaces and prints the resulting string


#reverse order of words internally in a string
# n=input().split()
# i=0
# s=[]
# while i<len(n):
#     s.append(n[i][::-1])
#     i=i+1
# print(" ".join(s))

##to find eve n and odd characters
# n=input()
# print("even characters are :" ,",".join(n[0::2]))
# print("odd characters are  :" ,",".join(n[1::2]))
# i=0
# print("even characters are : ")
# while i<len(n):
#     print(n[i],end=",")
#     i+=2
# print() 
# print("odd characters are : ")
# i=1
# while i<len(n):
#     print(n[i],end=",")
#     i+=2  
# print()


# n=input()
# i=len(n)-1
# s=''
# while i>=0:
#     s+=n[i]
#     i-=1
# print("Reversed String is: ",s.swapcase().split())    

# n=input().split()
# m=[]
# i=0
# while i<len(n):
#     m.append(n[i][::-1])
#     i+=1
# output=" ".join(m)    
# print(output)

#VALID PALINDROME
# s=input()
# s1 = ''.join([char for char in s if char.isalnum()])
# s1=s1.lower()
# #s1 = ''.join([char for char in s if char.isalnum()])
# s2=s1[::-1]
# print(s1,s2)
# if s1==s2:
#     print( True)
# else:
#     print( False) 
 
#reverse order of words which are even in a string
# n=input().split()
# m=[]
# i=0
# while i<len(n):
#     if i%2!=0:
#         m.append(n[i][::-1])
#     else:
#         m.append(n[i])
#     i+=1        
# print(' '.join(m))       




#reverse order of words internally in a string
# n=input().split()
# i=0
# s=[]
# while i<len(n):
#     s.append(n[i][::-1])
#     i=i+1
# print(" ".join(s))

##to find eve n and odd characters
# n=input()
# print("even characters are :" ,",".join(n[0::2]))
# print("odd characters are  :" ,",".join(n[1::2]))
# i=0
# print("even characters are : ")
# while i<len(n):
#     print(n[i],end=",")
#     i+=2
# print() 
# print("odd characters are : ")
# i=1
# while i<len(n):
#     print(n[i],end=",")
#     i+=2  
# print()

# n=input() 
# i=0
# even=''
# odd=''
# while i<len(n):
#     if i%2==0:
#         even+=n[i]
#     else:
#         odd+=n[i]  
#     i+=1    
# print("even characters are: ",even)
# print(odd)

#for loop - reverse order of words which are even in a string
# n=input().split()
# m=[]
# for i in range(len(n)):
#     if i%2==0:
#         m.append(n[i])
#     else:
#         m.append(n[i][::-1]) 
# print(' '.join(m))           

# n=input().split()
# i=0
# m=[]
# while i<len(n):
#     if i%2==0:
#         m.append(n[i])
#     else:
#         m.append(n[i][::-1])
#     i+=1
# print(' '.join(m))  
# 
#   
#adding characters alternately(merging)
# n=input()
# m=input()
# i,j=0,0
# k=''
# while i<len(n) or j<len(m):
#     if i<len(n):
#         k+=n[i]
#         i+=1
#     if j<len(m):
#         k+=m[j]
#         j+=1
# print(k)     

#SORTING ALPHABETS THEN NUMBERS
# from this/B2C1A3-- to this/ABC123
# n=input()
# i=0
# alpha=''
# digit=""
# while i <len(n):
#     if  n[i].isalpha():
#         alpha+=n[i]
#     else:
#         digit+=n[i]
#     i+=1    
# print(''.join((sorted(alpha)+sorted(digit)))) 

#another way

# n=input()
# alpha=[]
# digit=[]
# for i in n:
#     if i.isalpha():
#         alpha.append(i)
#     else:
#         digit.append(i)
# out=''.join(sorted(alpha)+sorted(digit))  
# print(out)    

#solve this /- a3b2c1 -- aaabbc
# n=input()
# out=''
# for i in n:
#     if i.isalpha():
#         s=i
#     else:
#         d=int(i) #here i is converted into int because we cannot multiply two characters in a string
#         out+=s*d 
# print(out)       
# 
# aaaaaabbbbcccdde===5a4b3c2d1e
# n=input()
# i=1
# prev=n[0]
# m=''
# c=1
# while i<len(n):
#     if n[i]==prev:
#         c+=1
#     else:
#         m+=str(c)+prev
#         c=1
#         prev=n[i]
#     if i==len(n)-1:
#         m+=str(c)+prev
#     i+=1            
# print(m)


# print(ord('z'))
# print(chr(77))

# n=input()
# i=0
# m=''
# while i<len(n):
#     if n[i].isalpha():
#         m+=n[i]
#         x=ord(n[i])
#     else:
#         y=x+int(n[i])
#         m+=chr(y)
#     i+=1    
# print(m)     
# 
#if there is a two digit number after alphabet then use this:
# n = input("Enter the encoded string: ")
# i = 0
# m = ''
# while i < len(n):
#     if n[i].isalpha():
#         m += n[i]
#         x = ord(n[i])
#         i+=1 
#     else:
#         num_str = ''
#         while i < len(n) and n[i].isdigit():
#             num_str += n[i]
#             i += 1
#         y = x + int(num_str)
#         m += chr(y)
       
# print(m)


# n=input("enter main string: ")
# m=input("enter sub string: ")
# for i in range(len(n)):
#     if n[i]==m:
#         print(f"substring {m} found at: ",i)
# finding unique vowels   
# n=input()
# v=["a","e","i","o","u"]
# f=[]
# for i in n:
#     if i in v:
#         if i not in f:
#             f.append(i)
# print(f)


# n=input()
# s=set(n)
# m=[10,20,30,"a"]
# s.update(m)
# print(s)
# print(s.pop())


#n=eval(int(input("enter the list")))
# def binary_search(A,target):
#     i=0
#     left=0
#     right=len(A)-1
#     while left<=right:
#         mid=(left+right)//2
#         if A[mid]==target:
#             return mid
#         elif A[mid] < target:
#             left=mid+1
#         elif A[mid] > target:
#             right=mid-1
#         else:
#             return -1           
        
# A=[1,2,4,8,9,11,16,22,28,29,30,31,34,35,38,39,43,44,56,76,88]
# target=88
# print(binary_search(A,target))

# def binary_search(A, target):
#     left = 0
#     right = len(A) - 1
    
#     while left <= right:
#         mid = (left + right) // 2
#         if A[mid] == target:
#             return mid
#         elif A[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
    
#     return -1

# A = [1, 2, 4, 8, 9, 11, 16, 22, 28, 29, 30, 31, 34, 35, 38, 39, 43, 44, 56, 76, 88]
# target = 22
# print(binary_search(A, target))


# def add(a,b):
#     sum=a+b
#     print(sum)
# add(4,4)

# def multiply(*args,**kwargs):
#     x=1
#     y=1
#     for i in args:
#         x*=i
#     for i,j in kwargs.items():
#         y*=j
#     product=x+y
#     return product
# s=multiply(1,3,5,8,a=54,b=32,c=22)
# print(s) 
 

# import math
# def paint(h,w) :
#     s=7
#     n=h*w /7
#     s=math.ceil(n)
#     print(s)
# paint(3,8)   
# 

#prime factors program

# def isPrime(n):
#     if n<2:
#         return False
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             return False
#     else:
#         return True

# def primeFactors(n):
#     l=[]
#     n1=n
#     for i in range(2,n+1):
#         while n%i==0:
#             l.append(i)
#             n//=i    
#     return l 
# n=int(input())
# print(primeFactors(n))     
# 
# 
#gcd
# n=int(input())
# m=int(input())

# for i in range(1,min(n,m)+1) :
#     if n%i==0 and m%i==0:
#         gcd=i
# print(f'gcd of {n} and {m} is: {gcd}')        

 

def calculate_total_distance(good_string: str, name: str) -> int:
    total_distance = 0
    prev_good_char = good_string[0]  # Initialize the previous good letter as the first in the good string
    
    for char in name:
        if char in good_string:
            prev_good_char = char  # If the character is already in the good string, no distance to be added
            continue
        
        min_distance = float('inf')  # Set a large initial value for minimum distance
        best_good_char = None  # Track the best good character for the current char
        
        # Find the closest good letter for this character
        for good_char in good_string:
            distance = abs(ord(char) - ord(good_char))  # Calculate distance
            
            if distance < min_distance:
                min_distance = distance
                best_good_char = good_char
            elif distance == min_distance:
                # If distances are equal, choose the letter closest to the previous good letter
                if abs(ord(prev_good_char) - ord(good_char)) < abs(ord(prev_good_char) - ord(best_good_char)):
                    best_good_char = good_char
        
        # Add the minimum distance to the total distance
        total_distance += abs(ord(char) - ord(best_good_char))
        
        # Update previous good letter to the chosen good letter
        prev_good_char = best_good_char
    
    return total_distance

# Input
good_string = input().strip()  # Good string from input
name = input().strip()         # Name of the student

# Output the result
result = calculate_total_distance(good_string, name)
print(result)


 
    




