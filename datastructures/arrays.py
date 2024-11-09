#---------//////--------ARRAYS----------\\\\\-----
# Let us say your expense for every month are listed below,
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190
# Create a list to store these monthly expenses and using that find out,

# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this
# arr=[2200,2350,2600,2130,2190]
# ep=arr[1]-arr[0]
# print(ep)
# s=0
# for i in range(0,len(arr)-2):
#     s+=arr[i]
# print(s)
# for i in range(len(arr)):
#     if i==2000:
#         print(i)
#     else:
#         print(None)    
# arr.insert(5,1980)
# print(arr)

# arr[3]+=200    
# print(arr)  
# 
# 
# You have a list of your favorite marvel super heros.
# heros=['spider man','thor','hulk','iron man','captain america']
# Using this find out,

# 1. Length of the list
# 2. Add 'black panther' at the end of this list
# 3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'
# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)      
# heros=['spider man','thor','hulk','iron man','captain america']
# print(len(heros))
# heros.append("black panther")
# print(heros)
# heros.remove("black panther")
# print(heros)
# heros.insert(3,"black panther")
# #heros.remove("hulk")
# heros[2]="doctor strange"
# print(heros)
# #heros.insert(2,"doctor strange")
# print(sorted(heros))

# Create a list of all odd numbers between 1 and a max number. Max number is
#  something you need to take from a user using input() function
# def odd(num):
#     num1=str(num)  #WORST CODE EVER WRITTEN 
#     l1=[]
#     for i in range(len(num1)):
#         if int(i)%2!=0:
#             l1.append(i)
#     return l1        
# n=int(input())
# odd(n)
# print(n)

# max=int(input())
# l1=[]
# for i in range(max):
#     if i%2!=0:
#         l1.append(i)
# print(l1)




#=======//////////----ARRAYS----\\\\\\\\========

#find largest element
# def maxi(arr):
#     maxi=arr[0]
#     for i in arr:
#         if i>maxi:
#             maxi=i
#     return maxi        
# arr=[1,4,33,45,3,45,78,85,23]  
# print(maxi(arr))         

#second largest element
# def sec(arr):
#     sorted_arr=sorted(arr)
#     l=sorted_arr[-1]
    
#     for i in range(len(arr)-1,0,-1) :
#         if sorted_arr[i]!=l :
#             return sorted_arr[i]
           
# arr=[1]  
# print(sec(arr))    
#----brute force approach-----
# arr=[81,4,33,45,3,45,78,78,78,78,78,85,23]
# arr.sort()
# l=arr[-1]
# sl=None
# for i in range(len(arr)-2,-1,-1):
#     if arr[i]!=l:
#         sl=arr[i]
#         break
# print(sl)  
#
# better approach
# arr=[81,4,33,45,3,45,78,78,78,78,78,85,83] 
# l=arr[0] 
# sl=float('-inf')
# # finding largest element
# for i in arr:
#     if i>l:
#         l=i
# # finding second largest element  
# for j in arr:
#     if j >sl and j!=l:
#         sl=j
# print(sl)     

#optimal approach
# arr=[81,4,33,45,3,45,78,78,78,78,78,85,83]
# maxi=float("-inf")
# sec_maxi=float("-inf")
# mini=float("inf")
# sec_mini=float("inf")
# for i in arr:
#     if i>maxi:
#         sec_maxi=maxi
#         maxi=i
#     elif i>sec_maxi and i!=maxi:
#         sec_maxi=i
#     if i<mini:
#         sec_mini=mini
#         mini=i
#     elif i<sec_mini and i!=mini:
#         sec_mini=i    
# print(maxi,sec_maxi,mini,sec_mini )       

# arr=[1,1,1,2,2,2,2,2,3,3,3,3,3,3,3,3,3,4,4,4]
# a=list(set(arr))

# print(len(a),a)

# def sec_max(arr):
#     if len(arr)<2:
#         return "given arr length is one so cannot find second largest",-1
#     l=float("-inf")
#     sl=float("-inf")
#     for i in range(len(arr)):
#         if arr[i]>l:
#             sl=l
#             l=arr[i]
#         elif arr[i]>sl and arr[i]!=l:
#             sl=arr[i]
#     if sl not in arr:
#             return -1    

#     return sl,arr.index(sl) 
# arr=[42] 
# print(sec_max(arr))   
          

# arr = [1, 1, 2, 2, 2, 3, 3]  # Example sorted array

# # First Pass: Insert elements into the set
# st = set()
# for i in arr:
#     st.add(i)

# # Second Pass: Reassign unique elements back to the array
# index = 0
# for element in st:
#     arr[index] = element
#     index += 1

# # The rest of the array beyond the number of unique elements is not needed
# # We can either slice it off or simply acknowledge that the unique elements
# # are in the first `index` positions of the array.
# unique_arr = arr[:index]

# print(unique_arr)

#rotate thr array one place
# arr=[1,2,3,4,5]
# temp=arr[0]
# for i in range(1,len(arr)):
#     arr[i-1]=arr[i]
# arr[len(arr)-1]=temp
# print(arr)
    

#rotate the array k times
# def s(arr,d):
#     n=len(arr)
#     temp=arr[:d]

#     for i in range(d,n):
#         arr[i-d]=arr[i]  #not yet solved

    
#     for i in range(d):
#         arr[n-d+i]=temp[i]
        
#     return arr
# arr=[1,2,3,4,5,6,7]
# d=3 
# print(s(arr,d))  
#rotate array by one place
# def rotate(arr,d):
#     temp=arr[:d]
#     for i in range(d,len(arr)):
#         arr[i-d]=arr[i]
    
#     for i in range(d,len(arr)):

#         arr.pop()
#         arr.append(temp[0])
#         temp+=1    

# arr=[1,2,3,4,5,6,7]
# d=3 
# rotate(arr,d)       
# print(arr)        

# def rotate(arr):
#     temp=arr[0]
#     for i in range(1,len(arr)):
#         arr[i-1]=arr[i]
#     arr[len(arr)-1]=temp 
#     return arr
# arr=list(map(int,input().split()))
# print(rotate(arr)) 
       
#rotate a string and substring is present or not
# def ss(s):
      
#     d=s+s
#     if s in d:
#         return True
#     return False    
        
# s="abcde"
# goal="cdeab"
# print(ss(s))

#[1,2,3,4,5,6,7] and k=3 -->[5,6,7,1,2,3,4] 
# def right(arr, k):
#     size = len(arr)
#     k = k % size       # To handle cases where k is larger than the size of the array
#     return arr[-k:] + arr[:-k]
# arr = [1, 2, 3, 4, 5, 6, 7]
# k = 6
# rotated_arr = right(arr, k)
# print(rotated_arr)


# #RIGHT ROTATION OPTIMAL APPROACH
# def rotate(nums, k):
#     def rev(l, r):
#         while l < r:
#             nums[l], nums[r] = nums[r], nums[l]
#             l +=1
#             r -=1
#     rev(0, len(nums) - 1)
#     rev(0, k-1)
#     rev(k, len(nums)-1)
#     return nums      
# arr=[1,2,3,4,5,6,7]
# k=3
# print(rotate(arr,k))

#brute_force:
#arr=[0,1,0,0,0,3,12,0,0]
# temp=[]
# for i in range(len(arr)):
#     if arr[i]!=0:
#         temp.append(arr[i])
# for i in range(len(temp))   :
#     arr[i]=temp[i] 
# for i in range(len(temp),len(arr)):
#     arr[i]=0
#optimal_solution
# j=0
# for i in range(1,len(arr)):
    
#     if arr[i]!=0:
#         arr[i],arr[j]=arr[j],arr[i]
#         j+=1    
# print(arr)    

# a=[1,1,2,3,4,5,6,7]
# b=[1,3,5,8,9]
# # c=set()
# # for i in range(len(a)):
# #     c.add(a[i])
# # for i in range(len(b)):
# #     c.add(b[i])    
# # c=list(c)
# # print(c)
# c=set()
# for i in range(len(a)):
#     for j in range(len(b)):
#         if a[i]==b[j]:
#             c.add(a[i])
# d=list(c)            
# print(d)   


#UNION
# a=[1,1,2,3,4,5,6,7]
# b=[1,3,5,8,9]
# i=j=0
# union=[]
# while i<len(a) and j<len(b):
#     if a[i]<b[j]:
#         if len(union)==0 or union[-1]!=a[i]:
#             union.append(a[i])
#         i+=1
#     elif a[i]>b[j]:
#         if len(union)==0 or union[-1]!=a[i]:
#             union.append(a[i])
#         i+=1
#     else:
#         if len(union)==0 or union[-1]!=b[j]:
#             union.append(b[j]) 
#         j+=1
#         i+=1
# while i<len(a):
#     if len(union)==0 or union[-1]!=a[i]:
#             union.append(a[i])
#     i+=1 
# while j<len(b):
#     if len(union)==0 or union[-1]!=b[j]:
#             union.append(b[j])
#     j+=1
# print(union)            

#intersection
# a=[1,1,2,3,4,5,6,7]
# b=[1,3,5,8,9]
# i=j=0
# intersection=[]
# while i<len(a) and j<len(b):
#     if a[i]<b[j]:
#         i+=1
#     elif a[i]>b[j]:
#         j+=1
#     else:
#         if len(intersection)==0 or intersection[-1]!=a[i]:
#             intersection.append(a[i])
#         i+=1
#         j+=1
# print(intersection)     
# 
# 
# FINDING MISSING NUMBER
# arr=[0,1,2,4,5]
# arr1=sorted(arr)
# n=len(arr)
# s=[]
# for i in range(0,n):
#     s.append(i)
# i=j=0
# while i<len(arr1):

#     if arr1[i]!=s[j]:
#         print(s[j])
#     i+=1
#     j+=1    
# for i in range(1,len(arr)):
#     flag=0
#     for j in range(0,len(arr)-1):
#         if arr[j]==i:
#             flag=1
#             break
#     flag=0        
        
#max occurrence of a number
# arr=[1,1,0,1,0,0,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1]
# maxi=0
# c=0
# for i in range(0,len(arr)):
#     if arr[i]==1:
#         c+=1
#         maxi=max(maxi,c)
#     else:
#         c=0
# print(maxi)            
# maxi=0
# count=0
# for i in range(0,len(nums)):
#     if nums[i]==1:
#         count+=1
#         maxi=max(maxi,count)
#     else:
#         c=0
#     return maxi

#LONGEST SUB_ARRAY WITH GIVEN SUM k (positives)

#1) BRUTE FORCE

# def sub_array(arr,k):
#     n=len(arr)
#     length=0
#     for i in range(0,n):
#         for j in range(i,n):
#             s=0
#             for idx in range(i,j+1):
#                 s+=arr[idx]
#             if s==k:
#                 length=max(length,j-i+1)
#     return length
# arr=list(map(int,input().split()))
# k=3
# print(sub_array(arr,k))                   

#2) optimization of brute
# def sub_array(arr,k):
#     n=len(arr)
#     length=0
#     for i in range(0,n):
#         s=0
#         for j in range(i,n):
#             s+=arr[j]
#             if s==k:
#                 length=max(length,j-i+1)
#     return length
# arr=list(map(int,input().split()))
# k=3
# print(sub_array(arr,k)) 

#3)using two pointers
# def sub_array(arr,k):
#     n=len(arr)
#     left=0
#     right=0
#     sum=arr[0]
#     maxlen=0
#     while right<n:
#         while left<=right and sum>k:
#             sum-=arr[left]
#             left+=1
#         if sum==k:
#             maxlen=max(maxlen,right-left+1)
#         right+=1
#         if right<n:
#             sum+=arr[right] 
#     return maxlen           
# arr=[2,3,5,1,9]  
# k=10
# print(sub_array(arr,k))             



#right rotate
# def rightRotate(arr):
#     n=len(arr)
#     temp=arr[n-1]
#     for  i in range(n-2,-1,-1):
#         arr[i+1]=arr[i]
        

#     arr[0]=temp
#     return arr
# arr=[1,2,3,4,5,6]
# print(rightRotate(arr))        


# def left(arr,k):
#     n=len(arr)
#     k=k % n
#     return arr[k:]+arr[:k]
# arr=[1,2,3,4,5,6,7]
# k=3
# print(left(arr,k))    


# def right(arr,k):
#     n=len(arr)
#     k=k % n
#     return arr[-k:]+arr[:-k]
# arr=[1,2,3,4,5,6,7]
# k=3
# print(right(arr,k))    


#longest sub_array
# def sub_array(arr,k):
#     n=len(arr)
#     length=0
#     for i in range(0,n):
#         s=0
#         for j in range(i,n):
#             s+=arr[j]
#             if s==k:
#                 length=max(length,j-i+1)
#     return length

# arr=[1,2,3,1,1,1,1,4,5,6,1,1]
# k=27
# print(sub_array(arr,k)) 

#medium q1
#two sum(brute)
# def twoSum(arr,t):
#    
#     for i in range(0,len(arr)):
#         for j in range(i+1,len(arr)):
#             if arr[i]+arr[j]==t:
#                 s=i,j
#     return list(s)
#     # else:       
#     #     return -1              
# arr=[0,1,2,3,4,5]
# t=5
# print(twoSum(arr,t))

#better/optimal
# def twoSum(arr,t):
     
#      l=0
#      r=len(arr)-1
#      while l<r:
#         s=arr[l]+arr[r]
#         if s==t:
#             return True
#         elif s<t:
#             l+=1
#         else:
#             r-=1
#      return False  

# arr=[9,1,0,3,4,6,8]
# t=5
# print(twoSum(arr,t))


#MEDIUM Q2
#brute- sorting(merge sort (o(nlogn)))
#better
# arr=[0,1,2,1,0,2]
# n=len(arr)
# c0=0
# c1=0
# c2=0
# for i in range(0,n):
#     if arr[i]==0:
#         c0+=1
#     elif arr[i]==1:
#         c1+=1
#     else:
#         c2+=1
# for i in range(c0):
#     arr[i]=0
# for j in range(c0,c0+c1):
#     arr[j]=1
# for k in range(c0+c1,len(arr)):
#     arr[k]=2
# print(arr)        

# DUTCH NATIONAL FLAG ALGORITHM
# def dnf(arr):
#     n=len(arr)
#     low=0
#     mid=0
#     high=n-1

#     while mid<=high:
#         if arr[mid]==0:
#             arr[mid],arr[low]=arr[low],arr[mid]
#             low+=1
#             mid+=1
#         elif arr[mid]==1:
#             mid+=1
#         else:
#             arr[mid],arr[high]=arr[high],arr[mid]
#             high-=1
#     return arr
# arr=list(map(int,input().split()))
# print(dnf(arr))            


#majority element >n/2
# arr=[2,3,2,3,2,3,3,3,3,]
# n=len(arr)
# for i in range(0,n):
#     c=0
#     for j in range(0,n):
#         if arr[i]==arr[j]:
#             c+=1
#     if c>n/2:
#         print(arr[i],c)
#         break
# else:
#     print(-1)
      






#k places
# arr=[1,2,3,4,5,6,7]
# k=3
# print(arr[k:]+arr[:k])

# print(arr[-k:]+arr[:-k])

#q18 kadane's algorithm
#brute
# arr=[-2,-3,4,-1,-2,1,5,-3]
# maxi=float('-inf')
# for i in range(0,len(arr)):
    
#     for j in range(i,len(arr)):
#         s=0
#         for k in range(i,j+1):
#             s+=arr[k]
#         maxi=max(maxi,s)
# print(maxi)

#better
# arr=[-2,-3,4,-1,-2,1,5,-3]
# maxi=float('-inf')
# for i in range(0,len(arr)):
#     s=0
#     for j in range(i,len(arr)):
#         s+=arr[j]
#         maxi=max(maxi,s)
# print(maxi)    

# optimal kadane's algorithm

# arr=[-2,-3,4,-1,-2,1,5,-3]
# maxi=float('-inf')
# sums=0
# start=-1
# end=-1
# for i in range(0,len(arr)):
     
#      sums +=arr[i]
#      if sums>maxi:
#         maxi=sums

#      if sums<0:
#         sums=0
# if maxi<0:
#     maxi=0       
# print(maxi)   
        
#IF WE WANT TO PRINT THE SUB ARRAY
# arr = [-2, -3, 4, -1, -2, 1, 5, -3]

# Initialize variables
# maxi = float('-inf')  # This will store the maximum subarray sum
# sums = 0              # This will store the current subarray sum
# start = 0             # Start index of the maximum subarray
# end = 0               # End index of the maximum subarray
# temp_start = 0        # Temporary start index to mark the beginning of a potential subarray

# for i in range(len(arr)):
#     sums += arr[i]

#     if sums > maxi:
#         maxi = sums
#         start = temp_start
#         end = i

#     if sums < 0:
#         sums = 0
#         temp_start = i + 1

# # Handle case where all numbers are negative
# if maxi < 0:
#     maxi = 0

# print("maxi is:",maxi, "And sub array is: ",arr[start:end+1])

#strivers kadane's algorithm
# import sys

# def maxSubArraySum(arr, n):
#     maxi = -sys.maxsize - 1  # maximum sum
#     sum = 0

#     start = 0
#     ansStart, ansEnd = -1, -1
#     for i in range(n):

#         if sum == 0:
#             start = i  # starting index

#         sum += arr[i]

#         if sum > maxi:
#             maxi = sum

#             ansStart = start
#             ansEnd = i

#         # If sum < 0: discard the sum calculated
#         if sum < 0:
#             sum = 0

#     # printing the subarray:
#     print("The subarray is: [", end="")
#     for i in range(ansStart, ansEnd + 1):
#         print(arr[i], end=" ")
#     print("]")

#     # To consider the sum of the empty subarray
#     # uncomment the following check:

#     # if maxi < 0:
#     #     maxi = 0

#     return maxi

# arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# n = len(arr)
# maxSum = maxSubArraySum(arr, n)
# print("The maximum subarray sum is:", maxSum)


#rearrange the elements by sign ex: [1,-2,4,5,6,-3,-2] ----to----[1,-2,4,-3,5,-2,6]
# arr=[3,1,-2,-5,2,-4,6,8,9]
# pos=[]
# neg=[]
# res=[]
# for i in range(0,len(arr)):
#     if arr[i]>0:
#         pos.append(arr[i])
#     else:
#         neg.append(arr[i])    
   
# for i in range(max(len(pos),len(neg))):
#     if i<len(pos):
#         res.append(pos[i])
#     if i<len(neg):     
#         res.append(neg[i])
# print(res)


#22)leaders 

# arr=[10,22,12,0,3,6]
# s=[]

# for i in range(len(arr)):
#     flag=True
#     for j in range(i+1,len(arr)):
#         if arr[j]>arr[i]:
#             flag=False
#             break
#     if flag: # if flag == True: 
#          s.append(arr[i])
# print(s)

# arr=[10,22,12,0,3,6]
# s=[]
# maxi=float("-inf")
# for i in range(len(arr)-1,-1,-1):

#     if arr[i]>maxi:
#         s.append(arr[i])
#         maxi=max(maxi,arr[i])
# s.reverse()
# print(s)        


#arr=[1,1,2,2,3,2,1,2,3,4,5,6,7,101,102,101,102,101,102,103,104,105,106,107,108]
# arr=[100,4,200,1,3,2]

# s=set(arr)
# arr1=sorted(s)
# s2=list(arr1)
# c=1
# maxi=0
# for i in range(1,len(s2)):
#     if s2[i]-s2[i-1]==1:
#         c+=1
#         maxi=max(maxi,c)
#     else:
#         c=1
# print(s2)        
# print(maxi)        

    
        # arr2=set(arr1)
        # arr=list(arr2)

        # count=1
        # maxi=0
        # for i in range(1,len(arr)):
        #     if arr[i]-arr[i-1]==1:
        #         count+=1
        #         maxi=max(maxi,count) 
                
        #     else:
        #         count=1
                   
        # return maxi   



# t=int(input())
# for i in range(t):
#         n=int(input())
#         s=0
#         while n>0:
#                 s+=n%10
#                 n=n//10
#         print(s)            


# w=int(input())
# res=w//2
# if w%2==0 and res!= 1:
#         print("Yes")
# else:
#         print("no") 
# 

# t=int(input())
# for i in range(t):
#         mini=float('inf')
#         a,b=map(int,input().split())
#         if a>=b :
#             mini=0
#         else:        
#             for i in range(a,b):
#                 if a<=i and i<=b:
#                     s=i-a + b-i
#                 mini=min(s,mini) 
#         print(mini)

# n=int(input())
# arr=list(map(int,input().split()))
# res={}
# for i in arr:
#     if i in res:
#         res[i]+=1
#     else:
#         res[i]=1 
# result=max(res.values())

# c=0
# for i,j in :
#     if result==i:
#         c+=1
# print(c) 
     

n=int(input())
if n<1:
    print(0)
elif n==1:
    print(1)    
else:
    fib=[1,1]
    for i in range(2,n):
        res=fib[-1]+fib[-2]
        fib.append(res)
    print(sum(fib))    
    
n=int(input())
if n<1:
    print(0)
elif n==1:
    print(1)
else:
    fib=[1,1]
    for i in range(2,n):
        res=fib[-1]+fib[-2]
        fib.append(res)
    print(sum(fib))    
    









