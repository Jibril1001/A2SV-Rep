#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n, k;
    string numbers_str;
    cin >> n >> k;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    sort(arr.begin(), arr.end());

    if (k == 0 && arr[0] == 1) {
        cout << -1 << endl;
        return 0;
    } else if (k == 0 && arr[0] > 1) {
        cout << 1 << endl;
        return 0;
    } else if (k == 1 && n == 1) {
        cout << arr[0] << endl;
        return 0;
    }

    if (arr[k - 1] != arr[k]) {
        cout << arr[k - 1] << endl;
    } else {
        cout << -1 << endl;
    }

    return 0;
}