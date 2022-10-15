
# input a intenger from user
n=int(input())
center=n
# making and printing pattern using nested for loop
for i in range(n):
  # custom variable for patterns
  pattern=""
  for j in range((n*2)-1):
    
    # condtional statment
    if j>=center-1-i and j<=center-1+i:
      pattern+="*"
    else:
      pattern+=" "
    
  # printing pattern
  print(pattern)
