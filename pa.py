n=int(input("records:"))
d=dict.fromkeys(range(1,n+1),[])
for i in range(1,n+1):
    a=input("std name:")
    b=int(input("roll no:"))
    c=int(input("sem:"))
    d=input("contact:")
    e=input("course:")
    print()
    d[i].append(a,b,c,d,e)

    
x=input("enter std name for displaying details:")
for j in range(1,n+1):
    for z in range(0,5):
        if(z==0):
            print("std name:",d[i][z])
        elif(z==1):
            print("roll no:",d[i][z])
        elif(z==2):
            print("sem:",d[i][z])
        elif(z==3):
            print("contact:",d[i][z])
        else:
            print("course=",d[i][z])
    break

            
