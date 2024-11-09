#date 24/09/2024

#string reversal 
# s='srikar nulu'
# print(s[::-1])

#reversing words
# a='happy birthday sowmya'
# s=a.split()
# s=s[::-1]
# s1=' '.join(s)
# print(s1)

#reversing internal content of a string
# a= 'happy birthday sowmya'
# s=a.split()
# s=' '.join(s)
# print(s[::-1])

#characters at even and odd position
# a='srikar are you happy'
# print('EVEN POSITION :',a[0::2])
# print('ODD POSITION :',a[1::2])

#merging two strings alternatively
a='srikar are u happy or sad'
b='can u really find a job or not'
a1=len(a)
b1=len(b)
res=''
for  i in range(max(a1,b1)):
    if i<a1 :
       res+=a[i]
    if i<b1:   
       res+=b[i]
print(res)    






