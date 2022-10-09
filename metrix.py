#input a no. from user
n=int(input())



# making pattern usign nested for loop
for i in range(n):
  # intializing variable as a empty string
  pattern=""
  for j in range(n):
    pattern+="*"
  
  # printing metrix`s rows line by line length to n
  print(pattern)
