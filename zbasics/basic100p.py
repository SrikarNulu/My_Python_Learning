# ages=map(int,input().split())
# s=list(ages)
# maxi=0
# for i in s:
#     if i>maxi:
#         maxi=i
# print(maxi)

# n=list(map(int,input().split()))
# n.sort()
# print(n[-1])

#2)celsius to fahrenheit

# c=int(input())
# # f=int(input())

# f= c*(9/5)+32
# # c = f* (5/9) - 32 

# print(f)


#class degree: ''' incorrect code '''
#     def __init__self(celsius,fahrenheit):
#         celsius=self.celsius
#         fahrenheit=self.fahrenheit
#     def cel(celsius,fahrenheit):
#         c=self.fahrenheit * (9/5) + 32
#         return c 
#     def fah(fahrenheit,celsius) :
#         f= self.celsius*(5/9) - 32   
#         return f 
# cels=int(input())
# fahr=int(input())
# ob= degree() 
# print(ob.cel(cels,fahr))
# print(ob.fah(fahr,cels)) 
# 
# class degree:
#     def __init__(self,celsius,fahrenheit):
#         self.celsius=celsius
#         self.fahrenheit=fahrenheit
#     def cel(self):
#         c=self.celsius * (9/5) + 32
#         return c 
#     def fah(self) :
#         f= (self.fahrenheit - 32) * (5/9)  
#         return f 
# cels=int(input())
# fahr=int(input())
# ob= degree(celsius=cels,fahrenheit=fahr) 
# print(ob.cel())
# print(ob.fah())  
# 
#7) leap year
# n=int(input())
# if (n%4==0 and n%100 !=0) or (n%400==0):
#     print(True)     
# else:
#     print(False)

#8) euclidean distance

# x1=int(input())
# y1=int(input())
# x2=int(input())
# y2=int(input())

# d= ((x2-x1)**2 + (y2-y1)**2)**0.5
# print(d)

#9) a=int(input())
# b=int(input())
# c=int(input())

# res=a+b+c
# if res==180 and a>0 and b>0 and c>0:
#     print(True)
# else:
#     print(False)    


# res=list(map(int,input().split()))

# for i in range(1,4):
#     if i not in res:
#         print(i) 

# t=int(input())

# for i in range(t):
#     n=int(input())
#     l=list(map(int,input().split()))
#     s1=sum(l[::2])
#     s2=sum(l[1::2])
#     res=s1-s2
#     print(res)

# s='this is srikar calling'
# res=s.split()
# print(" ".join(res[::-1]))

# x,y,z=map(int,input().split())

# res=x+y+z

# print(res/3)


# t=int(input())
# for i in range(t):
#     a,b=map(int,input().split())
  
#     if a==0 and b%2!=0:
#         print("NO")
#     elif a==0 and b%2==0 and b>1: 
#         print("YES")   
#     elif b==0 and a%2==0:
#         print("YES")   

#     elif (a*1 + b*2) %2==0:
#         print("YES") 

#     elif (a*1+b*2) % 2!=0:
#         print("NO")


# t=int(input())
# for i in range(t):
#     a,b=map(int,input().split())
    
#     if a==0 and b%2!=0:
#         print("NO")
    
#     elif a==0 and b%2==0 and b>1:
#         print("YES")
    
#     elif (b==0 and a%2==0):
#         print("YES")
    
#     elif (a*1 + b*2 ) %2 ==0:
#         print("YES")
    
#     elif (a*1 + b*2 ) %2 !=0:
#         print("NO")  


