import math
x= input("input Data : ")
c= int(x)
cek =1
a = 0
b=1
iter = 1

while cek>0.001:
    f_x = 0
    f_y = 0
    for i in range(a):
        f_x += (2**i)*c**i/math.factorial(i)
    for j in range(b):
        f_y += (2**j)*c**j/math.factorial(j)
    cek = f_y-f_x
    a+=1
    b+=1
    print("iterasi ke-",iter,"= ",cek)
    iter+=1 
