# 1)BASKET BALL SUM k=2, 1 based indexing
# def sub_array(n,arr,k):
    
#     maxi=0
#     for  i in range(n-k+1):
#         s=arr[i:i+k]
        
#         sums=0
#         for idx in range(1,k+1):
#             sums+=idx*s[idx-1]
#         maxi=max(maxi,sums)
        
#     return maxi
# n=int(input())
# arr=list(map(int,input().split()))
# k=int(input())
# print(sub_array(n,arr,k))    


# 2)chocolates sum

# n=3
# arr=[10,20,30]
# s=0
# for i in range(len(arr)):
#     s+=arr[i]//3
#     if arr[i]%3!=0:
#         s+=1
# print(s)


# 3)diwali sum      
# n=int(input())
# p=int(input())
# time_rem=240-p
# count=0
# for i in range(1,n+1):
#     solve=i*5
#     if solve<time_rem and time_rem>0:
        
#         count+=1
#         time_rem-=solve
#         print(time_rem,count)
#     else:
#         break    
# print(count) 

       

# 4)dog sum
# n=int(input())
# print(n*7)


# 5)ant and rail sum
# n=int(input())
# arr=list(map(int,input().split()))
# c=0
# s=0
# for i in arr:
#     s+=i
#     if s==0:
#         c+=1
# print(c)   


#6) most repeating vowel in the given string
# s = input()
# d = {
#     'a': 0,"e": 0,"i": 0,"o": 0,"u": 0
# }
# for i in s:
#     if i in "aeiou":
#         d[i] += 1
# ans, maxValue = '',0
# for key, value in list(d.items()):
#     if value > maxValue:
#         ans = key
#         maxValue = value
# print(ans)      


#7)occurrence of a 
# n=input()
# s=n.count(" ")
# print(s)

#8)
#9)

#10)next prime

# def prime(n):
#     if n==0 or n==1:
#         return False
#     else:
#         for i in range(2,(n//2)+1) :
#             if n%i==0:
#                 return False
#         return True
# num=int(input())
# next_num=num+1
# while True:
#     if prime(next_num):
#         print(next_num)
#         break
#     next_num+=1   




#41)
# arr=[1,2,3,4,5]
# arr2=[]

# for i in range(len(arr)):
#     left=sum(arr[:i+1])
#     right=sum(arr[i+1:])
#     res=abs(left-right)
#     arr2.append(res)
# print(arr2)  

# arr=[1,2,3,4,5]
# arr2=[]
# total=sum(arr)
# left=0
# right=0
# for i in range(len(arr)):
#     left+=arr[i]
#     right=total-left
#     res=abs(left-right)
#     print(left,right,res)
#     arr2.append(res)
# print(arr2)

a,b,c=map(int,input().split())

res=[a,b,c]
while a>0:
    rem=a-b
    if rem not in res:
        res.append(rem)
    
    a=rem
print(len(res)-1)    



    










