# input a intenger from user
n=int(input())
center=int(n/2)+1

# making and printing pattern using nested for loop
for i in range(n):
  # custom variable for patterns
  pattern=""
  for j in range(n):
    
    # condtional statment
    if j==0 or j==n-1 or j==i  :
      pattern+="*"
    else:
      pattern+="-"
    
  # printing pattern
  print(pattern)
