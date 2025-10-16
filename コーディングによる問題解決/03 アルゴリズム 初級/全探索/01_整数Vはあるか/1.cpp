#include <bits/stdc++.h>
using namespace std;

int main(){
    int N, V;
    cin >> N >> V;
    vector<int> A(N);
    for (int i = 0; i < N; i++) cin >> A[i];

    for (int i = 0; i < N; i++){
        if (A[i] == V){
            cout << "Yes" << endl;
            return 0;
        }
    }
    cout << "No" << endl;
    return 0;
}
