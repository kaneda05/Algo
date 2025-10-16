#include <iostream>
#include <string>
using namespace std;

int main(){
    string S, c;
    cin >> S >> c;
    bool found = false;

    for (char ch : S){
        if (ch == c[0]){
            found = true;
            break;
        }
    }

    cout << (found ? "Yes" : "No") << endl;
    return 0;
}