class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        a, b = nums1, nums2
        

        if len(b) < len(a):
            a, b = b, a
        
        lena, lenb = len(a), len(b)
        total = lena + lenb
        mid = (total + 1)//2

        l, r = 0, lena

        while l <= r:
            mid1 = (l + r) // 2
            mid2 = mid - mid1

            aleft = a[mid1 - 1] if mid1 > 0 else float("-inf")
            bleft = b[mid2 - 1] if mid2 > 0 else float('-inf')

            aright = a[mid1] if mid1 < lena else float('inf')
            bright = b[mid2] if mid2 < lenb else float('inf')

            if aleft <= bright and bleft <= aright:
                if total % 2 ==1:
                    return  max(aleft, bleft)
                
                return (max(aleft, bleft) + min(aright, bright)) / 2
            
            if aleft > bright:
                r  =  mid1  - 1
            else:
                l = mid1 + 1
        return 0.0