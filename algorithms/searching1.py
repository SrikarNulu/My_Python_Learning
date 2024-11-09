
#====///////------SEARCHING ALGORITHMS------//////====
# def binary_search(arr,target):
#     if len(arr)<=1:
#         return arr
#     left=0
#     right=len(arr)-1
#     while left<=right:
#         midpoint=(left +right)//2
#         mid_value=arr[midpoint]
#         if target==mid_value:
#             return midpoint
#         elif target<mid_value:
#             right=midpoint-1
#         else:
#             left=midpoint+1
#     return -1
# arr_1=list(map(int,input("enter the array of elements: ").split()))
# target=int(input("enter the target: "))
# print(binary_search(arr_1,target))                 

# def binary_search_recursive(numbers_list, number_to_find, left_index, right_index):
#     if right_index < left_index:
#         return -1

#     mid_index = (left_index + right_index) // 2
#     # if mid_index >= len(numbers_list) or mid_index < 0:
#     #     return -1

#     mid_number = numbers_list[mid_index]

#     if mid_number == number_to_find:
#         return mid_index

#     if mid_number < number_to_find:
#         left_index = mid_index + 1
#     else:
#         right_index = mid_index - 1

#     return binary_search_recursive(numbers_list, number_to_find, left_index, right_index)
# numbers_list=list(map(int,input("enter the array of elements: ").split())) 
# number_to_find=int(input("enter the target element: "))
# index = binary_search_recursive(numbers_list, number_to_find, 0, len(numbers_list)-1)
# print(f"Number found at index {index} using binary search")    
           

# def search( nums, target):
        
#         left_index=0
#         right_index=len(nums)-1
#         while left_index<=right_index:
#             mid_index=(left_index+right_index)//2
#             mid_value=nums[mid_index]
#             if target==mid_value:
#                 return mid_index
#             elif target<mid_value:
#                 right_index=mid_index-1
#             else:
#                 left_index=mid_index+1
#         return -1            
# arr=list(map(int,input().split()))
# target=int(input())
# print(search(arr,target))

# class Solution(object):
#     def search(self, nums, target):
        
        
#         def binary_search(left, right):
#             if left > right:
#                 return -1
            
#             mid = (left + right) // 2
            
#             if nums[mid] == target:
#                 return mid
#             elif nums[mid] < target:
#                 return binary_search(mid + 1, right)
#             else:
#                 return binary_search(left, mid - 1)
#         return binary_search(0, len(nums) - 1)            
# solution = Solution()
# arr = list(map(int,input("enter the required array: ").split()))
# target = int(input("enter required target: "))
# result = solution.search(arr, target)
# print("Element found at index:", result) 

def binary_search(arr,t):
    l=0
    r=len(arr)-1
    while l<=r:
        mid=(l+r)//2
        if arr[mid]==t:
            return mid
        elif arr[mid]<t:
            l=mid+1
        else:
            r=mid-1
    return -1   
arr=list(map(int,input().split()))
t=int(input()) 
print(binary_search(arr,t))                
