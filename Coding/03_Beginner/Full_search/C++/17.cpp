#include <iostream>
#include <vector>
using namespace std;

int main(){
    int N;
    cin >> N;
    vector<int> A(N);
    for (int i = 0; i < N; i++) cin >> A[i];

    int cnt = 0;
    for (int i = 0; i < N; i++){
        if (A[i] >= 2){
            bool flag = true;
            for (int j = 2; j < A[i]-1; j++){
                if (A[i] % j == 0){
                    flag = false;
                    break;
                }
            }if (flag) cnt++;
        }
    }
    cout << cnt << endl;
    return 0;
}