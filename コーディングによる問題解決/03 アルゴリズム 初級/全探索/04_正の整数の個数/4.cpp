#include <bits/stdc++.h>
using namespace std;

int main(){
    int N;
    cin >> N;
    vector<int> A(N);
    for (int i = 0; i < N; i++) cin >> A[i];

    int cnt = 0;

    for (int i = 0; i < N; i++){
        if(A[i]>0){
            cnt++;
        }
    }

    cout << cnt << endl;

    return 0;
}