nums=list(map(int,input().split()))
count={}
for num in nums:
    count[num]=count.get(num,0)+1
for num, freq in count.items():
    print(num,":",freq)