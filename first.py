def twoSum(nums,target):
    for i in range (len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return [i,j]
    return None
nums=list(map(int,input("Enter the numbers: ").split()))
target=int(input("Enter the target: "))
print(twoSum(nums,target))
