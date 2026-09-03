nums=list(map(int,input("Enter the numbers:").split()))
largest=nums[0]
for num in nums:
    if num>largest:
        largest=num
print("The largest number is:",largest)