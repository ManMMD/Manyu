def bubble_sort(nums):
    for i in range(len(nums) - 1):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    print(nums)

if __name__ == '__main__':
    a=raw_input('ten numbers:')
    s=a.split()
    for i in range(len(s)):
        s[i]==int(s[i])
    bubble_sort(s)
