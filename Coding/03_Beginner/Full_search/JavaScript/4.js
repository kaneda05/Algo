const fs = require("fs");
const input = fs.readFileSync(0, "utf8").trim().split(/\s+/);

const N = Number(input[0]);
const A = input.slice(1).map(Number);

let flag = false;
let cnt = 0;
for (let i = 0; i < N; i++){
    if (A[i] > 0){
        cnt++;
    }
}

console.log(cnt);