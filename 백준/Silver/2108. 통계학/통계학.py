import sys
from collections import Counter

input = sys.stdin.read
data = list(map(int, input().split()))

n = data[0]
nums = data[1:]
avg = round(sum(nums) / n)
nums.sort()
median = nums[n // 2]
count = Counter(nums)
modes = count.most_common()
max_freq = modes[0][1]
mode_list = [num for num, freq in modes if freq == max_freq]
mode_list.sort()
mode = mode_list[0] if len(mode_list) == 1 else mode_list[1]
rng = max(nums) - min(nums)
print(avg)
print(median)
print(mode)
print(rng)
