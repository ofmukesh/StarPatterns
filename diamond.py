n=50
c=int(n/2)

for i in range(n):
    p=""
    for j in range(n):
        if j==c-i :
            p+="*"
        elif i==c+j:
            p+="*"
        elif j==c+i:
            p+="*"
        elif i==n-1-j+c:
            p+="*"
        else:
            p+="_"
    print(p)
