#include<iostream>
#include<vector>
class Solution {
public:
    int timeRequiredToBuy(vector<int>& tickets, int k) {
        int r=0;
        for(int i=0;tickets[k]>0;i++){
            for(int j=0;j<tickets.size();j++){
                if(tickets[j]!=0){
                    tickets[j]= tickets[j]-1;
                    r++;
                }
            }
        }
        return r;
    }
};