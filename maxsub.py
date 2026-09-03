nums = list(map(int, input("Enter numbers: ").split()))
current_sum = nums[0]
max_sum = nums[0]
for num in nums[1:]:
    current_sum = max(num, current_sum + num)
    max_sum = max(max_sum, current_sum)
print("Maximum subarray sum:", max_sum)