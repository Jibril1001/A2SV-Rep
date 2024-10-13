#include<iostream>
using namespace std;
class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> num;
        int x,y;
        for(int i=0;i<tokens.size();i++)
        {
            if( ( tokens[i].length()==1 && isdigit(tokens[i][0]) ) || tokens[i].length()>1 )
            {
                num.push( stoi( tokens[i] ) );
            }else
            {
                if(tokens[i]=="*")
                {
                    x=num.top();
                    num.pop();
                    y=num.top();
                    num.pop();
                    num.push( x*y );
                }else if(tokens[i]=="/")
                {
                    x=num.top();
                    num.pop();
                    y=num.top();
                    num.pop();
                    num.push( y/x );
                }else if(tokens[i]=="+")
                {
                    x=num.top();
                    num.pop();
                    y=num.top();
                    num.pop();
                    num.push( x+y );
                }else if(tokens[i]=="-")
                {
                    x=num.top();
                    num.pop();
                    y=num.top();
                    num.pop();
                    num.push( y-x );
                }

                
            }
        }
        return num.top();
    }
};