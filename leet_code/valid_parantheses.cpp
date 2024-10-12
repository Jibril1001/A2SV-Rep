#include <iostream>

using namespace std;
class Solution {

public:
    bool isValid(string s) {
      stack<char> arr;
      for(int i=0;i<s.length();i++){

      if(s[i]=='('||s[i]=='['||s[i]=='{') arr.push(s[i]);
      
      else if(!arr.empty()){

        if(s[i]==')' && arr.top()=='('){
            arr.pop();
        }else if(s[i]==']' && arr.top()=='['){
            arr.pop();
        }else if(s[i]=='}' && arr.top()=='{'){
            arr.pop();
        }else return false;

      } else if(arr.empty()) return false;
      
    }

    if(arr.empty()){
    return true;
    }else return false;
    }
};