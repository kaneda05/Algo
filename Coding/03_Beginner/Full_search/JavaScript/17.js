const fs = require("fs");
const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);
const N = input[0];
const A = input.slice(1);

let cnt = 0;
for (let i = 0; i < N; i++){
    if (A[i] >= 2){
        let flag = true;
        for (let j = 2; j < A[i]-1; j++){
            if (A[i] % j == 0){
                flag = false;
                break;
            }
        }
        if (flag) cnt++;
    }
}

console.log(cnt);