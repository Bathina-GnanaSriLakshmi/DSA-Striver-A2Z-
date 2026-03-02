#To find missing number from 1 to n 
arr = list(map(int,input("Enter numbers: ").split(" ")))
n = arr[-1]
actual_sum = n*(n+1)/2
sum = 0
for i in arr:
    sum += i
if sum == actual_sum:
    print("No number is missing")
else :
    print(f"{actual_sum - sum} is the missing number")