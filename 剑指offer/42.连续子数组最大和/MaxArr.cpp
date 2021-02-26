class Solution {
public:
    int maxSubArray(vector<int>& nums) {

        // 使用优化后的动态规划
        int all_max_val = nums[0];
        int sub_max_val = nums[0];

        // 特殊情况处理
        if(nums.size() == 1)
        {
            return all_max_val;
        }

        for(int cnt = 1; cnt < nums.size(); cnt++)
        {
            // 前一个数小于0，则直接替换为当前值
            if(sub_max_val < 0)
            {
                sub_max_val = nums[cnt];
            }
            else
            {
                sub_max_val = sub_max_val + nums[cnt];
            }

            if(sub_max_val > all_max_val)
            {
                all_max_val = sub_max_val;
            }
        }

        return all_max_val;


        // 使用动态规划的方式实现如下
        // vector<int> arr;
        // int max_val = nums[0];

        // // 特殊情况处理
        // if(nums.size() == 1)
        // {
        //     return max_val;
        // }
        // // 处理首元素
        // arr.push_back(nums[0]);

        // for(int cnt = 1; cnt < nums.size(); cnt++)
        // {
        //     // 前一个数小于0，则
        //     if(arr[cnt - 1] < 0)
        //     {
        //         arr.push_back(nums[cnt]);
        //     }
        //     else
        //     {
        //         int val = arr[cnt - 1] + nums[cnt];
        //         arr.push_back(val);
        //     }
        // }

        // for(int cnt = 0; cnt < arr.size(); cnt++)
        // {
        //     if(max_val < arr[cnt])
        //     {
        //         max_val = arr[cnt];
        //     }
        // }

        // return max_val;

    }
};