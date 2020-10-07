from collections import Counter

wordfile = input('Enter text/text file')

try:
    file = open(wordfile)

except:
    file = wordfile

splitting = file.split()
counter= Counter(splitting)
print(counter)

print(counter.most_common(2))