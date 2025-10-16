const fs = require("fs");
const input = fs.readFileSync(0, "utf8").trim().split(/\s+/);

const N = Number(input[0]);
const A = input.slice(1).map(Number);

let ans = -1;
for (let i = 0; i < N; i++){
    if (A[i] > ans){
        ans = A[i];
    }
}

console.log(ans);