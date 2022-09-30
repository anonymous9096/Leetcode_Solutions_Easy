def MZ(nums):
    root = nums
    for i in range(len(root)):
        if root[i] == 0:
            root.remove(root[i])
            root.append(0)

    return print(root)


if __name__=="__main__":
    nums = [0, 1, 3, 0, 15]
    MZ(nums)