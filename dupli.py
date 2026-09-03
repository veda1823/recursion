nums = list(map(int, input("Enter numbers: ").split()))
seen = set()
duplicates = set()
for num in nums:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)
print("Duplicates:", duplicates)