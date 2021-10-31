
def sort(list):

        for i in range(len(nums)-1):
            minpos = i
            for j in range(i,len(nums)-1):
                if nums[minpos] > nums[j]:
                    minpos = j

            temp = nums[i]
            nums[i] = nums[minpos]
            nums[minpos] = temp


nums = [7, 4, 0, 3, 9, 2, 6, 1, 5, 8]


sort(nums)

print(nums)