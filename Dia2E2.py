class Solution:
    def merge(self,nums1, m, nums2, n):
        del nums1[m::]      #guardar hasta el m-esimo
        nums1.extend(nums2)     #agregar nums2
        nums1.sort()        #ordenar


def delete(nums,n,m):
    del nums[n:m]
    return nums