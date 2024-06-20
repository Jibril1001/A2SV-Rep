#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int main(){
    int t;
    cin >> t;
    while(t--){
        int size;
        bool sorts=true,done=true;
        cin >> size;
        if(size==1) sorts=false;
        vector<int> arr(size);
        for(int i=0;i<size;i++){
                cin >> arr[i];
                if( sorts==true && i>0){
                    if(arr[i]<arr[i-1]) sorts=false;
                }
        }
        if(size==1){
            cout << "YES" << endl;
            continue;
        }
        if(sorts==false) sort(arr.begin(),arr.end());

        for(int i=1;i<size;i++){
            if(arr[i-1]!=arr[i]-1 && arr[i-1]!=arr[i]){
                cout << "NO" << endl;
                done=false;
                break;
            }
        }
        if(done) cout << "YES" << endl;

    }
}