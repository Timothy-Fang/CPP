/*
 * @lc app=leetcode.cn id=26 lang=c
 *
 * [26] 删除有序数组中的重复项
 */

// @lc code=start
#include <stdio.h>

int removeDuplicates(int* nums, int numsSize) {
    if (numsSize == 0) {
        return 0;
    }
    int fast = 1, slow = 1;
    while (fast < numsSize) {
        if (nums[fast] != nums[fast - 1]) {
            nums[slow] = nums[fast];
            ++slow;
            //printf ("数组长度为 : %d\n", slow);
        }
        ++fast;
    }
    printf ("数组长度为：%d",slow);   //这里为什么%d后面加不加\n差10倍
    for(int i=0; i<slow; i++) //有几个单元 i就<几，如果大于单元数就结束循环
    printf("%d\n",nums[i]);
    //printf ("当前数组: %d", nums);
    return slow;
}

int main()
{
    
    int a[] = {0,1,1,2,2,3};
    int b = removeDuplicates(a,6);
    printf("数组长度为 : %d",b);
    return 0;
}

// @lc code=end



