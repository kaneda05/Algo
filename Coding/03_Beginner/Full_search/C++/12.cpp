#include <bits/stdc++.h>
using namespace std;

int main() {
    int A, B;
    cin >> A >> B;
    int min_num = std::min(A, B);
    int ans = 0;
    for (int i = 1; i <= min_num; i++){
        if (A % i == 0 && B % i == 0){
            ans = i;
        }
    }
    cout << ans << endl;
    return 0;
}