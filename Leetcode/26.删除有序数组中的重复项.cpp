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
int main()

{
   Solution so;
   int a[] = {0,1,1,2,2,3};
   vector<int> su(a,a+5);
   //在su中添加a的6个元素
   std::vector<int> nVec;
   nVec.push_back(1);
   nVec.push_back(1);
   nVec.push_back(2);
   nVec.push_back(3);
   nVec.push_back(4);
  //逐个第二种方式压入元素
  // for (int i = 0; i < su.size(); i++)
  //    cout << su[i] << endl;


   so.removeDuplicates(su);
   cout << su.size() << endl;
   return 0;
}

// @lc code=end

