#
# @lc app=leetcode.cn id=4 lang=python
#
# [4] 寻找两个有序数组的中位数
#

# @lc code=start
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        #默认nums1长度大于nums2，如果小于了，那么就将其交换
        #假定理想的中位数是x，假定在nums1和nums2中都存在一个数（或者一个位置），使该位置左边都小于x，该位置右边都大于x，所以目标就是找到这么两个位置也就是mid1和mid2
        if len(nums1) > len(nums2):
            nums1 , nums2 = nums2,nums1 
        len1 = len(nums1)
        len2 = len(nums2)
        
        left ,right ,half_len = 0,len1,(len1 + len2 + 1) // 2

        #出循环时mid1和mid2都在最完美的位置，也就是二者对应的假设中位数的位置
        while left <= right:
             #更新mid1和mid2
            mid1 = (left + right) // 2
            mid2 = half_len - mid1

            #若nums2中间点左边都要比nums1中间点大，说明mid的位置小了，那么就要增加mid
            #当然还要保证mid1不越界
            if mid1 < len1 and nums2[mid2-1] > nums1[mid1]:
                left  = mid1 + 1
            
            elif mid1 > 0 and nums1[mid1-1] > nums2[mid2]:
                right = mid1 -1
            
            else:
                 #返回情况判断
                if mid1 == 0:
                    max_of_left = nums2[mid2-1]
                elif mid2 == 0:
                    max_of_left = nums1[mid1-1]
                else:
                    max_of_left = max(nums1[mid1-1],nums2[mid2-1])
           
                #如果时奇数，直接返回max_of_left就可以了，也就是其中一个最大值
                if (len1 + len2) % 2 == 1:
                    return max_of_left
                 #如果不是奇数，则还要判断右边，中位数是左边和右边的二分之一
                if mid1 == len1:
                    min_of_right = nums2[mid2]
                elif mid2 == len2:
                    min_of_right = nums1[mid1]
                else:
                    min_of_right = min(nums1[mid1],nums2[mid2])
        
                return (min_of_right + max_of_left) / 2
        
        
        
       


# @lc code=end

