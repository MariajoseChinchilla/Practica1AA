#indicar si hay numeros repetidos en un arreglo de enteros dado

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numset = set(nums)
        if len(numset) == len(nums):
            return False
        return True