#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, V;
    cin >> N >> V;
    vector<int> A(N);
    for (int i = 0; i < N; i++) cin >> A[i];

    int cnt = 0;
    for (int i = 0; i < N; i++) {
        if (A[i] == V) cnt++;
    }

    cout << cnt << endl;
    return 0;
}
