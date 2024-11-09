book={}

book['sri'] = {

    "name" : "sri",
    "age" : 22
, "phone" : 44444
}

book['ram'] = {

    "name" : "ram",
    "age" : 11
, "phone" : 3333
}

book['kav'] = {

    "name" : "kav",
    "age" : 33
, "phone" : 1111
}

#print(book)

import json
s= json.dumps(book)

#with open ("C://Users/srika/Documents/pythonnew/sampels/adres.txt","w") as f:
    #f.write(s)

p= open ("C://Users/srika/Documents/pythonnew/sampels/adres.txt","r")
z=p.read()
#print(z)
books = json.loads(z)
#print(books)

print(books['ram']['age'])

for i in books:
    print(books[i])

