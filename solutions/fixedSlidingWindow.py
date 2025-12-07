from asyncore import close_all


def closeDuplicates(nums, k):
    window = set()
    L = 0

    for R in range(len(nums)):
        if R - L + 1 > k:
            #we remove from the hast set if it's greter than k
            window.remove(nums[L])
            L += 1
        if nums[R] in window:
            return True
        
        window.add(nums[R])

    return False

nums = [1,2,3,2,3,3]

sol = closeDuplicates(nums, 1)

print(sol)