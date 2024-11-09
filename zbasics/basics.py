#2**2-1**1, 3**3-2**2 .....=!
# def empty_square_sequence(n):
#     s=[]
#     for i in range(2,n+2):
#         m=((i**2)-((i-1)**2))
#         s.append(m)
#     return s    
# n=5
# print(empty_square_sequence(n))


# def collatz_conjecture(n):
#     m=[]
#     while n>1:
#         m.append(n)
#         if n%2==0:
#             n=n/2
#             m.append(n)
         
#         else:
#             n=n*3+1
#             m.append(n)
#     return m     
# n=6
# print(collatz_conjecture(n))
      

# def count_digits(n):
    
#     s=str(n)
#     y=list(s)

#     even =0
#     odd=0
#     for i in y:
#         if int(i)%2==0:
#             even+=1
#         else:
#             odd+=1
#     z=even,odd
#     return tuple(z)        
# n=1234567890

# print(count_digits(n)) 

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

# def to_spongecase(text):
#     y=text.replace(" ","")
#     z=y
#     print(y)
#     s=len(z)
#     m=''
    
#     for i in range(s):
       
#             if i%2==0:
                
#                 m+=z[i]
#             else:
#                 m+=z[i].upper()    
#     return m        
# text='learn to code'

#**** print(to_spongecase(text))
# def to_spongecase(text):
#     res=""
#     is_upper=False
#     for i in text:
#         if i.isalpha():
#             if is_upper==True:
#                 res+=i.upper()
#             else:
#                 res+=i.lower()
#             is_upper=not is_upper 
#         else:
#             res+=i
#     return res                   
# input_text = input()
# print(to_spongecase(input_text)) 

# def ss(arr):
#     c=0
#     for i in range(len(arr)):
#         mini=i
#         for j in range(i+1,len(arr)):
#             if arr[j]<arr[mini]:
#                 mini=j
#                 print(arr[i],arr[mini])
#         arr[i],arr[mini]=arr[mini],arr[i]
#         c+=1
#     print(c)       
#     return arr
# arry=[13,44,24,52,20,9] 
# print(ss(arry)) 

# def bs(arr):
#     n=len(arr)
#     for i in range(0,n-1):
#         for j in range(n-i-1):
#             if arr[j]>arr[j+1]:
#                 arr[j],arr[j+1]=arr[j+1],arr[j]
#     return arr
# arr1=[4,5,3,2,7]    
# print(bs(arr1))

# def mask_credit_card(card_number):
#     c=list(card)
#     n=len(c)
#     n2=c[-1:-4]
#     l1=[]
#     for i in range(n-4):
#         l1.append('*')
#     newlist=n2+l1
#     return newlist
# card=int(input("enter: "))
# print(mask_credit_card(card))

# def mask_credit_card(card_number):
#     # Convert the number to a string
#     c = str(card_number)
#     n = len(c)
    
#     # Get the last 4 digits
#     n2 = c[-4:]
    
#     # Create a list of '*' for the remaining digits
#     l1 = ['*'] * (n - 4)
    
#     # Combine the '*' and last 4 digits
#     newlist = l1 + list(n2)
    
    
#     masked_card = ''.join(newlist)
    
#     return masked_card

# card =444444441234
# print(mask_credit_card(card)) 
 

#n='welcome to geeks' 
# n1=list(n)
# alpha=[]
# y=[]
# for i in range(97,123):
#     alpha.append(chr(i))



# for i in range(0,len(n1)):
#     if n1[i] in alpha and n1[i] not in y:
#         y.append(n1[i])
#         alpha.remove(n1[i])
# s="".join(alpha)
# print(s)        


#DICTIONARY
# keys=[1,2,3,4,5]
# values=[1,4,9,16,25]
# data=dict(zip(values,keys))
# # data[3]=12
# del data[2]
# data[3]=9
# print(data)

# for i,j in data.items():
#     print(i,j)

# prog={'js':'atom','c#':'vs','python':['pycharm','sublime'],'java':{'jse':'netBeans','jee':'eclipse'}}

# prog.update({'java':{'jse':'pe_da','jee':'r'}  ,'js':'vs','c#':'atom',2:4,'python':[1,2,5,6,'ji','king']})
# print(prog['java']['jee'],prog['java']['jse'])

  


# print(len(prog))
# print(prog.items())
#keys,values,items,len,pop,get,dict,copy



#ENCODED THREE STRINGS

# class Result:
#     def __init__(self, output1, output2, output3):
#         self.output1 = output1
#         self.output2 = output2
#         self.output3 = output3

# class UserMainCode:
#     def slice_string(self, s):
#         l = len(s)
#         if l % 3 == 0:
#             front = s[:l // 3]
#             mid = s[l // 3:2 * (l // 3)]
#             end = s[2 * (l // 3):]
#         elif l % 3 == 1:
#             front = s[:l // 3]
#             mid = s[l // 3:2 * (l // 3) + 1]
#             end = s[2 * (l // 3) + 1:]
#         else:
#             front = s[:l // 3 + 1]
#             mid = s[l // 3 + 1:2 * (l // 3) + 1]
#             end = s[2 * (l // 3) + 1:]
#         return front, mid, end

#     def encodeThreeStrings(self, input1, input2, input3):
#         # Slice the strings
#         front1, mid1, end1 = self.slice_string(input1)
#         front2, mid2, end2 = self.slice_string(input2)
#         front3, mid3, end3 = self.slice_string(input3)

#         # Concatenate parts to form output strings
#         output1 = front1 + front2 + front3
#         output2 = mid1 + mid2 + mid3
#         output3 = end1 + end2 + end3

#         # Toggle the case of output3
#         output3 = output3.swapcase()

#         # Create and return the Result object
#         return Result(output1, output2, output3)

# # Take inputs from the user
# input1 = input("Enter the first string: ")
# input2 = input("Enter the second string: ")
# input3 = input("Enter the third string: ")

# # Process the inputs
# user_code = UserMainCode()
# result = user_code.encodeThreeStrings(input1, input2, input3)

# # Print the final results
# print("Output1:", result.output1)
# print("Output2:", result.output2)
# print("Output3:", result.output3)


# class square:
#     def __init__(self,l,b):
#         self.length=l
#         self.breadth=b
#     def area(self):
#         area=self.length*self.breadth 
#         return f"area of {self.length} and {self.breadth} is {area}" 
#     def perimeter(self):

#         peri=2*(self.length+self.breadth)

#         return f"perimeter of {self.length} and {self.breadth} is {peri}"    

# def main():
#     t=int(input("enter no of test cases:"))
#     c=1
#     while t>0:

#         print(f"current test case: {c}")
#         l=int(input("enter the length: "))
#         b=int(input("enter the breadth: "))
#         sq=square(l,b)  
#         print(sq.area())  
#         print(sq.perimeter())
#         t-=1
#         c+=1
# if __name__=="__main__":
#     main()        


#digits to fact:
# class Solution:
#     def digitsInFactorial(self,n):
#         #write your code here
#         return f"square root of {n} is: {n**0.5}"

# def main():
#     t=int(input("enter : "))
#     while t>0:
#         n=int(input("enter: "))
#         sl=Solution()
#         print(sl.digitsInFactorial(n))
#         t-=1
# if __name__=="__main__":
#     main()        

          
# n=input("enter a string: ")
# for i in range(0,len(n)):
#     for j in range(i+1,len(n)+1):
#         print(n[i:j])
        

# for i in range(121,125):
#     for j in range(1,13):
#         print(i,"*",j, "=",i*j )

# list1=["i am ","you are"]
# list2=["healthy","fine","geek"]
# for item in list1:
#     print(f"start outer loop : {list1.index(item)+1}")
#     i=0
#     while i < len(list2):
#         print(item , list2[i])
#         i+=1
#     print("end of inner loop ")    

# left rotation
# def left(arr,k):
#     temp=arr[:k]
#     for i in range(0,len(arr)):
#             if i<len(arr)-k:
#                 arr[i]=arr[i+k]
#     arr[-k:]  = temp
#     return arr
# arr=list(map(int,input().split()))
# k=int(input())   
# print(left(arr,k)) 


# def right(arr,k):
#     temp=arr[-k:]
#     for i in range(len(arr)-k-1,-1,-1):
        
#             arr[i+k]=arr[i]

#     arr[:k]=temp
#     return arr
    


# arr=list(map(int,input().split()))
# k=int(input())   
# # print(right(arr,k)) 
# k=3     
# arr=[1,2,3,4,5,6,7]
# arr=arr[-k:]+arr[:-k]
# print(arr)


# def find_majority_party(num_voters, votes):
#     if num_voters == 0:
#         return -1
#     if num_voters == 1:
#         return votes[0]

#     # Phase 1: Find a candidate for majority element using Boyer-Moore Voting Algorithm
#     count = 0
#     candidate = None

#     for vote in votes:
#         if count == 0:
#             candidate = vote
#             count = 1
#         elif vote == candidate:
#             count += 1
#         else:
#             count -= 1

#     # Phase 2: Verify if the candidate is actually the majority element
#     count = 0
#     for vote in votes:
#         if vote == candidate:
#             count += 1

#     if count > num_voters // 2:
#         return candidate
#     else:
#         return -1

# # Test Cases
# # Example 1
# num_voters = 6
# votes = [1, 1, 2, 2, 2, 3]
# print(find_majority_party(num_voters, votes))  # Output: 2

# # Example 2
# num_voters = 6
# votes = [1, 2, 1, 1, 2, 2]
# print(find_majority_party(num_voters, votes))  # Output: -1

# # Additional Case with Tied Majority
# num_voters = 6
# votes = [1, 2, 1, 2, 1, 2]
# print(find_majority_party(num_voters, votes))  # Output: -1

# # Edge Case: Only one voter
# num_voters = 1
# votes = [5]
# print(find_majority_party(num_voters, votes))  # Output: 5

# arr = [10,4,8,3]
# left=[0]
# right=[0]
# s1=0
# s2=0
# s=[]
# if len(arr)==1 or len(arr)==0:
#     print([0])
# else:

#     for i in range(len(arr)-1):
#         s1+=arr[i]
#         left.append(s1)
#     for i in range(len(arr)-1,0,-1):
        
#         s2+=arr[i]
#         right.append(s2)
# right=right[::-1]      

# for i in range(len(arr)):
#     s.append(abs(left[i]-right[i]))
# print(s)
            


# import math
# def lcm(a,b):
#     Gcd=math.gcd(a,b)
#     Lcm=abs ((a*b)//(Gcd) )    
#     return Lcm
# a,b=map(int,input().split())
# print(lcm(a,b))     


#counting no of digits
# n=1245234
# c=0
# while n>0:
#     n=n//10
#     c+=1
 
# # print(c)

#palindrome
# def palindrome(n):
#     temp=n
#     rev=0
#     while temp>0:
#         rem=temp%10
#         rev=rev*10+rem
#         temp=temp//10
#     return rev==n
# n=int(input())
# print(palindrome(n))   
# 
# def pal(n):
#     temp = n
#     rev = 0
#     while temp != 0:
#         s = temp % 10
#         rev = rev * 10 + s
#         temp = temp // 10
#         print(f"After extracting {s}: rev = {rev}, temp = {temp}")  # Debugging statement
       
#     print(f"Original number: {n}, Reversed number: {rev}")  # Final comparison debugging
#     return n == rev

# n = int(input())
# print(pal(n))

# def factorial(n):
#     result=1
#     for i in range(1,n+1):
#         result=result*i
#     return result    
# n=int(input())
# print(factorial(n))  

  
# def fact(n):
#     if n==0:
#         return 1
#     return  n*fact(n-1)    
# n=int(input())
# print(fact(n)) 
 

#gcd & lcm
# def gcd(a,b):
#     while b!=0:
#         a,b=b,a%b
#     return a   
# def lcm(a,b):
#     return abs((a*b)//gcd(a,b))         
# a,b = map(int,input().split())    
# print(gcd(a,b),lcm(a,b))

#prime number
# n=int(input())

# if n>1:
#     for i in range(2,(n//2)+1):
#         if n%i==0:
#             print("not a prime")
#             break
#     else:
#         print(f"{n} is a prime number")
# else:
#     print("not a prime")       
    

# n=int(input())
# if n>1:
#     limit=int((n**0.5)+1)
#     for i in range(2,limit):
#         if n%i==0:
#             print(True)
#             break
#     else:
#         print(False)   
# else:
#     print(False) 
# import math
# def primeFactor(n):
#     l=[]
#     c=0
#     for i in range(2,int(n**0.5)+1):
#         c+=1
#         while n%i==0:
#             l.append(i)
#             n=n//i
            
#     if n>1:
#         l.append(n)
#     print("n value inside is: ", n)    
#     print("square root inside the loop is: ",math.sqrt(n)) 
#     print("count is:", c)    
#     return f"prime factors are: {l}"
# n=int(input())
# print(primeFactor(n)) 
# print("n value outside is: ", n)
# print('square root inside the loop is :',math.sqrt(n))             


# In this problem, you need to write a program
# to calculate the electricity bill for a household,
# based on the units of electricity the household consumed
# The price for unit varies based on the slab. 
# The charges per unit for different slabs are as mentioned below:
# For the first 50 units (0-50), the charge is 2/unit
# For the next 100 units (51-150), the charge is 3/unit
# For the next 100 units (151-250), the charge is 5/unit
# For above 250 units (251 and above), the charge is 8/unit
# Apart from these charges, there is also an additional 
# surcharge of 20% on the total amount is added to the bill.
# Input:
# The input will be a single line containing an integer.
# Output:
# The output should be a single line containing the calculated bill amount.
# Explanation
# For example, if the given number of units is 50.
# Charges 2/unit for 0 to 50 units => 50 x 2 = 100
# Charges 3/unit for 51 to 150 units => 0 x 3 = 0
# Charges 5/unit for 151 to 250 => 0 x 5 = 0
# Charges 8/unit for 251 and above => 0 x 8 = 0
# Total => 100
# Surcharge (20% of Bill) => 100 x 0.2 = 20
# Bill => 120
# So the total bill should be 120.0
# Image 3:
# For example, if the given number of units is 200.
# Charges 2/unit for 0 to 50 units => 50 x 2 = 100
# Charges 3/unit for 51 to 150 units => 100 x 3 = 300
# Charges 5/unit for 151 to 250 => 50 x 5 = 250
# Charges 8/unit for 251 and above => 0 x 8 = 0
# Total => 650
# Surcharge (20% of Bill) => 650 x 0.2 = 130
# Bill => 780
# So the total bill should be 780.0




# n=int(input())
# if n<=50:
#     print(n*2 + (n*2)*0.2)
# elif n>=51 and n<=150:
#     amount=50*2+ (n-50)*3 
#     print(amount+ amount*0.2)
# elif n>=151 and n<=200:
#     amount=50*2+100*3+(n-150)*5  
#     print(amount+amount*0.2)
# elif n>=201:
#     amount=50*2+100*3+100*5+(n-250)*8
#     print(amount+amount*0.2)     



# n=int(input())
# rem=n
# a=n//2000
# rem=rem-a*2000
# b=rem//500
# rem=rem-b*500
# c=rem//200
# rem=rem-c*200
# d=rem//50
# rem=rem-d*50
# e=rem//20
# rem=rem-e*20
# f=rem//5
# rem=rem-f*5
# g=rem//2
# rem=rem-g*2
# h=rem//1
# print("2000:",a,"500:",b,"200:",c,"50:",d,"20:",e,"5:",f,"2:",g,"1:",h)





# s=input()
# n=int(input())
# if s=='Monday':
#     n=n
# elif s=='Tuesday':
#     n=n+1
# elif s=='Wednesday':
#     n+=2
# elif s=='Thursday':
#     n+=3
# elif s=='Friday':
#     n+=4
# elif s=='Saturday':
#     n+=5
# else:
#     n+=6    
                        
# if n%7==0:
#         print(s)
# elif n%7==1:
#         print("Tuesday")
# elif n%7==2:
#         print("Wednesday")
# elif n%7==3:
#         print("Thursday")
# elif n%7==4:
#         print("Friday")
# elif n%7==5:
#         print("Saturday")
# elif n%7==6:
#         print("Sunday")                     


# # Input
# s = input("Enter the day: ")
# n = int(input("Enter the number: "))

# # Convert the day to a numeric value
# if s == 'Monday':
#     current_day_value = 0
# elif s == 'Tuesday':
#     current_day_value = 1
# elif s == 'Wednesday':
#     current_day_value = 2
# elif s == 'Thursday':
#     current_day_value = 3
# elif s == 'Friday':
#     current_day_value = 4
# elif s == 'Saturday':
#     current_day_value = 5
# elif s == 'Sunday':
#     current_day_value = 6

# # Calculate the new day value
# new_day_value = (current_day_value + n) % 7

# # Convert the numeric value back to a day
# if new_day_value == 0:
#     print("Monday")
# elif new_day_value == 1:
#     print("Tuesday")
# elif new_day_value == 2:
#     print("Wednesday")
# elif new_day_value == 3:
#     print("Thursday")
# elif new_day_value == 4:
#     print("Friday")
# elif new_day_value == 5:
#     print("Saturday")
# elif new_day_value == 6:
#     print("Sunday")

# n=int(input())
# c= 1
# while c<=2*n:
    
#     if c<=n:
#         print(str(c)*c)
#     else:
#         print(str(c-n)*(c-n))
#     c+=1



# c=1
# while c<=n:
#     print("* "*c)
#     c+=1
# for i in range(1,n+1):
#     print("* "*i)

# n=int(input())
# for i in range(1,n):
#     print("*"*n)
# n1=n
# while n>0:
#     print("*"*n1)
#     n-=1

# for i in range(1,n+1):
#     print("*"*i)
# c=1
# while c<=n:
#     print("*"*c)
#     c+=1

# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j, end=" ")
#     print() 

# n=int(input())
# for i in range(n-1,-1,-1):
#     print("* "*(n-i))
     

# def gcd(a,b):
#     while b!=0:
#         a,b=b,a%b
#     return a 
# def lcm(a,b) :
#     lcm = abs (a*b) // gcd(a,b)
#     return lcm      
       
# a,b=map(int,input().split())
# print(gcd(a,b), lcm (a,b))  

#prime number

# n=int(input())
# if n>1:
#     is_prime=True
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             is_prime=False
#             break
#     print(is_prime)
# else:
#     print(False)    
# 
# fibonacci -- 0,1,1,2,3,5,8,13,21,34....
# 
# n=int(input())

# a,b=0,1
# fib=[]

# for i in range(0,n):
    
#     fib.append(a)
#     a,b=b,a+b
  
# print(fib)    

#36  2 2 9
# 
# def prime(n):
#     s=[]
#     for i in range(2,int(n**0.5)+1):
#         while n%i==0:
#             s.append(i)
#             n=n//i
#     if n>1:
#         s.append(n)
#     return s
# n=int(input())
# print(prime(n))                


# #divisors of n

# n=int(input())

# res=[]
# for i in range(1,int(n**0.5)+1):
#     if n%i==0:
#         print(i)
#         res.append(i)
#         if n//i!=0:
#             res.append(n//i)
# print(res)        
        



    