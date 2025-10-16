#include <iostream>
#include <vector>
using namespace std;

int main(){
    int N, M;
    cin >> N >> M;
    vector<int> A(N), B(M);

    for (int i = 0; i < N; i++) cin >> A[i];
    for (int j = 0; j < M; j++) cin >> B[j];

    int cnt = 0;
    for (int i = 0; i < N; i++){
        for (int j = 0; j < M; j++){
            if (A[i] > B[j]) cnt++;
        }
    }

    cout << cnt << endl;
    return 0;
}