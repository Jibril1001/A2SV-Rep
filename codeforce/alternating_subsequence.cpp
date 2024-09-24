#include<iostream>
#include<vector>
using namespace std;

void addlarge(int &index,vector<int> &arr,long long &sum){
    int maxim=arr[index],sign,sign2;
    if (arr[index]<0){
        sign=0;
    }else{
        sign=1;
    }

    for(int i=index;i<arr.size();i++){
        if (arr[i]<0){
            sign2=0;
        }else{
            sign2=1;
        }
        if(sign!=sign2){
            break;
        }
        index=i;
        maxim=max(arr[i],maxim);
    }
    
    sum=sum+maxim;
}

int main(){
    int trials;
    cin >> trials;
    while(trials--){
        int size;
        long long sum=0;
        cin >> size;
        vector<int> arr(size);
        for(int i=0;i<size;i++){
            cin >> arr[i];
        }

        for(int index=0;index<size;){
            addlarge(index,arr,sum);
            index++;
        }
        cout << sum << endl;
    }
}