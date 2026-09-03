nums = list(map(int, input("Enter numbers: ").split()))
n = max(nums)
total_sum = n * (n + 1) // 2
actual_sum = sum(nums)
missing = total_sum - actual_sum
print("Missing number:", missing)