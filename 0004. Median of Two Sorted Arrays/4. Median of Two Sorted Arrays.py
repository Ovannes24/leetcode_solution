# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         n = sorted(nums1 + nums2)
#         l = len(nums1) + len(nums2)
#         if l % 2 == 0:
#             return (n[l//2] + n[l//2-1]) / 2
#         else:
#             return n[l//2]


# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # def median(n):
        #     l = len(n)
        #     if l % 2 == 0:
        #         return (n[l//2] + n[l//2-1]) / 2
        #     else:
        #         return n[l//2]

#         return (median(nums1) + median(nums2)) / 2

# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         n = sorted(nums1 + nums2)
#         l = len(n)
#         if l % 2 == 0:
#             return (n[l//2] + n[l//2-1]) / 2
#         else:
#             return n[l//2]











# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         def median(n):
#             l = len(n)
#             if l % 2 == 0:
#                 return (n[l//2] + n[l//2-1]) / 2
#             else:
#                 return n[l//2]
#         l1 = len(nums1)
#         l2 = len(nums2)
        
#         if l1 == 0:
#             return median(nums2)
#         elif l2 == 0:
#             return median(nums1)

#         if nums2[0]<nums1[0]:
#             return self.findMedianSortedArrays(nums2, nums1)
#         l12 = l1+l2

#         i = 0
#         j = 0

#         if l12 % 2 == 0:
#             s = 0
#             for k in range(l12//2+1):
#                 if nums1[i] < nums2[j]:
#                     if i+j == l12//2-1:
#                         s = nums1[i] 
#                     i = i + 1
#                 else:
#                     if i+j == l12//2-1:
#                         s = nums2[j] 
#                     j = j + 1 

#                 # print(k, i, j, nums1[i], nums2[j], l12//2, i+j, s)

#                 # if i+1 < l1-1:
#                 #     if nums1[i] < nums2[j]:
#                 #         return (s + nums1[i+1])/2
#                 #     else:
#                 #         return (s + nums2[j])/2
#                 # else:
#                 if i+j > l12//2-1:
#                     return (nums1[i] + nums2[j])/2
                    
#         else:
#             for k in range(l12//2+1):
#                 print(k, i, j, nums1[i], nums2[j], l12//2, i+j)
#                 if nums1[i] < nums2[j]:
#                     if i+j == l12//2:
#                         return nums1[i] 
#                     i = i + 1
#                 else:
#                     if i+j == l12//2:
#                         return nums2[j] 
#                     j = j + 1 


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def median(n):
            l = len(n)
            if l % 2 == 0:
                return (n[l//2] + n[l//2-1]) / 2
            else:
                return n[l//2]
        l1 = len(nums1)
        l2 = len(nums2)
        
        if l1 == 0:
            return median(nums2)
        elif l2 == 0:
            return median(nums1)

        if nums2[0]<nums1[0]:
            return self.findMedianSortedArrays(nums2, nums1)
        l12 = l1+l2

        i = 0
        j = 0

        if l12 % 2 == 0:
            s = 0
            for k in range(l12//2):
                if nums1[i] < nums2[j]:
                    if i+j == l12//2-1:
                        s = nums1[i] 
                    i = i + 1
                else:
                    if i+j == l12//2-1:
                        s = nums2[j] 
                    j = j + 1 
            print(i, j, s)

            if i==l1:
                s += nums2[j] 
            if j==l2:
                s += nums1[i] 


            # if nums1[i] < nums2[j]:
            #     if i+j == l12//2-1:
            #         s += nums1[i] 
            #     i = i + 1
            # else:
            #     if i+j == l12//2-1:
            #         s += nums2[j] 
            #     j = j + 1 
            return s/2

                    
        else:
            for k in range(l12//2+1):
                print(k, i, j, nums1[i], nums2[j], l12//2, i+j)
                if nums1[i] < nums2[j]:
                    if i+j == l12//2:
                        return nums1[i] 
                    i = i + 1
                else:
                    if i+j == l12//2:
                        return nums2[j] 
                    j = j + 1 