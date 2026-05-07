class Solution {
   public:
    int longestConsecutive(vector<int>& nums) {
        if(nums.size()==0)return 0;
        map<int, int> mp;
        for (auto num : nums) {
            mp[num]++;
        }

        vector<int> res;
        for (auto m : mp) {
            res.push_back(m.first);
        }


        if (res.size() == 1) return 1;
        int ans = 1;
        int i = 0;
        for (int j = 1; j < res.size(); j++) {
            if (res[j] - res[j - 1] == 1) {
                ans = max(ans, j - i+1);

            } else {
                i = j;
            }
        }
        return ans;
    }
};
