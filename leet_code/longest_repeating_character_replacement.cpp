#include <iostream>
using namespace std;
class Solution {
public:
    int characterReplacement(string s, int k) {
        int total=0,count=0;
        for(char ch='A';ch<='Z';ch++){
            int i=0,j=0,f=0;
            count=0;
            while( j<s.length()){
                if(s[j]==ch){
                    count++;
                    j++;
                    total=max(total,count);
                }else if(f!=k){
                    f++;
                    count++;
                    j++;
                    total=max(total,count);
                }else if (s[i]!=ch){
                    count--;
                    i++;
                    f--;
                }else{
                    i++;
                    count--;
                }
                
            }

        }
        return total;
    }
};