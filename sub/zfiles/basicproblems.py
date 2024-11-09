# s=open("C:\\Users\\srika\\Documents\\pythonnew\\\\zfiles\\new.txt","r")

# s1=open("C:\\Users\\srika\\Documents\\pythonnew\\zfiles\\fun.txt","w")
# for line in s:
  
#     words=line.split(" ")
#     s1.write("word count: "+ str(len(words)) +" "+ line)
 

# s.close()
# s1.close()

# # with open("C:\\Users\\srika\\Documents\\pythonnew\\\\zfiles\\new.txt","r") as f:
# #   print(f.read()) 
# print(s1.closed)


# with open("C:\\Users\\srika\\Documents\\pythonnew\\zfiles\\exercise.txt",'r') as f:
#     c=0
    
#     num=input()
#     for line in f:
#         line1=line.strip()
#         line1=line1.split(",")
       
#         for i in line1:
#             if i==num:
#                 c+=1
# print(c)    
# 

# with open("C:\\Users\\srika\\Documents\\pythonnew\\zfiles\\exercise.txt",'r') as f,   \
#     open("C:\\Users\\srika\\Documents\\pythonnew\\zfiles\\fu.txt", 'a') as f1:
    
#     for i in f:
#         i=i.strip()
#         numbers=i.split(",")
#         s=0
#         for num in numbers: 
#             num=int(num) 
#             s+=num
#         print(s)
#         f1.write(f"sum: {s} | {','.join(numbers)}\n") 
       


#with open("C:\\Users\\srika\\Documents\\pythonnew\\zfiles\\exercise.txt","r") as res,\
#     open("C:\\Users\\srika\\Documents\\pythonnew\\zfiles\\fu.txt","a") as sol:

#     for i in res:
#         i=i.strip()
#         i=i.split(",")
#         prod=1
#         for n in i:
#             prod*=int(n)
#         print(prod)    
#         sol.write(f"product is: {prod} for the given numbers {','.join(i)}\n")




          
        
        







































