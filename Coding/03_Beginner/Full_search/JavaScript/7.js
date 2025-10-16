const fs = require("fs");
const input = fs.readFileSync(0, "utf8").trim().split(/\s+/);

const N = Number(input[0]);
const A = input.slice(1).map(Number);

const maxA = Math.max(...A);
let cnt = 0;

for (let i = 0; i < N; i++){
    if (A[i] == maxA){
        cnt++;
    }
}

console.log(cnt);