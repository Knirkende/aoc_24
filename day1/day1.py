from collections import Counter

with open('input1.txt', 'r') as file:
    l = file.readlines()
    left, right = sorted([int(x.split()[0].strip()) for x in l]), sorted([int(x.split()[1].strip()) for x in l])

acc = 0
right_count = Counter(right)

for i in range(len(left)):
    #acc += abs(left[i] - right[i]) #part1
    acc += abs(left[i]) * right_count.get(left[i], 0) #part2

print(acc)
