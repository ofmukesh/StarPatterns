# input a intenger from user
n=int(input())

# making and printing pattern using nested for loop
for i in range(n):
  # custom variable for patterns
  pattern=""
  for j in range(i):
    pattern+="*"
    
  # printing pattern
  print(pattern)
