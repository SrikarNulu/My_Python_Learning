#--------//////----SORTING ALGORITHMS----\\\\\-----
# 
# selection sort
# def selection_sort(arr):
#     for i in range(0,len(arr)):
#         mini=i
#         for j in range(i+1,len(arr)):
#             if arr[j]<arr[mini]:
#                 mini=j
#         arr[mini],arr[i]=arr[i],arr[mini]  
#     return arr           
# arr=list(map(int,input().split())) 
# print(selection_sort(arr)) 



# def selection_sort(arr, n):
#     for i in range(n):
#         min_val = arr[i]
#         min_idx = i
#         for j in range(i + 1, n):
#             if arr[min_idx] > arr[j]:
#                 min_val = arr[j]
#                 min_idx = j
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]

# if __name__ == "__main__":
#     n = int(input())

#     arr = [int(x) for x in input().split()]

#     selection_sort(arr, n)

#     for i in range(n):
#         print(arr[i], end=" ")

#     print()


#bubble sort
# def bubble_sort(arr):
#     n=len(arr)
#     for i in range(0,n-1):
#         for j in range(n-i-1):
#             if arr[j]>arr[j+1]:
#                 arr[j],arr[j+1]=arr[j+1],arr[j] 
#     return arr            
# arr=list(map(int,input().split()))
# print(bubble_sort(arr))   

#insertion sort
# def insertion_sort(arr):
#     n=len(arr)
#     for i in range(1,n):
#         key=arr[i]
#         j=i-1
#         while j>=0 and key<arr[j]:
#             arr[j+1]=arr[j]
#             j-=1
#         arr[j+1]=key
#     return arr
# arr=list(map(int,input().split()))
# print(insertion_sort(arr))
# 
# def insertion_sort(arr):
#     n=len(arr)
#     for i in range(1,n):
#         j=i
#         while j>0 and arr[j-1]>arr[j]:
#             arr[j],arr[j-1]=arr[j-1],arr[j]
#             j-=1
#     return arr
# arr=list(map(int,input().split()))
# print(insertion_sort(arr))  

# def insertion_sort(arr):
#     n=len(arr)
#     for i in range(1,n):
#         j=i
#         while j>0 and arr[j]<arr[j-1]:
#             arr[j-1],arr[j]=arr[j],arr[j-1]
#             j-=1
#     return arr
# arr=list(map(int,input().split()))
# print(insertion_sort(arr))             

#merge sort

# def merge(left,right):
#     merged=[]
#     i=0
#     j=0
#     while i<len(left) and j<len(right):
#         if left[i]<=right[j]:
#             merged.append(left[i])
            
#             print("length of left is: ",len(left))
#             print("length of i is: ",i)
#             i+=1
#         else:
#             merged.append(right[j])
            
#             print("length of right is: ",len(right))
#             j+=1
#     merged+=left[i:]+right[j:] 
#     return merged           

# def merge_sort(arr):
#     if len(arr)<=1:
#         return arr
#     mid=len(arr)//2
#     left=merge_sort(arr[:mid])
#     right=merge_sort(arr[mid:])
#     return merge(left,right) 
# arr1=eval(input())
# print(merge_sort(arr1))


# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     # Divide the array into two halves
#     mid = len(arr) // 2
#     left_half = merge_sort(arr[:mid])
#     right_half = merge_sort(arr[mid:])

#     # Merge the two sorted halves
#     return merge(left_half, right_half)

# def merge(left, right):
#     result = []
#     i = j = 0

#     # Compare each element and merge them in order
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1

#     # Append the remaining elements
#     result.extend(left[i:])
#     result.extend(right[j:])
    
#     return result

# # Example usage
# arr = [38, 27, 43, 3, 9, 82, 10]
# sorted_arr = merge_sort(arr)
# print(sorted_arr)


# def merge_sort(arr):
#     if len(arr)<=1:
#         return arr
#     mid=len(arr)//2
#     left=arr[:mid]
#     right=arr[mid:] 
#     left=merge_sort(left) 
#     right=merge_sort(right)
#     return merge_sorted_lists(left,right)

# def merge_sorted_lists(a,b):
#     len_a=(len(a))
#     len_b=(len(b))
#     i=j=0
#     res=[]
#     while i<len_a and j<len_b :
#         if a[i]<=b[j]:
#             res.append(a[i])
#             i+=1
#         else:
#             res.append(b[j])
#             j+=1
#     while i<len_a:
#         res.append(a[i])
#         i+=1
#     while j<len_b:
#         res.append(b[j]) 
#         j+=1 
#     return res
# arr1=list(map(int,input().split(",")))
# print(merge_sort(arr1))           



# def merge_sort(arr):
#     if len(arr) <= 1:
#         return

#     mid = len(arr)//2

#     left = arr[:mid]
#     right = arr[mid:]

#     merge_sort(left)
#     merge_sort(right)

#     merge_two_sorted_lists(left, right, arr)

# def merge_two_sorted_lists(a,b,arr):
#     len_a = len(a)
#     len_b = len(b)

#     i = j = k = 0

#     while i < len_a and j < len_b:
#         if a[i] <= b[j]:
#             arr[k] = a[i]
#             i+=1
#         else:
#             arr[k] = b[j]
#             j+=1
#         k+=1

#     while i < len_a:
#         arr[k] = a[i]
#         i+=1
#         k+=1

#     while j < len_b:
#         arr[k] = b[j]
#         j+=1
#         k+=1

# if __name__ == '__main__':
#     test_cases = [
#         [10, 3, 15, 7, 8, 23, 98, 29],
#         [],
#         [3],
#         [9,8,7,2],
#         [1,2,3,4,5]
#     ]

#     for arr in test_cases:
#         merge_sort(arr)
#         print(arr)

# def merge_sort(arr):
#     if len(arr)<=1:
#         return 
#     mid=len(arr)//2
#     left=arr[:mid]
#     right=arr[mid:]
#     merge_sort(left)
#     merge_sort(right)
    
#     # left=merge_sort(arr[:mid])
#     # right=merge_sort(arr[mid:]) 
#     i=j=k=0
#     while i<len(left) and j<len(right) :
#         if left[i]<=right[j]:
#             arr[k]=left[i]
#             i+=1
#         else:
#             arr[k]=right[j]
#             j+=1
#         k+=1
#     while i<len(left):
#         arr[k]=left[i]
#         i+=1
#         k+=1
#     while j<len(right) :
#         arr[k]=right[j]
#         j+=1
#         k+=1

# arr1=list(map(int,input().split()))
# merge_sort(arr1)
# print(arr1)                       


#quick sort
# def quick_sort(arr):
#     length=len(arr)
#     if length<=1:
#         return arr
#     else:
#         pivot=arr.pop() #LAST ELEMENT IS PIVOT AND POP RETURNS LAST ELEMENT
#         elements_greater=[]
#         elements_lower=[]
#         for i in arr:
#             if i>pivot:
#                 elements_greater.append(i)
#             else:
#                 elements_lower.append(i)
#         return  quick_sort(elements_lower)+[pivot]+quick_sort(elements_greater)
# arr1=list(map(int,input().split()))
# print(quick_sort(arr1))                   



#selection sort
# def selection(arr):
#     for i in range(0,len(arr)):
#         mini=i
#         for j in range(i+1,len(arr)):

#            if arr[j]<arr[mini]:
#                mini=j
#         arr[i],arr[mini]=arr[mini],arr[i]
#     return arr    
# arr=[1,3,6,2,4,8,7]
# print(selection(arr))     
# 
# Bubble sort
# def bubble(arr):
#     for i in range(0,len(arr)-1):
        
#         for j in range(len(arr)-1-i):

#            if arr[j]>arr[j+1]:
             
#                arr[j],arr[j+1]=arr[j+1],arr[j]
#     return arr    
# arr=[1,3,6,2,4,8,7]
# print(bubble(arr))    
# 
#insertion sort
# def insertion(arr):
#     for i in range(1,len(arr)):
#         j=i
#         while j >0 and arr[j]<arr[j-1]:
#             arr[j],arr[j-1]=arr[j-1],arr[j]
#             j-=1
#     return arr    
# arr=[1,3,6,2,4,8,7]
# print(insertion(arr))       

#merge sort
# def merge(arr):
#     if len(arr)<=1:
#         return arr
       
#     mid=len(arr)//2
#     l=arr[:mid]
#     r=arr[mid:]
#     merge(l)
#     merge(r)
#     i=j=k=0
#     while i<len(l) and j<len(r):
#         if l[i]<r[j]:
#             arr[k]=l[i]
#             i+=1
#         else:
#             arr[k]=r[j]
#             j+=1
#         k+=1    
#     while i<len(l):
#         arr[k]=l[i]
#         i+=1
#         k+=1
#     while j<len(r):
#         arr[k]=r[j]
#         j+=1
#         k+=1    

#     return arr
    
        
# arr=[7,4,2,1,3,8,9,7,4,3,2,7,8]
# print(merge(arr)) 

#merge sort using extra list 

# def merge_sort(arr):
#     if len (arr)<=1:
#         return arr
#     mid=len(arr)//2
#     l=merge_sort(arr[:mid])
#     r=merge_sort(arr[mid:]) 
#     return merge(l,r)
# def merge(l,r):
#     i=j=0
#     result=[]
#     while i<len(l) and j<len(r):
#         if l[i]<r[j]:
#             result.append(l[i])
#             i+=1 
#         else:
#             result.append(r[j])
#             j+=1
#     while i<len(l):
#         result.append(l[i])
#         i+=1
#     while j<len(r):
#         result.append(r[j])
#         j+=1     
#     return result
# arr=list(map(int,input().split())) 
# print(merge_sort(arr))   

#using extend function -MERGE SORT
# def merge_sort(arr):
#     if len (arr)<=1:
#         return arr
#     mid=len(arr)//2
#     l=merge_sort(arr[:mid])
#     r=merge_sort(arr[mid:]) 
#     return merge(l,r)
# def merge(l,r):
#     i=j=0
#     result=[]
#     while i<len(l) and j<len(r):
#         if l[i]<r[j]:
#             result.append(l[i])
#             i+=1 
#         else:
#             result.append(r[j])
#             j+=1
     
#     result.extend(l[i:]) 
#     result.extend(r[j:])  
#     return result
# arr=list(map(int,input().split())) 
# print(merge_sort(arr))

# def ss(a,b):
#     n=len(a)
#     n1=len(b)
#     s=0
#     for i in range(0,n):
#         for j in range(i,n1):
#             if a[i]>=b[j]:
#                 s+=a[i]-b[j]
#                 break
#             else:
#                 s+= a[i]-b[j] 
#                 break 
#     return abs(s)

# a=[12,14,19,19,12]

# b=[19,2,17,20,7]
# print(ss(a,b))                   