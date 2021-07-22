/*
 * @lc app=leetcode.cn id=26 lang=cpp
 *
 * [26] 删除有序数组中的重复项
 */

// @lc code=start
#include <iostream>
#include <vector>
#include <string>
using namespace std;
class Solution {
public:
    int removeDuplicates(std::vector<int>& nums) {
        int n = nums.size();
        if (n == 0) {
            return 0;
        }
        int fast = 1, slow = 1;
        while (fast < n) {
            if (nums[fast] != nums[fast - 1]) {
                nums[slow] = nums[fast];
                ++slow;
            }
            ++fast;
        }
        cout << "数组为：";
        cout << "[" ;
        for (int i = 0; i < slow; i++){
            cout << nums[i] ;
            if ( i < slow-1)
            {
                cout << "," ;
                }
            }  
        cout << "]" << endl;
        cout << "数组长度为：";
        cout << slow << endl;
        return slow;
        
    }
};


// @lc code=end

