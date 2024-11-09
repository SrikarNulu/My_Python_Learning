with open("C:\\Users\\srika\\Documents\\pythonnew\\zfiles\\exercise.txt","r") as res,\
    open("C:\\Users\\srika\\Documents\\pythonnew\\zfiles\\fu.txt","w") as sol:

    for i in res:
        i=i.strip()
        i=i.split(",")
        prod=1
        for n in i:
            prod*=int(n)
        print(prod)    
        sol.write(f"product is: {prod} for the given numbers {','.join(i)}\n")