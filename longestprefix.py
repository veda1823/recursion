words = input("Enter words: ").split()

prefix = words[0]

for word in words[1:]:
    while not word.startswith(prefix):
        prefix = prefix[:-1]

print("Longest common prefix:", prefix)