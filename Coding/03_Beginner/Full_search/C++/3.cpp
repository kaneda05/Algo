#include <bits/stdc++.h>
using namespace std;

int main(){
    int N, V;
    cin >> N >> V;
    vector<int> A(N);
    for (int i = 0; i < N; i++) cin >> A[i];

    bool flag = false;
    int ans = -1;

    for (int i = 0; i < N; i++){
        if(A[i]==V){
            ans = i;
            flag = true;
        }
    }
    if (flag){
        cout << ans << endl;
    }else{
        cout << -1 << endl;
    }

    return 0;
}