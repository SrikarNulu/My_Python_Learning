#aaaabbbcccdd
# def magic(arr):
#     j=0
#     c=1
#     maxi=1
#     for i in range(1,len(arr)):
#         if arr[i]==arr[j]:
#             c+=1
#             maxi=max(maxi,c)
#         else:
#             c=1    
#     return len(arr)-maxi

# arr=input("enter the string")
# print(magic(arr))


#167 -- 13649
# def en(n):
#     n1=str(n)
#     s=''
#     for i in n1:
#         s+=str(int(i)**2)
#     s1="".join(s)   
#     return int(s1) 

# n=int(input())
# print(en(n))

# def en(n):
#     n1 = list(str(n))  # Convert the number to a string and then to a list of characters
#     s = []
#     for i in n1:
#         s.append(str(int(i) ** 2))  # Convert each character to an integer, square it, then convert back to string
#     s1 = "".join(s)  # Join the list of strings into a single string
#     return int(s1)  # Convert the final string back to an integer

# n = int(input("Enter a number: "))
# print(en(n))
# s='hello'
# d=0
# for i in range(1,len(s)):
#     diff=abs(ord(s[i-1])-ord(s[i]))
    
#     d+=diff
# print(d)

# def defangIPaddr(arr):
#         s=''
#         for i in range(0,len(arr)):
            
#             if arr[i]== '.':
#                 s+='[.]'
#             else :
#                 s+=arr[i]    
#         return s 
# arr='1.1.1.1'           
# print(defangIPaddr(arr))            

#sub_array
# def max_score(n,k,arr):
#     res=-1
#     s=0
#     for i in range(n-k+1):
#         c=1
#         for j in range(i,i+k):
#             s+=c*arr[j]
#             c+=1
#         res=max(res,s)
#         s=0
#     return res
# n=int(input())
# k=int(input())
# arr=list(map(int,input().split()))
# print(max_score(n,k,arr))        

# import oops as o
# a=o.area(6)
# print(a,o.peri(6))

