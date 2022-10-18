n=int(input())
c=int(n/2)
for i in range(n):
    p=""
    for j in range(n):
        if i==0:
            p+="*"
        elif j==c:
            p+="*"
        elif i==n-1 and j<c:
            p+="*"
        elif i>=c and j==0:
            p+="*"
        else:
            p+=" "
    print(p)
