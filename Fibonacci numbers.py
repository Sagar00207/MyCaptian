a=0
b=1
n=int(input("Enter number of terms you needed:"))
print(a)
print(b)
for i in range(n-2):
    c=a+b
    a=b
    b=c
    print(c)
