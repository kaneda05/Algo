#include <iostream>
#include <string>
using namespace std;

int main(){
    string S;
    cin >> S;
    int cnt = 0;

    for (int i = 0; i < (int)S.size()-1; i++){
        if (S[i] == S[i+1]){
            cnt++;
        }
    }

    cout << cnt << endl;
    return 0;
}