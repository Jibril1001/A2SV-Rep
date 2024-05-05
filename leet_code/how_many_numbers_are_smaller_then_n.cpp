#include<vector>
#include<algorithm>
#include<map>
class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        vector<int> sortedv=nums;
        vector<int> answer(nums.size());
        sort(sortedv.begin(),sortedv.end());
        map<int,int> mymap;
        int z,c=0;

          for (int i = 0; i < nums.size(); i++) {
            if (mymap.find(sortedv[i]) == mymap.end()) {
                mymap[sortedv[i]] = i;
            }
        }


        for(int i=0;i<nums.size();i++){
         answer[i]=mymap[nums[i]];
        }

        return answer;
    }
};