class Solution {
public:
    int maxArea(vector<int>& height) {
        int i=0,j=height.size()-1;
        int max=(height.size()-1)*min(height[i],height[j]);
        while(i<j){
            if( height[i]>height[j]) j--;
            else i++;
            if(max<min(height[j],height[i])*(j-i)) max=min(height[j],height[i])*(j-i);
        }
        return max;
    }
};