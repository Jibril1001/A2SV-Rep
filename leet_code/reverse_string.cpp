#include<iostream>
#include<vector>
class Solution {
public:
    void reverseString(vector<char>& s) {
        int i=0,j=s.size()-1,n;
        while(i<=j){
            if(s[i]==s[j]){
                i++;
                j--;
                continue;
            }
            n=s[i];
            s[i]=s[j];
            s[j]=n;
            i++;
            j--;
        }
    }
};