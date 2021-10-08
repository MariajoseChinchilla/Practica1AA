def twoSum(nums, target):
    for i in range(0,len(nums)-1):
        list = nums[i+1:len(nums)]
        if target - nums[i] in list:
            answer = [i,list.index(target - nums[i])+i+1]
            break
    return answer
