#include<iostream>
#include<unordered_map>
using namespace std;
class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        unordered_map<char,int> dic;
        vector<int> ls;
        for(int i=0;i<p.length();i++){
            dic[p[i]]++;
        }
        unordered_map<char,int> dic1;
        dic1=dic;
        int siz=p.length();
        int i=0,j=0;
        while(j<s.length()){
            if(dic.find(s[j])!=dic.end()){
                if (dic[s[j]]==0){
                    dic[s[i]]++;
                    i++;
                    siz++;
                }else{
                    siz--;
                    dic[s[j]]--;
                    j++;
                }
                if (siz==0) ls.push_back(i);
            }else{
                j++;
                i=j;
                dic=dic1;
                siz=p.length();
            }
        }
        return ls;
    }
};