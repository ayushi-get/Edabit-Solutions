def oddone(*a):
    l=len(a)
    for i in a:
        n=0
        for j in range(l):
            if i==a[j]:
                n+=1
        
        if n%2==0:
            pass
        else:       
            print(i)
            break    



from array import *
a=array("i",[])
l=int(input("enter the length of the array: "))
print("Enter the numbers for the arrray:")
for i in range(l):
    t=int(input(""))
    a.append(t)
print("\n ")
print("The number that occur odd number of times is:")
oddone(*a)
