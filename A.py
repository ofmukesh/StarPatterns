n=int(input())
c=int(n/2)
for i in range(n):
    p=""
    for j in range(n):
        if j==n-i-1 or j>=c and i==c+1 or j==n-1:
            p+="*"
        else:
            p+=" "
    print(p)
