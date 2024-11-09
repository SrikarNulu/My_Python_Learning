#traversal to each element of an array

# def travel(arr):
#     s=[]
#     for i in arr:

#         s.append(i)

#     return s[11:-12:-1]    
        

# array=[1,2,3,4,5,6,7,8,9,10,11]

# print(travel(array))

#insertion of element

# arr=[1,2,3,4,5,6,7,9]

# arr.insert(7,899) 

# print(arr)     


#delete element

# arr=[1,2,3,4,5,6,7,8,9]
# for  i in arr[:]:

#     if i%2==0:

#         arr.remove(i) 

# print(arr)        


# arr=[1,2,3,4,5,6,7,8,9]

# del arr[0:3]

# print(arr)


# arr=[1,2,3,4,5,6,7,8,9]

# arr.remove(3)

# print(arr)


# arr=[1,2,3,4,5,6,7,8,9]
# for i in arr[:]:

#     if i%2==0:

#         arr.remove(i)

# print(arr)

# def delete_element(arr,index):

#     del arr[index]

#     return arr

# arr=[1,2,3,4,5,6,7,8,9]

# arr=delete_element(arr,2)

# print(arr)


#>25 and 2>5


# n=int(input())


# if n>25:
#     s=list(n)

#     for i in range(0,len(s)):

#         if s[i] > s[i+1]:

#             print(True)
#         else:

#             print(False)    
# else:

#     print(False)      



#second maximum element in an array


# arr=[1,2,3,12,22,13,17,54,55,53,57,89,88,79,99,89,93]
# arr=[1,1,1,1,1,1,1,1,2]

# maxi=float('-inf')

# sec_maxi=float('-inf')
# for i in arr:

#     if i>maxi:

#         sec_maxi=maxi
#         maxi=i

#     elif i>sec_maxi and i<maxi:

#         sec_maxi=i

# if sec_maxi==float('-inf'):

#     sec_maxi=-1
               

# print(sec_maxi, maxi)


#n largest elements


# arr=[1,2,3,12,22,13,17,54,55,53,57,89,88,79,99,89,93]

# n=4
# l=[]
# s=set()


# for i in range(n):

#     maxi=-float('inf')
#     for j in range(0,len(arr)):
#         if arr[j]>maxi and arr[j] not in s:
#             maxi=arr[j]

#     l.append(maxi)
#     s.add(maxi)
#     arr.remove(maxi)

# print(l) 

# #or
# n=4
# arr=[1,2,3,12,22,13,17,54,55,53,57,89,88,79,99,89,93]
# arr.sort(reverse=True)
# k=[]

# for i in range(0,len(arr)):
#     if arr[i] not in k and i<=n:
#         k.append(arr[i])
        
#     if i>n:
#         break   
    
# print(k)

#0, 1, 1, 2, 3, 5, 8, 13, 21,

# fibonacci=[]
# n=int(input())
# if n==1:
#     fibonacci=[0]
# if n==2:
#     fibonacci=[0,1]
# if n>=3:
#     fibonacci.append(0)
#     fibonacci.append(1)
    
#     for  i in range(2,n+1):
#         s=fibonacci[i-1]+fibonacci[i-2]
        
#         fibonacci.append(s)
# print(fibonacci)

# def fibonacci(n):
#     if n==0:
#         return []
#     elif n==1:
#         return [0]  

#     elif n==2 :
#         return [0,1]   
#     elif n>=3:
#         fib0=[0,1]
#         for i  in range(2,n):
#             s=fib0[i-1]+fib0[i-2]
#             fib0.append(s)
#     return fib0
# n=int(input())
# print(fibonacci(n))

#factorial

# def fact(n):
#     if n<0:
#         return -1
#     if n==0 or n==1:
#         return 1
#     factorial=1
#     for i in range(2,n+1):
#         factorial*=i
#     return factorial    
# n=int(input())    
# print(fact(n))

#sum of digits
# n=12345
# s=0
# while n>0:
#     s+=n%10
#     n=n//10
# print(s)    

#palindrome
#12321
# rev=0
# n=12321
# n1=n
# while n1>0:
#     s=n1%10
#     rev=rev*10+s
#     n1=n1//10

# print(rev==n)    
   

#multiplication table
#5*1=5

# for i in range(5,10):
#     print(f"multiplication table for {i} ")
#     for j in range(1,13):
#         #print(i,"*", j, "=", i*j )
#         print(f"{i} * {j} = {i*j}")
#     print()

#ARMSTRONG NUMBER --> 153  == 1**3 +5**3+3**3 =153 then it is armstrong

# n=int(input())
# n1=n
# n2=n
# digits=0
# arm=0
# while n1>0:
    
#     digits+=1
#     n1=n1//10
# while n2>0:
#     s=n2 %10
#     arm+=s**digits
#     n2=n2//10

# print(arm)
# print(n==arm)


#Gcd
# def gcd(a,b):
#     while b!=0:
#         a,b=b,a%b
#     return a

# def lcm(a,b):
#     return abs((a*b)//gcd(a,b) )   
# a,b=map(int,input().split())

# print(lcm(a,b))      

 