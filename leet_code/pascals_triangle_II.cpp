#include <iostream>
#include <vector>
Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<vector<int>> ls = {{1}, {1, 1}};
        if (rowIndex<ls.size()){
            return ls[rowIndex];
        }
        ls.push_back(getRow(rowIndex-1));
        vector<int> last_list=ls[ls.size()-1];
        vector<int>cur={1};
        for(int i=0;i<rowIndex-1;i++){
            cur.push_back(last_list[i]+last_list[i+1]);
        }
        cur.push_back(1);
        return cur;
    
    }
};