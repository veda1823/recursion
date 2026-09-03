nums = list(map(int, input("Enter numbers: ").split()))
result = []
for num in nums:
    if num != 0:
        result.append(num)
zeros = len(nums) - len(result)
result.extend([0] * zeros)
print(result)