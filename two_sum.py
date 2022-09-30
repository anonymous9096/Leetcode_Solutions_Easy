def TWO_SUMS(nums, target):
    if 2 <= len(nums) <= 1000:
            if  -1000000000 <= target <= 1000000000:
                for i in range(len(nums)):
                    for j in range(1, len(nums)):
                        if (nums[i] + nums[j]) == target:
                            if i == j:
                                pass
                            else:
                                return print([i, j])
                                break
    else:
        pass


if __name__=="__main__":
    nums = [2, 3, 4, 6]
    target = 10
    TWO_SUMS(nums, target)
