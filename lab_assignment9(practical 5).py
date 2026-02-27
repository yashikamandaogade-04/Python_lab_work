"""
#lab assignment 1
nums = tuple(map(int,input("Enter integers separated by space: ").split()))
print("Total items:",len(nums))
print("Last item:",nums[-1])
print("Reverse order:",nums[::-1])
if 5 in nums:
    print("Yes")
else:
    print("No")
if len(nums) > 2:
    new_tuple = nums[1:-1]
    sorted_tuple = tuple(sorted(new_tuple))
    print("After removing first and last and sorting:", sorted_tuple)
else:
    print("Not enough elements")
"""
#lab assignment 2
prices = tuple(map(int, input("Enter prices separated by space: ").split()))
print("Total items sold:", len(prices))
print("Cheapest item price:", min(prices))
print("Costliest item price:", max(prices))
print("Prices in ascending order:", tuple(sorted(prices)))
costliest = max(prices)
count = prices.count(costliest)
print("Number of costliest items sold:", count)