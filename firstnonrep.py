s=input("Enter a string: ")
count ={}
for char in s:
    count[char] = count.get(char, 0) + 1
for char in s:
    if count[char] == 1:
        print("First non-repeating character:", char)
        break