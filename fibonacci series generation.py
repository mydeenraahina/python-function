def fibo(value):
    x,y=0,1
    print(x,y,end=" ")
    for i in range(1,value):
        z=x+y
        print(z,end=" ")
        x,y=y,z
    return z
print(fibo(10))
        
