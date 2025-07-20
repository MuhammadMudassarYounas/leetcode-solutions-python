# This code finds the maximum number of consecutive 1's in a binary array.
num = [1, 1, 0, 1, 1, 1]

def ConsecutiveOnes(num):
    counter = 0
    maxCounter = 0
    for i in range(len(num)):
        if num[i] == 1:
            counter += 1
            maxCounter = max(maxCounter, counter)
        else:
            counter = 0
    return maxCounter

print(ConsecutiveOnes(num))
