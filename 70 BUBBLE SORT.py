
def sort(list,rof='null'):
    if rof == 'r':
        for i in range(len(nums) - 1, 0, -1):
            for j in range(i):
                if nums[j] < nums[j + 1]:
                    temp = nums[j]
                    nums[j] = nums[j + 1]
                    nums[j + 1] = temp
    else:
        for i in range(len(nums)-1,0,-1):
            for j in range(i):
                if nums[j] > nums[j+1]:
                    temp = nums[j]
                    nums[j] = nums[j+1]
                    nums[j+1] = temp



nums = [7, 4, 0, 3, 9, 2, 6, 1, 5, 8]


sort(nums,'r')

print(nums)