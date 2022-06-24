n = int(input())
nums = [int(x) for x in input().split()][:n - 1]
for i in range(1, n + 1):
    if i not in nums:
        print(i)
        break
    