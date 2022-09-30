def CN217(nums):
    array = nums
    for i in range(len(array)):
        if array.count(array[i]) > 1:
            return print('true')
            exit()
        else:
            if i == len(array)-1:
                return print('false')


if __name__=="__main__":
    nums = [1,2,3,4]
    CN217(nums)