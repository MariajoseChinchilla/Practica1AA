def intersect(nums1, nums2):
    answer = []
    if len(nums1) < len(nums2):
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                answer.append(nums1[i])
                nums2[nums2.index(nums1[i])] = None
                nums1[i] = None
    if len(nums2) <= len(nums1):
        for i in range(len(nums2)):
            if nums2[i] in nums1:
                answer.append(nums2[i])
                nums1[nums1.index(nums2[i])] = None
                nums2[i] = None
    return answer


print(intersect([1,2,3,4,5,5,5,6],[1,2,3,4,5,5]))