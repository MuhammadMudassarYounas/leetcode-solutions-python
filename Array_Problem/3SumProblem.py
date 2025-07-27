Arr = [-1,0,1,2,-1,-4]

def ThreeSum(Arr):
    Result = []
    Arr.sort()
    n = len(Arr)

    for i in range(n):
        if i > 0 and Arr[i] == Arr[i - 1]:
            continue  # skip duplicate i values

        j = i + 1
        k = n - 1

        while j < k:
            total = Arr[i] + Arr[j] + Arr[k]

            if total < 0:
                j += 1
            elif total > 0:
                k -= 1
            else:
                Result.append([Arr[i], Arr[j], Arr[k]])
                j += 1
                k -= 1

                # ✅ skip duplicate j values
                while j < k and Arr[j] == Arr[j - 1]:
                    j += 1
                # ✅ skip duplicate k values
                while j < k and Arr[k] == Arr[k + 1]:
                    k -= 1

    return Result

print(ThreeSum(Arr))