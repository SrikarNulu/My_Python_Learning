#class Attributes
# class student():
#     def __init__(self,name,age,course):
#         self.name=name
#         self.age=age
#         self.course=course
    
# st=student("sri",22,"IT")
# print(st.age,st.name,st.course) 
# st1=student("rav",21,"ece") 
# print(st1.age)      

#class methods
# class student():
#     followers=0
#     def __init__(self,name,age,course):
#         self.name=name
#         self.age=age
#         self.course=course
#     def work(self,read,play):
#         return f"{self.name} is {self.age} years old, studying in {self.course} and she has a hobby of reading {read} and playing {play} "
#     def update_follow(self,name):
#         self.followers += 1 
       

# student1=student("raya",19,"IT")
# print(student1.work("books","cricket"))
# student1.update_follow("k")
# print(student1.followers)

# student2=student("jaya",20,"CSE")
# print(student2.work("novels","badminton"))
# student2.update_follow("s")
# print(student2.followers)

#area and circumference of circle
# class circle():
    
#     def __init__(self,radius):
#         self.pi=3.14
#         self.radius=radius
#     def area(self):
#         a=self.pi*self.radius**2
#         return a    
#     def circumference(self):
#         c=2*self.pi*self.radius
#         return c
# radius1=int(input("enter a number: "))        
# circle1=circle(radius1)
# print(circle1.area())
# print(circle1.circumference()) 

# radius2=int(input("enter a number: "))        
# circle2=circle(radius2)
# print(circle2.area())
# print(circle2.circumference())

# #USING PI AS CLASS OBJECT ATTRIBUTE we can use self.pi or circle.pi whatever you want u can use
# class circle():
#     pi=3.14
#     def __init__(self,radius):
        
#         self.radius=radius

#     def area(self):
#         a=self.pi*self.radius**2
#         return a    
#     def circumference(self):
#         c=2*circle.pi*self.radius
#         return c
# radius1=int(input("enter a number: "))        
# circle1=circle(radius1)
# print(circle1.area())
# print(circle1.circumference()) 

#WITHOUT USING METHODS
# class circle():
#     pi=3.14
#     def __init__(self,radius):
        
#         self.radius=radius
#         self.area=circle.pi*radius*radius
#         self.circumference=2*self.pi*radius
    
    
# radius1=int(input("enter a number: "))        
# circle1=circle(radius1)
# print(f"radius of given circle is {circle1.radius}, area is {circle1.area}, and circumference is { circle1.circumference} ")


#rectangle
# class rectangle():
#     def __init__(self,length,breadth):
#         self.len=length
#         self.bre=breadth
#     def area(self):
#         return self.len*self.bre
#     def perimeter(self):
#         return 2*(self.len+self.bre)
# l,b=map(int,input().split())
# rec1=rectangle(l,b)
# print(rec1.area(), rec1.perimeter())                
       
# import sys

# sys.path.append('C:\\Users\srika\Documents\pythonnew\sampels')

# import sample as n

# print(n.area(50))

# n=input()
# m=input()
# try :
#     res= int(n)/int(m)
#     print(res)
# except Exception as e :
#     print("Exception occurred:",e)    



