#To return the maximum profit you can acheive
def stock_prices(arr):
    min = arr[0]
    current_max = 0
    best_max = 0
    for i in range(len(arr)):
            if arr[i]<min:
                  min = arr[i]
            current_max = arr[i] - min
            if current_max>best_max:
                        best_max = current_max
    print(f"Maximumm profit is {best_max}")
arr = list(map(int,input("Enter prices with space between them ").split()))
stock_prices(arr)